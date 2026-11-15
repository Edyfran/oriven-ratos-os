STAR='<svg class="star" viewBox="-1 -1 2 2" width="{s}" height="{s}"><path d="M0,-1 C0.1,-0.1 0.1,-0.1 1,0 C0.1,0.1 0.1,0.1 0,1 C-0.1,0.1 -0.1,0.1 -1,0 C-0.1,-0.1 -0.1,-0.1 0,-1Z" fill="{c}"/></svg>'
def star(s,c='#D9772B'): return STAR.format(s=s,c=c)
HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=JetBrains+Mono:wght@400;500;700&display=block" rel="stylesheet">
<link rel="stylesheet" href="base.css"><style>{css}</style></head><body class="{cls}">
<svg style="position:absolute;width:0;height:0"><filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4" stitchTiles="stitch"/></filter></svg>
'''
def page(n,body,css='',cls='',numcolor=''):
    return HEAD.format(css=css,cls=cls)+body+f'<div class="num m" style="{numcolor}">{n:02d} / 08</div><div class="prog" style="width:{n/8*100:.1f}%"></div><script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script></body></html>'
S={}
S[1]=page(1,f'''
<img class="foto" src="../imagens/oriente.jpg" style="object-position:center">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,26,26,.55) 0%,rgba(26,26,26,0) 18%,rgba(26,26,26,0) 52%,rgba(26,26,26,.85) 72%,rgba(26,26,26,.97) 100%)"></div>
<div class="tag m">{star(22)}&nbsp; Pack de Natal · ORIENTE</div>
<div style="position:absolute;left:64px;right:64px;bottom:110px">
 <div class="t" style="font-size:132px">Vimos a<br>estrela{star(70)}</div>
 <p style="margin-top:34px;font-size:36px;max-width:820px;color:var(--off)">Pack de Natal ORIENTE: três camisetas, uma mesma estrela.</p>
</div>''')
S[2]=page(2,f'''
<div style="position:absolute;right:-260px;top:120px;opacity:.07">{star(1100,'#F2EFE8')}</div>
<div class="tag m" style="color:var(--laranja)">MT 2:2 · ARA</div>
<div style="position:absolute;left:64px;right:110px;top:150px;bottom:110px;display:flex;flex-direction:column;justify-content:center">
 <p style="font-size:46px;line-height:1.35">Antes do presépio, da árvore e da ceia, o Natal tinha <b style="font-weight:800">uma estrela</b>. Uns magos do Oriente viram e foram atrás dela até encontrar Jesus.</p>
 <div style="margin:64px 0;border-left:8px solid var(--laranja);padding:10px 0 10px 40px">
  <div class="t" style="font-size:70px;line-height:1.05;font-weight:800">"Porque vimos a sua estrela no Oriente e viemos para adorá-lo."</div>
 </div>
 <p style="color:var(--areia);font-size:40px">A estrela de quatro pontas está na ORIVEN desde o primeiro dia. Neste Natal, ela conta essa história.</p>
</div>''')
row=lambda i,nome,cor,hexc,borda: f'''<div style="display:flex;align-items:center;gap:40px;padding:58px 0;border-top:3px solid var(--carvao)">
 <div class="m" style="font-size:30px;width:70px">{i}</div>
 <div style="width:120px;height:120px;border-radius:50%;background:{hexc};border:3px solid {borda};display:flex;align-items:center;justify-content:center">{star(44)}</div>
 <div><div class="t" style="font-size:76px">{nome}</div><div class="m" style="font-size:24px;margin-top:12px;color:var(--chumbo)">{cor}</div></div></div>'''
S[3]=page(3,f'''
<div style="position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--carvao)"></div>
<div class="tag m">O pack</div>
<div style="position:absolute;left:64px;right:64px;top:170px">
 <div class="t" style="font-size:170px;margin-bottom:70px">O pack</div>
 {row('01','Emanuel','off-white','#F2EFE8','#1A1A1A')}
 {row('02','Oriente','preto carvão','#1A1A1A','#1A1A1A')}
 {row('03','Luz','areia','#C8B89A','#1A1A1A')}
 <p style="border-top:3px solid var(--carvao);padding-top:50px;font-size:38px">Três peças, três cores e a mesma estrela no peito.</p>
</div>''',cls='claro')
S[4]=page(4,f'''
<img class="foto" src="../imagens/emanuel.jpg">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,26,26,.85) 0%,rgba(26,26,26,0) 16%,rgba(26,26,26,0) 58%,rgba(26,26,26,.9) 74%,rgba(26,26,26,.98) 100%)"></div>
<div class="tag m">{star(22)}&nbsp; 01 · off-white</div>
<div style="position:absolute;left:64px;right:64px;bottom:96px">
 <div class="t" style="font-size:110px">Emanuel</div>
 <p style="margin-top:22px;font-size:32px">O nome que resume o Natal. Uma palavra, uma estrela e a tradução embaixo, discreta no peito.</p>
 <p style="margin-top:20px;font-size:30px;color:var(--areia)">"…e ele será chamado pelo nome de Emanuel (que quer dizer: Deus conosco)." <br><span class="m" style="font-size:22px;color:var(--laranja)">MT 1:23 · ARA</span></p>
 <div class="m" style="margin-top:26px;font-size:22px;display:inline-block;background:var(--off);color:var(--carvao);padding:10px 16px">A mais fácil de dar de presente</div>
