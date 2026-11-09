---
name: carrossel-oriven
description: >
  Ajustes da ORIVEN pra skill global de carrossel da Ratos (/carrossel): onde está a marca, o tom
  com o cliente, os dois tipos de carrossel da ORIVEN (drop/produto e editorial), de onde vêm as
  imagens e onde fica o estilo visual. Roda junto com a /carrossel, nunca sozinha.
  Use sempre que pedirem carrossel neste sistema: "faz um carrossel", "carrossel do drop",
  "carrossel da estampa X", "slides pro Instagram", "carrossel pro TikTok".
---

# Carrossel da ORIVEN · complemento da /carrossel

A skill global `/carrossel` (da Ratos) faz o trabalho: texto, HTML e PNG. Ela é global e também
serve à Uniqee, então **não editar nenhum arquivo dela**. Esta skill só diz o que muda quando o
carrossel é da ORIVEN. Seguir o fluxo dela com as trocas abaixo; onde as duas divergem, vale esta.

## Onde as coisas estão (no lugar dos caminhos da /carrossel)

- **Identidade visual:** a marca (linha "marca" do mapa do `AGENTS.md`), começando pelo guia de
  design. A /carrossel procura em `marca/design-guide.md`; aqui é a pasta da marca do mapa. O guia
  já está preenchido: **não rodar o setup de cores, fontes e logo** dela.
- **Tom com o público:** o tom de voz da marca, na mesma pasta. O `preferencias.md` é como o agente
  fala com o Edyfran, não com o cliente: não usar como tom do carrossel. O tom já existe, então
  **não rodar o setup de tom** dela.
- **Contexto e foco:** `_contexto/empresa.md` e `_contexto/estrategia.md`.
- **Saída:** `conteudo/carrosseis/<tema>/`, na estrutura que a /carrossel já usa.

## Estilo visual da ORIVEN

O estilo escolhido na /carrossel vai pro `design-carrossel.md` global, que a Uniqee também usa.
Pra ORIVEN, o estilo mora em `design-oriven.md`, **nesta pasta**.

- Se `design-oriven.md` existe: usar ele como regras de design, no lugar do `design-carrossel.md`.
- Se não existe (primeira vez): fazer a pergunta de estilo da /carrossel (minimalista, elaborado,
  tweet), copiar o arquivo de estilo escolhido das `references/` dela pra `design-oriven.md` aqui,
  e ajustar a cópia à paleta Aurora e às fontes do guia. O `design-carrossel.md` global não muda.
- Recomendar **minimalista** na pergunta: combina com o clima da marca (limpo, off-white, preto
  carvão, laranja só de acento) e com o carrossel do Drop 01.

## Regras da marca que valem em todo slide

- Tratamento por **você**. Nada de "tu", mesmo nos textos de exemplo da /carrossel.
- Versículo sempre com referência e versão, no formato `LIVRO CAP:VERS · VERSÃO` em JetBrains Mono.
  Nunca inventar nem "adaptar" versículo como se fosse literal. Na dúvida do texto exato, avisar.
- Laranja aurora no máximo como acento. Nada de verde neon nem cor fora da paleta.
- O nome é **ORIVEN**. Nunca "OURIVEN".
- Nada de duplo sentido, palavrão ou promessa exagerada (prazo, estoque, resultado).
- Nunca debochar de Deus, da Bíblia ou de símbolo sagrado. Ironia leve só sobre a vida e a rotina.
- Nada da Uniqee: nome, cores, skills ou linguagem.
- Logo: o arquivo indicado no guia. Ele tem fundo off-white, então em slide escuro usar o
  wordmark em texto (ORIVEN, sans fina, caixa alta e espaçada, estrela de quatro pontas junto ao O).

## Os dois tipos de carrossel

No briefing da /carrossel, a primeira pergunta é o tipo.

**Drop/produto** (vitrine de coleção ou estampa, pra vender). Não usar o arco de reportagem (tese,
mecanismo, dado com fonte): aqui ninguém precisa de estatística, precisa ver a peça e querer.
O caminho que funcionou no Drop 01: capa com o nome do drop, mapa das peças, uma lâmina por estampa
seguida da lâmina do versículo dela, detalhes (tecido, oversized, frente e costas, DTF) e o CTA
("comenta PALAVRA" ou pré-venda). É um ponto de partida, não um molde: ajustar ao drop.
- Preço, prazo e estoque só se o Edyfran confirmar. Nunca inventar.
- O CTA conversa com a pré-venda e com os roteiros de DM do comercial da ORIVEN.

**Editorial** (fé no dia a dia, bastidores, a história de uma estampa). Usar o arco narrativo da
/carrossel normalmente, com as regras da marca acima. Sem dado inventado: opinião honesta vale
mais que número sem fonte.

## Imagens

- Estampas, mockups e fotos vêm da pasta `Artes/` da ORIVEN (um nível acima deste sistema; os
  mockups ficam em `Artes/Mockups/`) ou da skill de designer de estampas da ORIVEN.
- Copiar as usadas pra `conteudo/carrosseis/<tema>/imagens/`.
- Nunca usar imagem genérica de IA no lugar da peça. Se faltar mockup, pedir ao designer de
  estampas ou ao Kittl, e mostrar antes de usar.

## Depois de pronto

- Se o Edyfran pedir pra agendar: Metricool, **sempre como rascunho pra revisão**. Nunca publicar
  direto.
- O marketing da ORIVEN pode ter mandado o carrossel a partir do calendário: nesse caso, o tema, o
  pilar e o gancho já vêm de lá.
