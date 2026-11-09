---
name: reels-oriven
description: >
  Edita os Reels e TikToks da ORIVEN a partir dos vídeos que o Edyfran grava no celular: transcreve,
  propõe o corte, junta os takes na ordem do roteiro, padroniza em 1080x1920, coloca a legenda na
  identidade da marca e entrega o MP4 pronto com a legenda do post. Use sempre que ele pedir pra
  editar, cortar, montar, juntar ou legendar vídeo da ORIVEN: "edita esse reels", "corta esses
  vídeos", "junta os takes", "põe legenda", "deixa pronto pra postar", "gravei o vídeo do drop",
  ou quando aparecer vídeo novo em conteudo/reels/. Não use as skills da Uniqee (roteirista-video,
  ganchos-virais-uniqee, analisador-reels-uniqee) pra nada da ORIVEN.
---

# Reels da ORIVEN · do celular ao MP4 pronto

> **Caminho principal desde 2026-11-09: a Fábrica de Conteúdo** (ver `_contexto/integracoes.md`).
> Quando o Edyfran pedir pra editar um Reels, sugira primeiro abrir uma conversa na pasta da
> Fábrica e colar o pedido do `marca/PEDIDOS.md` de lá, com o caminho do vídeo. Esta skill é o
> plano B: use quando ele pedir pra fazer aqui ou a Fábrica não estiver disponível.

O Edyfran grava com o celular e quer o vídeo pronto pra postar: cortado, na ordem certa, com legenda
na cara da marca. Você faz a edição inteira aqui, com ffmpeg e faster-whisper (já instalados), usando
o script `scripts/reels.py` desta pasta. Ele faz a parte mecânica; o seu trabalho é decidir o corte,
revisar o texto e cuidar da marca.

## Antes de começar

- Leia a marca (linha "marca" do mapa do `AGENTS.md`): o guia de design e o tom de voz. Valem as
  regras de sempre: "você", nada de duplo sentido, palavrão ou promessa exagerada, versículo com
  referência e versão, nome **ORIVEN** (nunca "OURIVEN"), nada da Uniqee.
- Pasta do vídeo: `conteudo/reels/<tema>/`. Os arquivos do celular vão em `bruto/`. Se ele mandou o
  vídeo de outro lugar, copie pra lá (não mova o original).
- Roteiro: se existe, vem do marketing da ORIVEN (ou de `roteiro.md` na pasta do tema). Se não tem
  roteiro, siga a fala gravada e o objetivo que ele disser. Não chame as skills da Uniqee.

## 1. Transcrever e propor o corte

```bash
python <esta-skill>/scripts/reels.py transcrever conteudo/reels/<tema>/bruto/*.mp4
```

Sai um `.transcricao.json` por vídeo, com o tempo de cada frase e de cada palavra. A primeira vez
baixa o modelo do Whisper (alguns minutos); depois é rápido. Se a fala for difícil, rode com
`--modelo medium` (mais lento, erra menos).

Com isso, monte a proposta de corte e **mostre antes de renderizar**: quais trechos entram, em que
ordem, de que segundo a que segundo, e a duração final. Recomende um caminho e diga por quê. Critérios:

- Os 3 primeiros segundos seguram ou perdem a pessoa: comece no gancho, sem "oi gente" nem respiro.
- Corte tropeço, repetição, silêncio longo e o take ruim quando houver um melhor da mesma fala.
- Reels de produto da ORIVEN costuma render entre 15 e 40 segundos. Mais longo só se o conteúdo pede.
- Deixe uns 0,2 s de folga antes e depois da fala pra o corte não comer sílaba.

Com o ok, grave `conteudo/reels/<tema>/plano.json`:

```json
{"trechos": [{"arquivo": "bruto/take2.mp4", "inicio": 0.4, "fim": 6.1},
             {"arquivo": "bruto/take1.mp4", "inicio": 3.0, "fim": 9.8}]}
```

## 2. Montar

```bash
python <esta-skill>/scripts/reels.py montar conteudo/reels/<tema>/plano.json conteudo/reels/<tema>/montado.mp4
```

Corta cada trecho, enquadra em 1080x1920 a 30 fps (vídeo deitado é cortado no centro, então avise se
a peça ficar fora do quadro), junta e normaliza o volume pro padrão das redes. Take sem áudio ganha
silêncio pra não quebrar a junção.

## 3. Legenda: gerar, revisar, queimar

```bash
python <esta-skill>/scripts/reels.py legendas conteudo/reels/<tema>/montado.mp4 conteudo/reels/<tema>/legenda.ass
```

Gera a legenda em blocos de até 3 palavras, em caixa alta, Syne ExtraBold off-white com contorno
preto carvão, acima da área que a interface do Instagram cobre. As fontes estão em `fonts/`.

**Revise o `.ass` antes de queimar.** O Whisper erra exatamente o que mais importa: no teste,
"ORIVEN" virou "ORI VEM" e "drop" virou "DRAP". Confira linha a linha e corrija:

- o nome da marca, o nome do drop e das estampas, termos em inglês;
- o versículo: confira referência e texto na versão citada. Nunca invente nem complete de memória;
- palavrão ou duplo sentido que escapou na fala: avise o Edyfran em vez de só apagar.

Recursos de marca, com moderação (o laranja é acento, no máximo uma palavra por frase):

- destacar uma palavra em laranja: `{\c&H002B77D9&}PALAVRA{\c&H00E8EFF2&}`
- referência bíblica no topo, em JetBrains Mono: uma linha com o estilo `Referencia`, por exemplo
  `Dialogue: 0,0:00:04.30,0:00:07.00,Referencia,,0,0,0,,SL 46:10 · ARA`

Depois:

```bash
python <esta-skill>/scripts/reels.py queimar conteudo/reels/<tema>/montado.mp4 conteudo/reels/<tema>/legenda.ass conteudo/reels/<tema>/final.mp4
python <esta-skill>/scripts/reels.py frame conteudo/reels/<tema>/final.mp4 conteudo/reels/<tema>/frame.png --tempo 2
```

Olhe o frame (e mais um ou dois em momentos com destaque ou referência) antes de dizer que está pronto:
legenda legível, sem cobrir a estampa, sem palavra cortada na borda. Se a legenda tapar a peça, suba
ou desça o `MarginV` do estilo no `.ass` e queime de novo.

## 4. Entregar

- `final.mp4` na pasta do tema.
- `legenda.txt` com o texto do post: primeira linha que segura, corpo curto, CTA ligado à pré-venda ou
  ao "comenta PALAVRA", 5 a 8 hashtags de nicho, e o versículo com referência e versão se aparecer no
  vídeo. Escreva no tom da marca. Preço, prazo e estoque só se ele confirmou.
- Diga a duração final e o que foi cortado, em duas ou três linhas.

Agendar só se ele pedir: Metricool, **sempre como rascunho pra revisão**. Nada vai ao ar sem o sim dele.

## Se algo der errado

- `ffmpeg` ou `faster-whisper` sumiu: diga o que falta e o comando pra instalar
  (`winget install Gyan.FFmpeg` / `pip install faster-whisper`).
- Fonte trocada no vídeo (cara de Arial): confira se `fonts/` ainda tem os três `.ttf`.
- Ajuste pedido depois de pronto: mexa só no passo afetado (plano, legenda ou texto) e refaça dali
  pra frente, sem retranscrever tudo.
