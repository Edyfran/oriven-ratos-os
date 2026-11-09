<!-- quem alimenta: o /setup semeia na entrevista; o /atualizar acrescenta integração nova, acesso novo ou "não alcanço"; a /faxina confere e pergunta. Lido antes de dizer "não consigo" e ao criar skill. -->
# Integrações

> O que o negócio usa e como o agente alcança cada coisa. **"não ligada" é resposta válida:** é assim
> que o agente sabe que aquilo existe e dá pra ligar, em vez de achar que é impossível.
> Chave nunca fica aqui. Chave mora no `.env` (fora do git) ou no gerenciador de senha; aqui vai só o
> nome da variável. O cardápio do que dá pra ligar está em `sistema/templates/integracoes/catalogo.md`.

| integração | pra quê | como o agente alcança | estado | última checagem |
|---|---|---|---|---|
| Instagram | vitrine e canal de venda (pré-venda, DM) | via Metricool (agendar como rascunho); DM só você, na mão | ligada (via Metricool) | 2026-11-09 |
| TikTok | conteúdo, reaproveitando os Reels | via Metricool | ligada (via Metricool) | 2026-11-09 |
| Metricool | métricas, melhores horários, agendamento (sempre rascunho pra revisão) | MCP (conector do Claude) | ligada | 2026-11-09 |
| Notion | "ORIVEN Escritório": tarefas, calendário editorial, banco de estampas, parceiros | MCP (conector do Claude) | ligada | 2026-11-09 |
| Notion · Pedidos ORIVEN | pedidos da pré-venda e vendas: cliente, estampa, tamanho, cor, pagamento, status, rastreio. Base da grade de tamanhos e do pedido de DTF | MCP (conector do Claude), data source `collection://23951a29-76af-4d67-987a-a3c7e39a6af9` · [abrir](https://app.notion.com/p/aa129a1303c04d5c9eaddf3292b351d0) | ligada | 2026-11-09 |
| Pix e link de pagamento | como o cliente paga na pré-venda | só você, na mão (o pagamento é marcado na base Pedidos) | não ligada | 2026-11-09 |
| Canva | artes estáticas e capas | MCP (conector do Claude) | ligada | 2026-11-09 |
| Kittl | mockups e geração de arte | MCP (conector do Claude) | ligada | 2026-11-09 |
| Fábrica de Conteúdo com IA | editar os Reels do celular (corte, legenda, peças animadas, trilha, capa) no estilo `oriven-celular`, com a marca em `marca/` | pasta própria em `C:\Users\medei\fabrica-de-conteudo` (fora do OneDrive de propósito): abrir uma conversa nessa pasta e colar um pedido do `marca/PEDIDOS.md` | ligada | 2026-11-09 |
| ffmpeg + faster-whisper (local) | editar e legendar os Reels (skill reels-oriven) | CLI | ligada | 2026-11-09 |
| Ratoeira (VPS) | rodar rotinas fora deste computador | a definir | não ligada | 2026-11-09 |

## Os sete assuntos que todo negócio tem

| assunto | o que usa hoje | estado |
|---|---|---|
| mensagem com cliente | nada (DM do Instagram, na mão) | não ligada |
| tarefa e prazo | nada (as skills preveem o Escritório no Notion) | não ligada |
| email | nada | não ligada |
| agenda | nada | não ligada |
| dinheiro entrando e saindo | entrada: Pix e link de pagamento, registrados na base Pedidos ORIVEN (Notion). Saída: nada | ligada em parte (2026-11-09) |
| ficha do cliente | base Pedidos ORIVEN (Notion): nome, @, WhatsApp, endereço de entrega | ligada (2026-11-09) |
| reunião | nada | não ligada |
