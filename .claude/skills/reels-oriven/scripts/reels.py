"""Ferramenta de edição de Reels da ORIVEN (ffmpeg + faster-whisper).

Subcomandos:
  transcrever <video...> [--modelo small]           -> <video>.transcricao.json (segmentos e palavras com tempo)
  montar <plano.json> <saida.mp4>                   -> corta, padroniza 1080x1920 30fps e junta os trechos
  legendas <video.mp4> <saida.ass> [--palavras 3]   -> transcreve o vídeo montado e gera a legenda ASS na marca
  queimar <video.mp4> <legenda.ass> <saida.mp4>     -> grava a legenda no vídeo (fontes da pasta fonts/)
  frame <video.mp4> <saida.png> [--tempo 1.5]       -> tira um frame pra conferir

plano.json:
  {"trechos": [{"arquivo": "bruto/take1.mp4", "inicio": 0.4, "fim": 6.2}, ...]}
  Caminhos relativos são lidos a partir da pasta do plano.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTES = os.path.normpath(os.path.join(AQUI, "..", "fonts"))

# Paleta Aurora em formato ASS (&HAABBGGRR)
OFF_WHITE = "&H00E8EFF2"   # #F2EFE8
CARVAO = "&H001A1A1A"      # #1A1A1A
LARANJA = "&H002B77D9"     # #D9772B (acento: use com {\\c&H002B77D9&} numa palavra)


def rodar(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        sys.exit(f"falhou: {' '.join(cmd[:3])}...")
    return r


def tem_audio(caminho):
    r = rodar(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
               "stream=index", "-of", "csv=p=0", caminho])
    return bool(r.stdout.strip())


def transcrever_arquivo(caminho, modelo="small"):
    import numpy as np
    from faster_whisper import WhisperModel
    # o áudio sai pelo ffmpeg (16 kHz mono): evita depender da versão do PyAV instalada
    bruto = subprocess.run(["ffmpeg", "-v", "error", "-i", caminho, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                           capture_output=True).stdout
    audio = np.frombuffer(bruto, np.int16).astype(np.float32) / 32768.0
    m = WhisperModel(modelo, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(audio, language="pt", word_timestamps=True, vad_filter=True)
    saida = []
    for s in segs:
        saida.append({
            "inicio": round(s.start, 2), "fim": round(s.end, 2), "texto": s.text.strip(),
            "palavras": [{"inicio": round(w.start, 2), "fim": round(w.end, 2), "texto": w.word.strip()}
                         for w in (s.words or [])],
        })
    return saida


def cmd_transcrever(a):
    for v in a.videos:
        dados = transcrever_arquivo(v, a.modelo)
        destino = os.path.splitext(v)[0] + ".transcricao.json"
        with open(destino, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=1)
        print(f"{v}: {len(dados)} trechos -> {destino}")
        for s in dados:
            print(f"  [{s['inicio']:6.2f} - {s['fim']:6.2f}] {s['texto']}")


def cmd_montar(a):
    with open(a.plano, encoding="utf-8") as f:
        plano = json.load(f)
    base = os.path.dirname(os.path.abspath(a.plano))
    tmp = tempfile.mkdtemp(prefix="reels-")
    partes = []
    vf = ("scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
          "setsar=1,fps=30,format=yuv420p")
    for i, t in enumerate(plano["trechos"]):
        src = t["arquivo"] if os.path.isabs(t["arquivo"]) else os.path.join(base, t["arquivo"])
        dur = float(t["fim"]) - float(t["inicio"])
        out = os.path.join(tmp, f"p{i:02d}.mp4")
        cmd = ["ffmpeg", "-y", "-ss", str(t["inicio"]), "-t", f"{dur:.3f}", "-i", src]
        if not tem_audio(src):
            cmd += ["-f", "lavfi", "-t", f"{dur:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
                    "-map", "0:v", "-map", "1:a"]
        cmd += ["-vf", vf, "-af", "aresample=48000", "-ac", "2", "-c:v", "libx264", "-preset", "medium",
                "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-shortest", out]
        rodar(cmd)
        partes.append(out)
        print(f"trecho {i + 1}: {os.path.basename(src)} {t['inicio']}s-{t['fim']}s")
    lista = os.path.join(tmp, "lista.txt")
    with open(lista, "w", encoding="utf-8") as f:
        f.writelines(f"file '{p}'\n" for p in partes)
    juntos = os.path.join(tmp, "juntos.mp4")
    rodar(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", juntos])
    rodar(["ffmpeg", "-y", "-i", juntos, "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.saida])
    print(f"montado: {a.saida}")


def ts(seg):
    h = int(seg // 3600); m = int(seg % 3600 // 60); s = seg % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def cmd_legendas(a):
    dados = transcrever_arquivo(a.video, a.modelo)
    palavras = [w for s in dados for w in s["palavras"] if w["texto"]]
    linhas = []
    grupo = []
    for w in palavras:
        grupo.append(w)
        fim_frase = w["texto"][-1:] in ".!?,"
        if len(grupo) >= a.palavras or fim_frase:
            linhas.append(grupo); grupo = []
    if grupo:
        linhas.append(grupo)
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Legenda,Syne ExtraBold,76,{OFF_WHITE},{OFF_WHITE},{CARVAO},&H64000000,0,0,0,0,100,100,1,0,1,5,0,2,90,90,460,1
Style: Referencia,JetBrains Mono Medium,40,{OFF_WHITE},{OFF_WHITE},{CARVAO},&H64000000,0,0,0,0,100,100,2,0,1,3,0,8,90,90,260,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    eventos = []
    for i, g in enumerate(linhas):
        ini = g[0]["inicio"]
        fim = g[-1]["fim"]
        if i + 1 < len(linhas):
            fim = max(fim, min(linhas[i + 1][0]["inicio"], fim + 0.3))
        texto = ""
        for w in g:  # "pré" + "-venda" vira "pré-venda", sem espaço antes de hífen ou pontuação
            t = w["texto"]
            texto += t if (not texto or t[:1] in "-.,!?;:") else " " + t
        texto = texto.upper()
        eventos.append(f"Dialogue: 0,{ts(ini)},{ts(fim)},Legenda,,0,0,0,,{texto}")
    with open(a.saida, "w", encoding="utf-8-sig") as f:
        f.write(cab + "\n".join(eventos) + "\n")
    print(f"{len(eventos)} linhas de legenda -> {a.saida}")
    for e in eventos:
        print("  " + e.split(",", 1)[1].split(",,0,0,0,,")[0][:30], "|", e.rsplit(",,", 1)[-1])


def caminho_filtro(p):
    # escapa caminho Windows pro filtro do ffmpeg (C\:/pasta/arquivo)
    p = os.path.abspath(p).replace("\\", "/")
    return p.replace(":", "\\:").replace("'", "\\'")


def cmd_queimar(a):
    vf = f"subtitles='{caminho_filtro(a.legenda)}':fontsdir='{caminho_filtro(FONTES)}'"
    rodar(["ffmpeg", "-y", "-i", a.video, "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-c:a", "copy", "-movflags", "+faststart", a.saida])
    print(f"final: {a.saida}")


def cmd_frame(a):
    rodar(["ffmpeg", "-y", "-ss", str(a.tempo), "-i", a.video, "-frames:v", "1", a.saida])
    print(f"frame: {a.saida}")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("transcrever"); s.add_argument("videos", nargs="+"); s.add_argument("--modelo", default="small")
    s = sub.add_parser("montar"); s.add_argument("plano"); s.add_argument("saida")
    s = sub.add_parser("legendas"); s.add_argument("video"); s.add_argument("saida")
    s.add_argument("--palavras", type=int, default=3); s.add_argument("--modelo", default="small")
    s = sub.add_parser("queimar"); s.add_argument("video"); s.add_argument("legenda"); s.add_argument("saida")
    s = sub.add_parser("frame"); s.add_argument("video"); s.add_argument("saida"); s.add_argument("--tempo", type=float, default=1.5)
    a = p.parse_args()
    {"transcrever": cmd_transcrever, "montar": cmd_montar, "legendas": cmd_legendas,
     "queimar": cmd_queimar, "frame": cmd_frame}[a.cmd](a)


if __name__ == "__main__":
    main()
