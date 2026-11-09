<!-- quem alimenta: o /setup semeia na entrevista; o /atualizar acrescenta quando algo passa a estar hospedado. Lido quando a sessão precisa saber onde algo está (mapa). -->
# Infra

> Onde as coisas estão hospedadas: site, domínio, servidor, banco, DNS, email, área de membros.
> É diferente de `integracoes.md` (o que você usa) e aponta pra onde cada coisa **mora**.
> Sem chave, sem senha. Aqui vai o nome do serviço, o endereço e quem tem acesso.

| o quê | onde mora (serviço) | endereço | quem acessa e como | observações |
|---|---|---|---|---|
| perfil da marca (vitrine e venda) | Instagram | | Edyfran | único canal no ar em 2026-11-09; sem site, loja ou domínio |
| servidor da Ratoeira | VPS Hostinger (Ubuntu 24.04, `srv2142624`) | https://srv2142624.hstgr.cloud · IP 179.197.231.82 | Edyfran: painel/chat da Ratoeira (usuário `edyfran`) e SSH `root` com a chave `ratoeira` | Ratoeira 0.13.19; ORIVEN em `/srv/ratoeira/areas/trabalho/oriven-ratos-os`, Uniqee ao lado em `uniqee-ratos-os` |
| cópia de segurança do sistema | GitHub (privado) | https://github.com/Edyfran/oriven-ratos-os | Edyfran | ponte entre este computador e a Ratoeira |
