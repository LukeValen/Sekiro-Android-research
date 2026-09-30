# Plano de investigação do port nativo

Cada fase termina em uma evidência verificável. Não pular diretamente para geração de APK.

| Fase | Trabalho | Critério de conclusão |
| --- | --- | --- |
| 0 — Identificação | Registrar hash, formato e versão da cópia de PC | Relatório local reproduzível do executável |
| 1 — Dependências | Imports, cargas dinâmicas, componentes de plataforma e gráficos | Lista separando itens observados, inferidos e desconhecidos |
| 2 — Análise piloto | Selecionar função pura pequena, estudar assembly/pseudocódigo e escrever implementação própria | Comparação documentada de entradas e saídas com referência |
| 3 — Dados | Selecionar formato simples e construir leitor/visualizador | Fixtures sintéticas no CI e arquivos reais somente localmente |
| 4 — Base Android | Criar host ARM64 para módulos originais com logging e entrada | Build Android que executa um módulo validado; ainda não é o jogo |
| 5 — Gráficos | Escolher estratégia após medir shaders, passes e dependências | Cena mínima reproduzida e comparada com referência |
| 6 — Sistemas | Avaliar animação, física, scripts, áudio, streaming e saves separadamente | Provas funcionais por sistema antes de integração |
| 7 — Integração | Integrar somente componentes cuja reconstrução foi validada | Cena jogável e testes de comportamento/desempenho |

## Próxima ação concreta

Executar `tools/inspect_pe.py` na cópia local. Sem esse arquivo, nenhum endereço, função ou dependência específica pode ser afirmado. Em seguida levantar imports com Ghidra/LLVM e decidir qual função pequena investigar primeiro.

## Registro de execução por compatibilidade, caso usado como referência

Anotar dispositivo, Android, runtime, tradutor de CPU, versão Wine, DXVK, driver, hash do executável, resolução, preset, logs, cenário e duração. Separar crash de CPU, falha de API, erro Vulkan, shader, entrada e falta de memória. Não usar apenas "abre/não abre" como evidência de viabilidade.
