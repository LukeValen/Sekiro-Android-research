# Sekiro Android Research

Pesquisa para avaliar um port nativo ARM64 de Sekiro usando a versão de PC como referência. Autor do projeto: LukeValen.

**Estado: investigação inicial. Não existe APK, engine reconstruída ou executável do jogo analisado neste repositório.**

## Objetivo e limites técnicos

Um decompilador permite estudar o executável, mas seu pseudocódigo não recupera automaticamente o projeto C++ original nem um projeto compilável para Android. Um port nativo exigiria reconstruir e validar a lógica e adaptar gráficos, plataforma, entrada, áudio, memória, threads, arquivos e dependências.

O objetivo permanece um port nativo. Wine com Box64/FEX e DXVK pode servir como referência de comportamento e desempenho, mas é execução por compatibilidade/tradução, não um port nativo.

## Primeiro passo no Termux

Use sua instalação de PC como entrada local. O analisador não executa nem modifica o jogo e usa apenas a biblioteca padrão do Python.

```sh
pkg install python git
termux-setup-storage
python tools/inspect_pe.py '/storage/emulated/0/Download/Sekiro/sekiro.exe' --output analysis-local/executable.json
```

O caminho é um exemplo: ajuste para sua pasta. O relatório contém SHA-256, formato PE, arquitetura e seções. Ele não contém funções decompiladas nem uma lista de dependências. Para o levantamento de imports, use posteriormente `llvm-readobj --coff-imports` com uma versão de LLVM disponível no seu ambiente ou a janela de imports do Ghidra.

Leia [a pesquisa](docs/RESEARCH.md), [o plano](docs/ROADMAP.md) e [como publicar](docs/GITHUB.md).

## Arquivos locais

Mantenha executáveis, DLLs, arquivos do jogo, saves, dumps, projetos Ghidra e resultados de decompilação fora dos commits. Este repositório contém documentação e ferramentas originais; o usuário fornece seus próprios arquivos localmente.

## Verificação das ferramentas

```sh
python -m unittest discover -s tests -v
```

Esses testes verificam o analisador com arquivos sintéticos. Não comprovam compatibilidade com Sekiro nem viabilidade do port.
