# Pesquisa técnica — 30/09/2026

## Resultado

A pesquisa pública realizada não identificou uma decompilação completa e recompilável de Sekiro nem um port nativo aberto para Android. Isso é um resultado limitado de busca, não prova de inexistência. Nenhum executável foi fornecido ou analisado; arquitetura, imports e middleware da cópia do usuário ainda precisam ser confirmados.

## Ferramentas e o que realmente entregam

| Ferramenta | Utilidade | Limite para este projeto |
| --- | --- | --- |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Disassembly, decompilação e investigação do executável | Não transforma automaticamente pseudocódigo em engine portátil |
| [UXM](https://github.com/JKAnderson/UXM) | Desempacotamento de arquivos e ajuste do carregamento de arquivos soltos em Sekiro | Não decompila a engine; não precisamos aplicar patches nesta fase |
| [SoulsFormats](https://github.com/JKAnderson/SoulsFormats) | Biblioteca .NET para ler/escrever formatos FromSoftware | Ler formatos não implementa renderização, gameplay ou animação |
| [DSLuaDecompiler](https://github.com/katalash/DSLuaDecompiler) | Decompilação Lua/HavokScript de IA e scripts de comportamento | Trabalha com scripts; não é uma decompilação do executável inteiro |
| [Box64](https://github.com/ptitSeb/box64) | Execução de programas Linux x86-64 em outras arquiteturas, com suporte a uso com Wine | Depende de integração com o ambiente; não gera código fonte do jogo |
| [FEX](https://github.com/FEX-Emu/FEX) | Emulação de aplicações x86/x86-64 em Linux ARM64 | Não é um APK de Sekiro nem solução Android pronta por si só |
| [DXVK](https://github.com/doitsujin/dxvk) | Tradução Direct3D 8/9/10/11 para Vulkan em conjunto com Wine | Exige driver Vulkan e recursos adequados; não substitui a tradução de CPU |

## Três caminhos diferentes

1. **Compatibilidade:** preservar o executável, traduzir instruções de CPU e APIs. É o caminho de menor escopo para tentar jogar, mas não atende sozinho ao objetivo nativo.
2. **Reconstrução nativa:** estudar funções e formatos, escrever implementações portáveis e validar resultados em módulos. É o objetivo investigado e tem escopo muito maior.
3. **Recompilação estática:** traduzir o binário para outra representação compilável. Ainda exige resolver chamadas indiretas, ABI, bibliotecas, sistema operacional e gráficos. Não foi encontrada uma ferramenta demonstrada que faça isso de ponta a ponta para Sekiro.

Essas conclusões são avaliação técnica a partir das capacidades documentadas das ferramentas, não resultados de um teste do jogo.

## Por que decompilar não basta

O executável não fornece automaticamente nomes, tipos, organização original, configurações de build e bibliotecas fonte. Otimização mistura ou remove abstrações. Além da lógica reconstruída, será necessário investigar convenções de chamada, layouts de objetos, ponteiros e callbacks, sincronização, SIMD, shaders, dependências e formatos.

Não presumir que a posse dos assets ou o funcionamento de um visualizador implica uma engine funcional. Não estimar FPS ou prazo sem provas de execução.

## Trabalhando pelo Android

O Termux é suficiente para começar com Git, Python, hashes e relatórios estáticos pequenos. A análise completa de um executável grande com Ghidra e a validação dinâmica serão mais práticas em um computador ou ambiente remoto adequado. Não foi verificado um fluxo completo de Ghidra para este jogo rodando somente no telefone. Builds Android poderão ser feitos por CI quando houver código nativo suficiente para compilar; adicionar um workflow agora não produziria o jogo.

## Evidências necessárias antes de escolher a arquitetura

- SHA-256 e edição/build exata do executável.
- Formato, arquitetura, seções, imports normais e imports atrasados.
- Bibliotecas e componentes efetivamente usados, incluindo cargas dinâmicas.
- Recursos gráficos observados em logs/capturas; requisitos publicados não bastam para isso.
- Dispositivo alvo, Android, RAM, GPU e driver Vulkan confirmado.
- Uma função pequena cujo comportamento possa ser comparado com uma implementação original.

As URLs acima foram consultadas como fontes primárias. Nenhuma das ferramentas foi incorporada, instalada ou testada com o jogo nesta fase.