</div>''')
S[5]=page(5,f'''
<div class="tag m">{star(22)}&nbsp; 02 · preto carvão</div>
<div style="position:absolute;left:64px;right:64px;top:130px;height:780px;border-radius:18px;overflow:hidden"><img src="../imagens/oriente.jpg" style="width:100%;height:100%;object-fit:cover;object-position:center 8%"></div>
<div style="position:absolute;left:64px;right:64px;top:950px">
 <div style="display:flex;align-items:baseline;justify-content:space-between"><div class="t" style="font-size:104px">Oriente</div><div class="m" style="font-size:24px;color:var(--laranja)">MT 2:2 · ARA</div></div>
 <p style="margin-top:22px;font-size:32px">O selo dos magos. A frase de Mateus gira em volta de uma estrela em traço fino, como um emblema.</p>
 <p style="margin-top:18px;font-size:32px;color:var(--areia)">Na camiseta preta, é a peça que faz alguém perguntar o que é aquilo. Aí você conta.</p>
</div>''')
S[6]=page(6,f'''
<img class="foto" src="../imagens/luz.jpg"><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,26,26,.85) 0%,rgba(26,26,26,0) 16%)"></div>
<div class="tag m" style="color:var(--off);text-shadow:0 2px 10px rgba(0,0,0,.6)">{star(22)}&nbsp; 03 · areia</div>
<div style="position:absolute;left:64px;right:64px;bottom:80px;background:var(--off);color:var(--carvao);padding:44px 48px;border-left:10px solid var(--laranja)">
 <div style="display:flex;align-items:baseline;justify-content:space-between"><div class="t" style="font-size:100px">Luz</div><div class="m" style="font-size:22px;color:var(--chumbo)">JO 1:5 · NVI</div></div>
 <p style="margin-top:14px;font-size:30px">Três letras pesadas com a estrela acesa atrás.</p>
 <p style="margin-top:14px;font-size:30px;font-weight:700">"A luz brilha nas trevas, e as trevas não a derrotaram."</p>
 <p style="margin-top:14px;font-size:30px;color:var(--chumbo)">Começou no Natal e não apaga em janeiro.</p>
</div>''',numcolor='color:#F2EFE8;text-shadow:0 2px 10px rgba(0,0,0,.6)')
item=lambda t: f'<div style="display:flex;gap:30px;align-items:flex-start;padding:30px 0;border-bottom:2px solid rgba(26,26,26,.15)"><div style="padding-top:6px">{star(34)}</div><p style="font-size:36px">{t}</p></div>'
S[7]=page(7,f'''
<div style="position:absolute;right:-220px;bottom:-300px;width:560px;height:560px;background:var(--areia);border-radius:50%;opacity:.5"></div>
<div class="tag m">Os detalhes</div>
<div style="position:absolute;left:64px;right:64px;top:170px">
 <div class="t" style="font-size:120px;margin-bottom:40px">Os<br>detalhes</div>
 {item('Modelagem <b>oversized</b>.')}
 {item('Estampa de <b>9 cm no peito</b>, impressa em DTF.')}
 {item('<b>Off-white</b>, <b>preto carvão</b> ou <b>areia</b>.')}
 {item('Sem gorro e sem pisca-pisca: dá pra usar o ano inteiro.')}
 {item('<b>Pré-venda:</b> você garante a sua agora e a gente produz depois.')}
</div>''',cls='claro')
S[8]=page(8,f'''
<div style="position:absolute;left:50%;top:44%;width:900px;height:900px;transform:translate(-50%,-50%);background:radial-gradient(circle,rgba(217,119,43,.22) 0%,rgba(217,119,43,0) 62%)"></div>
<div style="position:absolute;left:50%;top:30%;transform:translate(-50%,-50%)">{star(260)}</div>
<div style="position:absolute;left:64px;right:64px;top:600px;text-align:center">
 <div class="t" style="font-size:118px">Viu a<br>estrela?</div>
 <p style="margin:48px auto 0;font-size:40px;max-width:860px">Comenta <span class="t" style="background:var(--laranja);color:var(--carvao);padding:4px 16px;font-size:40px;letter-spacing:0">Estrela</span> aqui embaixo que a gente te manda a pré-venda no direct.</p>
</div>
<div style="position:absolute;left:0;right:0;bottom:90px;text-align:center;font-family:Archivo;font-weight:300;font-size:40px;letter-spacing:22px;text-transform:uppercase">O<span style="position:relative;top:-14px;margin-left:-14px;margin-right:8px">{star(22)}</span>RIVEN</div>''')
for n,h in S.items(): open(f'slide-{n:02d}.html','w').write(h)
