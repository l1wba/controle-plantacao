# Controle de Plantacao

Aplicacao desktop em Python para registrar e acompanhar o plantio realizado em uma fazenda. A fazenda e representada por uma matriz de **7 x 7**, totalizando 49 areas de plantio.

O projeto foi desenvolvido com foco didatico no ensino de logica de programacao estruturada e procedural, utilizando `tkinter` e `tkinter.ttk` para a interface grafica.

## Funcionalidades

- Visualizacao da fazenda em uma matriz com 49 areas.
- Identificacao individual de cada area por linha e coluna.
- Selecao de culturas por menu de contexto:
  - Milho
  - Soja
  - Batata
  - Cenoura
  - Tomate
  - Feijao
- Alteracao de uma cultura ja plantada.
- Limpeza de uma area, retornando-a ao estado livre.
- Indicacao visual por cores para cada cultura.
- Contadores atualizados em tempo real.
- Relatorio final com:
  - quantidade de cada cultura;
  - total de areas plantadas;
  - total de areas livres;
  - percentual de ocupacao da fazenda.
- Reinicializacao de todas as areas com confirmacao.
- Interface com tema escuro e dimensionamento responsivo.

## Requisitos

- Python 3.10 ou superior.
- Tkinter, normalmente incluido na instalacao do Python para Windows.
- Sistema operacional Windows, Linux ou macOS com suporte ao Tkinter.

Nao sao necessarios pacotes externos.

## Como executar

Abra um terminal na pasta do projeto e execute:

```powershell
python controle_plantacao.py
```

No Windows, tambem e possivel utilizar o caminho completo do interpretador:

```powershell
& "C:/Users/seu-usuario/AppData/Local/Programs/Python/Python314/python.exe" "controle_plantacao.py"
```

## Como utilizar

1. Abra o programa.
2. Clique em uma area da matriz.
3. Escolha uma cultura no menu exibido.
4. A area sera marcada como plantada e recebera a cor correspondente.
5. Para substituir o cultivo, clique novamente na mesma area e selecione outra cultura.
6. Para liberar a area, clique nela e escolha **Limpar Area**.
7. Consulte os contadores laterais durante o preenchimento.
8. Clique em **Gerar Relatorio Final** para visualizar o resumo do plantio.
9. Use **Reiniciar Fazenda** para limpar todas as areas e iniciar um novo controle.

## Estrutura do projeto

```text
controle-plantacao/
|-- controle_plantacao.py   # Aplicacao principal
|-- README.md                # Documentacao do projeto
|-- Prompt Python.md         # Requisitos pedagogicos e regras da atividade
```

## Abordagem pedagogica

O programa segue o paradigma procedural puro:

- nao ha classes personalizadas;
- a logica e organizada em funcoes;
- o estado da fazenda e mantido em estruturas de dados globais;
- o fluxo evidencia sequencia, selecao e repeticao;
- os principais atalhos e metodos utilizados possuem comentarios explicativos no codigo.

A matriz utiliza listas bidimensionais para representar as areas. Cada posicao armazena o nome da cultura ou o valor `Livre`.

## Observacoes

- Os dados nao sao gravados em arquivo ou banco de dados.
- Ao fechar o programa, o controle atual e perdido.
- Cada nova execucao inicia com as 49 areas livres.
- O relatorio representa somente o estado registrado durante a execucao atual.

## Validacao

Para verificar a sintaxe do programa:

```powershell
python -m py_compile controle_plantacao.py
```

## Licenca

Este projeto foi criado para fins academicos e de estudo. Nenhuma licenca especifica foi definida.
