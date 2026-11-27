# Publicação diária — erppro.pages.dev

Este repositório guarda o site **https://erppro.pages.dev** (Cloudflare Pages, projeto `erppro`, conta Cloudflare do contato.erppro@gmail.com). A Cloudflare **troca o site inteiro** a cada envio: sempre publique a pasta `site/` completa, nunca só a página nova.

Dono: Adriano Fernandes (ERPPro). Responda a ele em português, direto, tom leve, com emojis que combinem com o assunto.

## O que fazer em cada rodada (1 guia novo por dia)

1. **Escolher o tema**: pegue o primeiro item da fila abaixo que ainda não esteja em `paginas.json` (nem em `fora_do_pages_dev`). Se a fila acabar, crie um tema novo do mesmo estilo e acrescente na fila.
2. **Achar a página certa do site** para o único link do guia: abra `https://erppro.com.br/sitemap_index.xml` no navegador e escolha a página do erppro.com.br que é dona do assunto. Se não houver uma específica, use `https://erppro.com.br/`. Nunca invente URL.
3. **Escrever o guia** em `site/<slug>/index.html`, copiando a estrutura e o CSS de `site/crediario-proprio/index.html`:
   - `<title>`, meta description, `<link rel="canonical" href="https://erppro.pages.dev/<slug>/">`, autor "Adriano Fernandes"
   - JSON-LD com `Article` (author Adriano Fernandes, publisher ERPPro com url https://erppro.com.br/) e `FAQPage` com 3 perguntas
   - Link "← Conheça o ERPPro" para `/` no topo
   - 1 H1, de 4 a 6 H2, perguntas frequentes no fim e um bloco final do ERPPro com **um único link** para o erppro.com.br (texto do link natural, com a palavra-chave da página do site)
   - Conteúdo útil de verdade, 900 a 1.400 palavras, texto próprio (nunca copiar o erppro.com.br)
4. **Registrar** o guia em `paginas.json` (`slug`, `titulo`, `resumo`, `icone`, `palavra_chave`, `link_site`, `publicado_em` = data de hoje).
5. **Montar**: `python3 scripts/build.py` (atualiza a capa, `sitemap.xml`, `robots.txt` e gera `dist/site.zip.b64`). A pasta `dist/` não vai para o git.
6. **Salvar no GitHub**: commit e push na branch `main`.
7. **Publicar pela Cloudflare** no Chrome do Adriano (veja abaixo).
8. **Conferir**: abra `https://erppro.pages.dev/<slug>/` e a capa; confira que o guia novo e os antigos estão no ar.
9. **Avisar o Adriano** com uma mensagem curta: tema publicado, link, e o H1/H2 usados.

## Regras de conteúdo (obrigatórias)

- Fatos do produto só do site erppro.com.br. Nada inventado (preço, número de clientes, recurso que não existe).
- Não citar fontes nem colocar links para fora; o único link externo é o do erppro.com.br (mais o link interno para a capa).
- Não usar a palavra "grátis" no sentido de sistema grátis. O teste do ERPPro só é oferecido depois da demonstração.
- Nomes proibidos em qualquer texto: "Winpro" e "ChatPro". Não citar marcas de concorrentes.
- Plano Master não é multi-lojas (filiais só no Elite). CRM só no Master e Elite. O PDV a divulgar é o PDV2.
- O tema "estoque por grade" está na AWS até ~maio/2027 — não repetir aqui enquanto estiver lá.
- Uma página por tema; nada de páginas rasas ou repetidas só para link.

## Como publicar na Cloudflare (pelo Chrome)

1. Abra `https://dash.cloudflare.com/c2e97dc83482766e8062c5feaea4bb81/pages/view/erppro/deployments/new`.
2. Se pedir login: **pare**, não digite senha, e avise o Adriano que precisa entrar na Cloudflare. Publique na próxima rodada.
3. Deixe marcado **Produção**.
4. Envie o zip pela ferramenta de JavaScript da página: decodifique o conteúdo de `dist/site.zip.b64` em bytes, crie `new File([bytes], 'erppro-site.zip', {type: 'application/zip'})`, coloque no `input[type=file][accept=".zip"]` com `DataTransfer` e dispare os eventos `input` e `change`.
5. Confira na tela que **todos** os arquivos foram carregados, inclusive as subpastas de cada guia com o tamanho certo (pasta com 0 B = erro: clique em "Remover tudo", confirme, refaça o build e envie de novo). Só então clique em **Salvar e implantar**.
6. Feche a aba da Cloudflare ao terminar.

## Fila de temas

1. Como emitir NFC-e na loja: passo a passo do cupom fiscal eletrônico
2. Fechamento de caixa sem diferença: rotina diária do PDV
3. Venda condicional (malinha): como controlar sem perder peça
4. Catálogo digital para vender pelo WhatsApp
5. Cobrança pelo WhatsApp sem constranger o cliente
6. Controle de estoque para loja pequena: o básico que funciona
7. Inventário rotativo: contar o estoque sem fechar a loja
8. Etiqueta com código de barras: como organizar a loja
9. Como formar preço de venda: markup e margem na prática
10. Curva ABC de produtos: o que comprar e o que liquidar
11. Certificado digital A1 para emitir nota: como funciona
12. Reforma Tributária (IBS e CBS) explicada para o lojista
13. Entrada de mercadoria pelo XML da nota do fornecedor
14. Contas a pagar e a receber: organizando o financeiro da loja
15. Gestão de loja de autopeças: estoque, aplicação e balcão
16. Gestão de papelaria e material escolar na volta às aulas
17. Gestão de pet shop: produtos, serviços e recorrência
18. Gestão de agropecuária: estoque sazonal e venda a prazo
19. Gestão de loja de cosméticos: validade, lote e kits
20. Gestão de mercadinho: giro rápido e controle de perdas
21. Várias lojas: transferência de estoque entre filiais
22. Venda sob encomenda: como não perder o pedido
23. Relatórios que o dono da loja deve olhar toda semana
24. Como reduzir perdas e furtos no varejo
25. Atendimento pelo WhatsApp: organizar pedidos e orçamentos
