# Memoria de trabalho do projeto

Este arquivo registra decisoes tecnicas e pedagogicas para que agentes de IA recuperem rapidamente o contexto antes de modificar o projeto.

## Identidade do projeto

- Projeto: Controle de Plantacao.
- Dominio: registro de culturas plantadas em uma fazenda.
- Aplicacao: desktop, executada localmente.
- Arquivo principal: `controle_plantacao.py`.
- Idioma da interface e da documentacao: portugues.
- Plataforma principal de desenvolvimento: Windows.
- Interpretador usado no ambiente atual: Python 3.14.

## Regras arquiteturais obrigatorias

1. Manter paradigma procedural puro.
2. Nao criar classes personalizadas nem usar a palavra-chave `class` no codigo da aplicacao.
3. Organizar a logica em funcoes procedurais.
4. Manter o estado da fazenda em estruturas globais simples, conforme o objetivo pedagogico original.
5. Usar `tkinter` e `tkinter.ttk` para a interface.
6. Evitar dependencias externas sem necessidade clara.
7. Preservar os comentarios didaticos que explicam algoritmos, atalhos e estruturas de controle.
8. Evidenciar no codigo as estruturas de Bohm-Jacopini: sequencia, selecao e repeticao.
9. Fazer alteracoes pequenas e focadas, sem reformatar trechos nao relacionados.

## Modelo de dados atual

- A fazenda possui uma matriz de 7 linhas por 7 colunas.
- Existem 49 areas de plantio.
- Cada posicao armazena o nome da cultura ou `Livre`.
- Culturas validas:
  - `Milho`
  - `Soja`
  - `Batata`
  - `Cenoura`
  - `Tomate`
  - `Feijao`
- Os dados existem apenas em memoria e sao perdidos ao fechar a aplicacao.
- A matriz visual de botoes acompanha a matriz logica para permitir atualizacoes imediatas.

## Comportamento implementado

- A aplicacao inicia com todas as areas livres.
- O clique em uma area abre um menu de contexto.
- O usuario pode plantar uma cultura em uma area livre.
- Uma cultura existente pode ser substituida por outra.
- Uma area plantada pode ser limpa e voltar ao estado `Livre`.
- O painel lateral atualiza os totais em tempo real.
- O relatorio final informa a quantidade por cultura, o total plantado e o total livre.
- A reinicializacao total pede confirmacao antes de limpar a matriz.

## Decisoes de interface

- A interface usa tema escuro.
- O tema `clam` do `ttk.Style` e usado por permitir personalizacao consistente das cores.
- Fundo principal: `#1E1E1E`.
- Paineis e botoes usam tons escuros com textos claros.
- As areas da matriz usam uma cor diferente para cada cultura.
- A janela inicia em `960x720` e possui tamanho minimo de `900x700`.
- O painel lateral possui largura minima para preservar os controles de relatorio e reinicializacao.
- A matriz ocupa a maior parte do espaco horizontal.
- Ao alterar o layout, verificar sempre a janela restaurada, e nao somente a tela cheia.

## Organizacao dos arquivos

```text
controle-plantacao/
|-- controle_plantacao.py   # Aplicacao, interface e regras de negocio
|-- README.md                # Documentacao publica para o GitHub
|-- ROADMAP.md               # Historico e proximas etapas
|-- MEMORY.md                # Memoria tecnica para agentes de IA
|-- Prompt Python.md         # Requisitos originais da atividade
```

## Validacao conhecida

Comando de verificacao de sintaxe:

```powershell
python -m py_compile controle_plantacao.py
```

No ambiente atual, tambem foi usado:

```powershell
& ".venv/Scripts/python.exe" -m py_compile "controle_plantacao.py"
```

Antes de finalizar uma alteracao Python:

1. Executar `py_compile`.
2. Consultar os diagnosticos do arquivo.
3. Iniciar a aplicacao quando a mudanca afetar a interface.
4. Verificar a janela em tamanho inicial, restaurado e maximizado.

## Limitacoes conhecidas

- Nao existe persistencia em JSON, CSV ou banco de dados.
- Nao ha historico entre execucoes.
- O relatorio e exibido em uma caixa de dialogo e nao e exportado.
- Nao existem testes automatizados para as regras de contagem.
- A interface depende do suporte local ao Tkinter.

## Proximos desenvolvimentos esperados

A ordem sugerida esta registrada em `ROADMAP.md`:

1. Adicionar persistencia em JSON.
2. Criar operacoes de salvar e carregar.
3. Criar testes automatizados para contagem e estatisticas.
4. Adicionar data e hora ao controle diario.
5. Exportar relatorios.
6. Melhorar acessibilidade e responsividade.

## Procedimento para futuros agentes

Antes de editar:

- Ler este arquivo e o `ROADMAP.md`.
- Conferir o estado atual do arquivo que sera alterado.
- Verificar se o usuario desfez alteracoes anteriores.
- Formular uma hipotese local sobre o comportamento e uma validacao objetiva.
- Respeitar a restricao de nao usar classes personalizadas.

Depois de editar:

- Executar a validacao mais especifica disponivel.
- Nao desfazer alteracoes do usuario.
- Atualizar este arquivo quando uma decisao arquitetural mudar.
- Atualizar o `ROADMAP.md` quando uma etapa relevante for concluida.
- Atualizar o `README.md` quando o uso da aplicacao mudar.
