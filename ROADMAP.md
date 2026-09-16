# Roadmap do Controle de Plantacao

Documento de acompanhamento do desenvolvimento do projeto. Esta pagina registra o que ja foi construido e serve como base para futuras atualizacoes.

## Status atual

**Versao:** 1.0.0 academica

**Situacao:** funcional para controle de plantio durante a execucao do programa.

## Historico do desenvolvimento

### 1. Definicao do escopo

- Definido o dominio de controle de plantacao em uma fazenda.
- Estabelecida uma matriz de 7 x 7, totalizando 49 areas.
- Definidas as culturas suportadas:
  - Milho;
  - Soja;
  - Batata;
  - Cenoura;
  - Tomate;
  - Feijao.
- Definidas as regras de negocio para plantar, substituir, limpar e contabilizar areas.

### 2. Implementacao da aplicacao

- Criado o arquivo `controle_plantacao.py`.
- Implementado o paradigma procedural puro, sem classes personalizadas.
- Criadas funcoes para:
  - inicializar a matriz;
  - aplicar um plantio;
  - limpar uma area;
  - contar ocorrencias por cultura;
  - calcular estatisticas;
  - atualizar os contadores em tempo real;
  - gerar o relatorio final;
  - reiniciar a fazenda.
- Implementada a matriz visual com 49 botoes.
- Adicionado menu de contexto para selecionar as culturas.
- Adicionada substituicao de culturas em areas ja plantadas.
- Adicionada limpeza individual de areas.

### 3. Interface grafica

- Utilizado `tkinter` e `tkinter.ttk`.
- Aplicado `ttk.Style` com tema escuro.
- Criado painel de contadores em tempo real.
- Adicionadas cores diferentes para cada cultura.
- Adicionada identificacao de linha e coluna em cada area.
- Criado relatorio final por meio de `messagebox`.
- Criada confirmacao antes da reinicializacao total.
- Ajustado o layout para reservar espaco para os botoes de relatorio e reinicializacao em janelas menores.
- Definidas dimensoes iniciais e dimensoes minimas para a janela.

### 4. Documentacao

- Criado `README.md` com:
  - apresentacao do projeto;
  - funcionalidades;
  - requisitos;
  - instrucoes de execucao;
  - guia de uso;
  - estrutura do projeto;
  - abordagem pedagogica;
  - limitacoes atuais.
- Criado este arquivo `ROADMAP.md` para acompanhar a evolucao do projeto.

### 5. Validacao realizada

- Validada a sintaxe de `controle_plantacao.py` com `py_compile`.
- Verificado que o arquivo Python nao apresenta erros no analisador do workspace.
- Aplicacao executada no ambiente Python local com sucesso.

## Arquitetura atual

```text
controle-plantacao/
|-- controle_plantacao.py   # Interface e regras de negocio
|-- README.md                # Documentacao para uso e apresentacao
|-- ROADMAP.md               # Historico e proximas etapas
|-- Prompt Python.md         # Requisitos originais da atividade
```

O estado atual da fazenda e mantido em memoria por meio de uma lista bidimensional. Nao existe persistencia em arquivo ou banco de dados.

## Proximas etapas

### Prioridade alta

- [ ] Adicionar persistencia dos plantios em arquivo JSON.
- [ ] Permitir salvar e carregar um controle de plantacao.
- [ ] Criar testes automatizados para as funcoes de contagem e estatisticas.
- [ ] Garantir que o layout continue utilizavel em resolucoes menores.

### Prioridade media

- [ ] Adicionar data e hora ao controle diario.
- [ ] Permitir iniciar um novo dia sem encerrar o programa.
- [ ] Exportar o relatorio para arquivo `.txt` ou `.csv`.
- [ ] Adicionar legenda visual das cores das culturas.
- [ ] Melhorar as mensagens de validacao e acessibilidade.

### Prioridade baixa

- [ ] Permitir configurar o tamanho da matriz.
- [ ] Adicionar uma tela de configuracao de culturas e cores.
- [ ] Criar historico de relatorios diarios.
- [ ] Adicionar graficos simples de distribuicao dos plantios.
- [ ] Preparar empacotamento como executavel para Windows.

## Decisoes e restricoes

- O projeto deve permanecer procedural para atender ao objetivo academico original.
- Nao devem ser introduzidas classes personalizadas sem uma revisao explicita do requisito pedagogico.
- A biblioteca grafica principal deve continuar sendo `tkinter`/`ttk`.
- Dependencias externas devem ser evitadas enquanto nao forem necessarias.
- Alteracoes futuras devem preservar os comentarios didaticos do codigo.

## Como atualizar este roadmap

Ao concluir uma etapa:

1. Mover o item correspondente de uma lista de pendencias para o historico.
2. Atualizar a versao ou o status atual quando houver uma entrega relevante.
3. Registrar novas decisoes arquiteturais ou restricoes.
4. Adicionar novas tarefas na secao de prioridade adequada.
5. Atualizar tambem o `README.md` quando o comportamento de uso mudar.
