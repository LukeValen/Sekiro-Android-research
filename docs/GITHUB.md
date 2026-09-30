# Criar e publicar no GitHub

Nome sugerido: `sekiro-android-research`. Owner: `LukeValen`. Descrição: `Pesquisa de viabilidade de um port nativo ARM64 de Sekiro a partir da versão PC.`

Começar como **Private** é uma escolha conservadora enquanto a pesquisa ainda está sendo organizada; isso não altera o objetivo do projeto. Não adicionar README ou licença pela página, pois os arquivos iniciais já existem. Ainda não foi escolhida uma licença para as ferramentas originais.

## Pelo celular

1. Abrir https://github.com/new e criar o repositório vazio com o nome acima.
2. Baixar o ZIP inicial e extrair. No Termux, entrar na pasta extraída.
3. Inicializar e publicar:

```sh
git init -b main
git add README.md docs tools tests .gitignore
git commit -m 'Initialize Sekiro Android feasibility research'
git remote add origin https://github.com/LukeValen/sekiro-android-research.git
git push -u origin main
```

Git precisa de nome/email configurados e autenticação GitHub. Não inserir tokens em arquivos, URLs do remote ou mensagens de chat. Pode-se usar GitHub CLI e autenticação via navegador se já estiverem disponíveis no ambiente.

Se criar com README no GitHub, clone esse repositório primeiro, copie os arquivos para ele e faça commit/push; não use force push.

## O que falta

O repositório remoto não foi criado nesta preparação: a integração conectada permite operações em repositórios existentes, mas não disponibiliza criação de repositório. Depois de criar o remoto e liberar acesso à integração GitHub, os arquivos podem ser publicados por ela.
