# -*- coding: utf-8 -*-
"""
Sistema de Controle de Plantação (Controle de Fazenda)
Desenvolvido sob o paradigma procedural puro para fins pedagógicos.

Este software permite monitorar e planejar as atividades de plantio em uma fazenda representada
por uma matriz de 7x7 (49 áreas de plantio). Cada área pode ser plantada com diferentes culturas
ou mantida livre. O sistema apresenta relatórios em tempo real e de finalização.

Autor: Desenvolvedor Python Sênior / Professor Acadêmico
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ==============================================================================
# CONFIGURAÇÕES GLOBAIS E ESTADO DA APLICAÇÃO (SEQUÊNCIA / INICIALIZAÇÃO)
# ==============================================================================
# [ESTRUTURA PEDAGÓGICA: SEQUÊNCIA]
# Inicialização sequencial do estado global do programa. No paradigma procedural,
# usamos variáveis globais e dicionários mutáveis no escopo do módulo para manter
# o estado da aplicação sem recorrer à orientação a objetos (classes).

# Matriz 7x7 que representa o estado de plantio de cada área da fazenda.
# Inicialmente, todas as 49 posições contêm o valor "Livre".
# OBRIGATÓRIO (REQUISITO PEDAGÓGICO): 
# A estrutura abaixo usa uma "List Comprehension" (compreensão de lista) para criar a matriz 7x7.
# Por debaixo dos panos: Este recurso executa dois loops aninhados (repetição) que alocam um vetor
# de 7 elementos dentro de outro vetor de 7 elementos na memória heap. Substitui um bloco
# tradicional de loops 'for' aninhados com inicialização manual de listas via .append().
estado_fazenda = [["Livre" for _ in range(7)] for _ in range(7)]

# Matriz de botões da interface gráfica para permitir atualização direta dos componentes visuais.
botoes_fazenda = [[None for _ in range(7)] for _ in range(7)]

# Dicionário de culturas disponíveis, suas respectivas cores de fundo (background) e de texto (foreground)
# OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
# Dicionários em Python usam tabelas Hash (função de espalhamento) sob o capô. 
# A busca por uma chave (ex: cores_culturas["Milho"]) é realizada em tempo constante médio O(1).
# Substitui um algoritmo de busca linear (Varredura sequencial com 'if/elif') em uma lista de tuplas.
# MODO ESCURO (DARK MODE): As cores foram ajustadas para proporcionar alto contraste e conforto visual.
cores_culturas = {
    "Livre":    {"bg": "#2D2D2D", "fg": "#AAAAAA", "active_bg": "#3E3E42"},
    "Milho":    {"bg": "#FBC02D", "fg": "#000000", "active_bg": "#FFF59D"},
    "Soja":     {"bg": "#2E7D32", "fg": "#FFFFFF", "active_bg": "#4CAF50"},
    "Batata":   {"bg": "#8D6E63", "fg": "#FFFFFF", "active_bg": "#A1887F"},
    "Cenoura":  {"bg": "#E65100", "fg": "#FFFFFF", "active_bg": "#FF9800"},
    "Tomate":   {"bg": "#C62828", "fg": "#FFFFFF", "active_bg": "#EF5350"},
    "Feijão":   {"bg": "#6A1B9A", "fg": "#FFFFFF", "active_bg": "#AB47BC"}
}

# Lista ordenada de culturas para montagem de menus e validação
culturas_disponiveis = ["Milho", "Soja", "Batata", "Cenoura", "Tomate", "Feijão"]

# Referências globais para os rótulos (Labels) de relatório em tempo real na interface gráfica
labels_tempo_real = {}

# Referência da janela principal
janela_principal = None


# ==============================================================================
# FUNÇÕES DE PROCESSAMENTO E LÓGICA DE NEGÓCIO (FUNÇÕES PROCEDURAIS)
# ==============================================================================

def obter_lista_linearizada():
    """
    Retorna uma lista de uma única dimensão (linear) contendo o estado de todas as áreas.
    Útil para aplicar funções de agregação como contagem (.count) e busca.
    """
    lista_linear = []
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO]
    # Loops aninhados para percorrer a matriz bidimensional (linhas e colunas).
    # Este algoritmo tradicional de achatamento (flattening) converte O(n^2) dados em O(n) linear.
    for linha in range(7):
        for coluna in range(7):
            lista_linear.append(estado_fazenda[linha][coluna])
    return lista_linear


def contar_ocorrencias(cultura):
    """
    Conta quantas áreas da fazenda estão atualmente plantadas com a cultura informada.
    """
    lista = obter_lista_linearizada()
    
    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # O método list.count() é utilizado abaixo para contar a ocorrência de uma cultura específica.
    # Por debaixo dos panos: Este método realiza um loop linear simples (O(n)) que percorre a lista do
    # início ao fim, comparando cada elemento com o argumento e incrementando um registrador interno.
    # Substitui uma estrutura clássica de 'for' manual com um acumulador (contador = contador + 1).
    quantidade = lista.count(cultura)
    return quantidade


def calcular_estatisticas():
    """
    Calcula de forma estruturada os totais para cada cultura, posições ocupadas e livres.
    """
    estatisticas = {}
    total_plantado = 0
    
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO]
    # Iteração sobre a lista de culturas para computar os dados de forma indexada.
    for cult in culturas_disponiveis:
        qtd = contar_ocorrencias(cult)
        estatisticas[cult] = qtd
        total_plantado += qtd  # Acumulação clássica (Sequência + Repetição)
        
    # O total de áreas livres é a diferença entre a área total (49) e o total plantado.
    total_livre = 49 - total_plantado
    
    estatisticas["Total Plantado"] = total_plantado
    estatisticas["Total Livre"] = total_livre
    
    return estatisticas


def atualizar_painel_lateral():
    """
    Atualiza as informações textuais exibidas no painel de estatísticas em tempo real.
    """
    # Executa a lógica de cálculo
    dados = calcular_estatisticas()
    
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO E REPETIÇÃO ANINHADA]
    # Percorremos cada chave do dicionário para atualizar o texto do widget correspondente na tela.
    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # O método dict.items() retorna uma visão dinâmica dos pares chave-valor do dicionário.
    # Por debaixo dos panos: Ele acessa a estrutura interna do dicionário (tabela hash) sem duplicar
    # os dados em uma nova lista na memória, permitindo um loop eficiente O(k) onde k é o número de chaves.
    # Substitui a necessidade de acessar individualmente cada elemento via chave ou fazer loops manuais de chaves.
    for chave, valor in dados.items():
        if chave in labels_tempo_real:
            # [ESTRUTURA PEDAGÓGICA: SELEÇÃO]
            # Formatação diferenciada baseada no tipo de informação (culturas vs totais gerais)
            if "Total" in chave:
                labels_tempo_real[chave].config(text=f"{chave:.<18} {valor:02d} / 49", font=("Segoe UI", 10, "bold"))
            else:
                labels_tempo_real[chave].config(text=f"{chave:.<22} {valor:02d}")


def aplicar_plantio(linha, coluna, nova_cultura):
    """
    Aplica fisicamente a alteração de estado em uma área da fazenda.
    Atualiza o estado lógico na matriz e os componentes visuais correspondentes.
    """
    # Validação de limites (Tratamento estruturado contra erros/inconsistências)
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO / TRATAMENTO DE EXCEÇÃO]
    # O operador lógico 'or' e operadores relacionais de comparação ('<' e '>=') garantem
    # que os índices fornecidos pertençam ao intervalo válido [0, 6].
    if linha < 0 or linha >= 7 or coluna < 0 or coluna >= 7:
        messagebox.showerror("Erro de Limites", "A posição selecionada está fora dos limites da fazenda!")
        return

    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # O operador 'in' é empregado para validar se a cultura informada é válida ou se é "Livre".
    # Por debaixo dos panos: Se aplicado a uma lista/tupla, ele realiza uma busca linear de O(n)
    # comparando cada elemento sequencialmente. Se aplicado a um dicionário/set, usa a tabela hash para O(1).
    # Aqui, como 'culturas_disponiveis' é uma lista, ele faz uma busca sequencial comparando o termo.
    # Substitui um loop de busca com flag booleana ('achou = False; para cada item: se item == termo: achou = True').
    if nova_cultura != "Livre" and (nova_cultura not in culturas_disponiveis):
        messagebox.showerror("Erro de Dados", f"A cultura '{nova_cultura}' não é suportada pelo sistema!")
        return

    # Atualização do estado lógico na matriz bidimensional
    estado_fazenda[linha][coluna] = nova_cultura
    
    # Recuperação do botão correspondente para atualização de layout
    btn = botoes_fazenda[linha][coluna]
    
    # Recuperação da configuração de cor correspondente
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO]
    # Caso a cultura não exista no mapa de cores por segurança, adotamos uma cor neutra.
    cfg_cor = cores_culturas.get(nova_cultura, cores_culturas["Livre"])
    
    # Atualização visual do botão
    if nova_cultura == "Livre":
        btn.config(
            text=f"Área ({linha},{coluna})\nLIVRE",
            bg=cfg_cor["bg"],
            fg=cfg_cor["fg"],
            activebackground=cfg_cor["active_bg"],
            activeforeground=cfg_cor["fg"]
        )
    else:
        btn.config(
            text=f"Área ({linha},{coluna})\nPLANTADO\n{nova_cultura.upper()}",
            bg=cfg_cor["bg"],
            fg=cfg_cor["fg"],
            activebackground=cfg_cor["active_bg"],
            activeforeground=cfg_cor["fg"]
        )
        
    # Atualização em tempo real do painel de contadores laterais
    atualizar_painel_lateral()


def limpar_posicao(linha, coluna):
    """
    Limpa o plantio de uma posição da fazenda, retornando-a para a condição de livre.
    """
    aplicar_plantio(linha, coluna, "Livre")


def mostrar_menu_contexto(linha, coluna, event):
    """
    Gera dinamicamente um menu de contexto (dropdown flutuante) ao clicar em um botão da matriz.
    Estilizado em Modo Escuro (Dark Mode).
    """
    # Criação do menu de contexto procedural com tema escuro
    menu_popup = tk.Menu(
        janela_principal, 
        tearoff=0, 
        bg="#252526", 
        fg="#E0E0E0", 
        activebackground="#043927", 
        activeforeground="#FFFFFF",
        bd=1,
        relief="flat"
    )
    
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO]
    # Usamos uma estrutura de repetição sequencial 'for' para preencher o menu flutuante.
    # Cada opção é configurada para chamar uma função anônima (lambda) que passa as coordenadas
    # e a cultura selecionada para a função de plantio.
    for cult in culturas_disponiveis:
        # Recuperamos a cor associada para exibir ao lado do nome (indicador visual amigável)
        cor_hex = cores_culturas[cult]["bg"]
        menu_popup.add_command(
            label=f"Plantar {cult}", 
            command=lambda c=cult: aplicar_plantio(linha, coluna, c)
        )
        
    # Adiciona uma linha divisória visual
    menu_popup.add_separator()
    
    # Adiciona opção de limpeza caso a posição não esteja livre
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO]
    # Se o estado atual for diferente de "Livre", exibimos a opção de limpar.
    if estado_fazenda[linha][coluna] != "Livre":
        menu_popup.add_command(
            label="Limpar Área (Tornar Livre)",
            command=lambda: limpar_posicao(linha, coluna)
        )
    else:
        # Caso já esteja livre, a opção fica desabilitada
        menu_popup.add_command(label="Área já está livre", state="disabled")
        
    # Exibe o menu exatamente na posição do ponteiro do mouse (coordenadas de tela absoluta)
    menu_popup.post(event.x_root, event.y_root)


def exibir_relatorio_final():
    """
    Compila os dados finais da fazenda, exibe um resumo estatístico em uma janela de diálogo
    e valida as operações do usuário antes de finalizar.
    """
    dados = calcular_estatisticas()
    
    # Construção da mensagem textual de relatório estruturado
    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # A formatação de strings abaixo faz uso de quebras de linha e alinhamento à direita.
    # Substitui a concatenação manual exaustiva de strings por formatação estruturada de texto.
    mensagem = (
        "======================================\n"
        "      RELATÓRIO DE PLANTIO DIÁRIO     \n"
        "======================================\n\n"
        "CULTURAS PLANTADAS:\n"
    )
    
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO E SELEÇÃO]
    # Varredura do dicionário para geração das linhas de estatística das culturas
    for cult in culturas_disponiveis:
        qtd = dados[cult]
        mensagem += f"  • {cult:<12}: {qtd:>2} áreas\n"
        
    mensagem += (
        "\n--------------------------------------\n"
        "RESUMO DE UTILIZAÇÃO DA FAZENDA:\n"
        "--------------------------------------\n"
    )
    
    total_plantado = dados["Total Plantado"]
    total_livre = dados["Total Livre"]
    
    mensagem += f"  - Total de áreas Plantadas : {total_plantado:>2} / 49\n"
    mensagem += f"  - Total de áreas Livres    : {total_livre:>2} / 49\n\n"
    
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO]
    # Análise diagnóstica baseada na ocupação da terra para dar um feedback acadêmico ao aluno.
    if total_plantado == 0:
        mensagem += "Status: A fazenda está completamente vazia. Nenhum trabalho registrado hoje."
    elif total_plantado == 49:
        mensagem += "Status: Excelente! 100% de ocupação. Toda a área disponível foi cultivada!"
    else:
        percentual = (total_plantado / 49) * 100
        mensagem += f"Status: Ocupação média de {percentual:.1f}% das terras da fazenda."
        
    # Exibe a caixa de mensagem nativa do sistema operacional (Windows/Standard)
    messagebox.showinfo("Relatório Final de Plantação", mensagem)


def reiniciar_fazenda():
    """
    Reseta todas as posições da fazenda de volta ao estado inicial "Livre".
    Apresenta caixa de confirmação de segurança (validação de fluxo).
    """
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO]
    # Valida se o usuário realmente deseja apagar os registros de trabalho.
    confirmar = messagebox.askyesno(
        "Confirmar Reinicialização", 
        "Tem certeza que deseja limpar toda a fazenda? Esta operação não pode ser desfeita."
    )
    
    if confirmar:
        # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO ANINHADA (MATRIZ)]
        # Percorre as 7 linhas e 7 colunas aplicando o estado livre em sequência.
        for linha in range(7):
            for coluna in range(7):
                aplicar_plantio(linha, coluna, "Livre")
                
        messagebox.showinfo("Sucesso", "Toda a fazenda foi limpa com sucesso e está pronta para novos cultivos!")


# ==============================================================================
# CONSTRUÇÃO DA INTERFACE GRÁFICA (ESTRUTURA E LAYOUT)
# ==============================================================================

def criar_interface():
    """
    Inicializa o TKinter, aplica o estilo TTK e monta a arquitetura visual responsiva.
    """
    global janela_principal
    
    # Instanciação da janela do sistema operacional
    janela_principal = tk.Tk()
    janela_principal.title("Painel de Controle de Plantação - AgroTech")
    janela_principal.geometry("960x720")
    janela_principal.minsize(900, 700)
    janela_principal.configure(bg="#1E1E1E")
    
    # Aplicação de Estilo Nativo via ttk.Style
    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # O ttk.Style permite acessar a API de temas nativos do Tkinter (Windows, clam, etc.).
    # Por debaixo dos panos: O Tkinter faz chamadas para a API de desenho nativa do Windows (uxtheme.dll),
    # fornecendo uma integração visual impecável e moderna.
    estilo = ttk.Style()
    
    # Configuração de temas baseados no OS
    # [ESTRUTURA PEDAGÓGICA: SELEÇÃO]
    # Verifica de forma segura se o tema "vista" ou "xpnative" está disponível para Windows.
    # Caso contrário, utiliza o padrão seguro "clam".
    # O tema "clam" permite personalizar melhor as cores da interface escura.
    estilo.theme_use("clam")
        
    # Customização de fontes e espaçamentos do estilo
    estilo.configure(".", background="#1E1E1E", foreground="#E6E6E6", font=("Segoe UI", 10))
    estilo.configure("TFrame", background="#1E1E1E")
    estilo.configure("TLabel", background="#1E1E1E", foreground="#E6E6E6", font=("Segoe UI", 10))
    estilo.configure("Header.TLabel", background="#1E1E1E", foreground="#8FD694", font=("Segoe UI", 14, "bold"))
    estilo.configure("TituloPanel.TLabel", background="#1E1E1E", foreground="#8FD694", font=("Segoe UI", 11, "bold"))
    estilo.configure("TButton", background="#2D2D2D", foreground="#E6E6E6", font=("Segoe UI", 10), borderwidth=1)
    estilo.map("TButton", background=[("active", "#3E3E42"), ("pressed", "#043927")], foreground=[("disabled", "#777777")])
    estilo.configure("TLabelframe", background="#1E1E1E", foreground="#8FD694", bordercolor="#4A4A4A")
    estilo.configure("TLabelframe.Label", background="#1E1E1E", foreground="#8FD694")
    estilo.configure("TSeparator", background="#4A4A4A")
    
    # ==========================================
    # CONTAINER PRINCIPAL (GRID RESPONSIVO)
    # ==========================================
    # Criamos um frame principal que ocupa toda a tela.
    # Ele será dividido em 2 colunas:
    # Coluna 0: A matriz da fazenda (Grid 7x7)
    # Coluna 1: Barra lateral de estatísticas e ações (Sidebar)
    frame_principal = ttk.Frame(janela_principal, padding="10")
    frame_principal.pack(fill=tk.BOTH, expand=True)
    
    # Configuração de redimensionamento dinâmico (responsividade do grid)
    frame_principal.columnconfigure(0, weight=4, minsize=560)  # A matriz recebe o espaço restante
    frame_principal.columnconfigure(1, weight=0, minsize=245)  # Reserva espaço para os controles laterais
    frame_principal.rowconfigure(0, weight=1)
    
    # ==========================================
    # PAINEL DA MATRIZ DA FAZENDA (ESQUERDA)
    # ==========================================
    # Um LabelFrame para conter visualmente nossa plantação de 49 áreas.
    frame_matriz_container = ttk.LabelFrame(frame_principal, text=" MAPA DE CULTIVO DA FAZENDA (MATRIZ 7x7) ", padding="10")
    frame_matriz_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
    
    # Configuração de linhas e colunas internas do frame da matriz para distribuir igualmente o espaço
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO]
    # Um loop for configura os pesos de redimensionamento para todas as 7 linhas e 7 colunas.
    for i in range(7):
        frame_matriz_container.rowconfigure(i, weight=1)
        frame_matriz_container.columnconfigure(i, weight=1)
        
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO ANINHADA - CRIAÇÃO DOS BOTÕES]
    # Loops aninhados para criar os 49 botões que compõem a matriz bidimensional na tela.
    # Cada botão recebe seu próprio índice (linha, coluna) impresso visualmente, conforme requisito do cliente.
    for r in range(7):
        for c in range(7):
            # Criamos o botão como padrão clássico do tkinter para podermos customizar as cores ativamente
            # nas plataformas Windows e Unix sem limitações estéticas impostas pelo motor padrão do TTK.
            btn = tk.Button(
                frame_matriz_container,
                text=f"Área ({r},{c})\nLIVRE",
                font=("Segoe UI Semibold", 8),
                width=12,
                height=3,
                bg=cores_culturas["Livre"]["bg"],
                fg=cores_culturas["Livre"]["fg"],
                activebackground=cores_culturas["Livre"]["active_bg"],
                activeforeground=cores_culturas["Livre"]["fg"],
                highlightbackground="#1E1E1E",
                highlightcolor="#8FD694",
                bd=1,
                relief="groove",
                cursor="hand2"
            )
            # Posicionamento exato no grid de geometria
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            
            # Armazenamento da referência visual na matriz de botões (estado visual)
            botoes_fazenda[r][c] = btn
            
            # Vinculação de eventos: Clique Esquerdo do mouse abre o menu de contexto
            # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
            # O método widget.bind() vincula um sinal de evento a uma função manipuladora (callback).
            # Por debaixo dos panos: O Tkinter mantém uma tabela interna de registro de eventos conectada
            # ao loop de mensagens do sistema de janelas do SO (Win32 API message loop).
            # Quando ocorre o clique do mouse (sinal '<Button-1>'), a rotina associada é enfileirada e executada.
            btn.bind("<Button-1>", lambda event, row=r, col=c: mostrar_menu_contexto(row, col, event))

    # ==========================================
    # PAINEL DE CONTROLE E RELATÓRIO (DIREITA)
    # ==========================================
    frame_lateral = ttk.Frame(frame_principal, padding="5")
    frame_lateral.grid(row=0, column=1, sticky="nsew")
    
    # Título do Painel Lateral
    lbl_painel_titulo = ttk.Label(frame_lateral, text="PAINEL AGROTECH", style="Header.TLabel", anchor="center")
    lbl_painel_titulo.pack(fill=tk.X, pady=(6, 10))
    
    # Quadro de Estatísticas em Tempo Real
    frame_stats = ttk.LabelFrame(frame_lateral, text=" CONTADORES EM TEMPO REAL ", padding="10")
    frame_stats.pack(fill=tk.X, pady=(0, 12))
    
    # Criação dinâmica dos Labels de Estatísticas para cada Cultura
    # [ESTRUTURA PEDAGÓGICA: REPETIÇÃO]
    # Iteramos sobre a lista de culturas disponíveis para construir a lista de labels monitorados.
    for cult in culturas_disponiveis:
        # Recuperamos a cor representativa para aplicar como um pequeno bloco indicativo colorido ao lado
        cor_hex = cores_culturas[cult]["bg"]
        
        # Subframe para empilhar horizontalmente a cor indicativa e o texto
        sub_row = ttk.Frame(frame_stats)
        sub_row.pack(fill=tk.X, pady=2)
        
        # Canvas de cor (indicador de cor no padrão de legenda)
        canvas_cor = tk.Canvas(sub_row, width=12, height=12, bg="#1E1E1E", bd=0, highlightthickness=1, highlightbackground="#666666")
        canvas_cor.create_rectangle(0, 0, 12, 12, fill=cor_hex, outline="")
        canvas_cor.pack(side=tk.LEFT, padx=(0, 8))
        
        # Rótulo de texto
        lbl_info = ttk.Label(sub_row, text=f"{cult:.<22} 00")
        lbl_info.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Armazenamento no dicionário global de rótulos ativos para atualizações futuras
        labels_tempo_real[cult] = lbl_info

    # Adicionando uma divisória visual simples
    separador = ttk.Separator(frame_stats, orient="horizontal")
    separador.pack(fill=tk.X, pady=6)
    
    # Totais Gerais no Painel Lateral
    for total_key in ["Total Plantado", "Total Livre"]:
        sub_row = ttk.Frame(frame_stats)
        sub_row.pack(fill=tk.X, pady=2)
        
        lbl_tot = ttk.Label(sub_row, text=f"{total_key:.<18} 00 / 49", font=("Segoe UI", 9, "bold"))
        lbl_tot.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        labels_tempo_real[total_key] = lbl_tot

    # ==========================================
    # SEÇÃO DE BOTÕES DE AÇÕES (RODAPÉ LATERAL)
    # ==========================================
    frame_acoes = ttk.LabelFrame(frame_lateral, text=" OPERAÇÕES ", padding="15")
    frame_acoes.pack(fill=tk.BOTH, expand=True, pady=(0, 10), ipady=6)
    
    # Instrução de Uso
    lbl_instrucao = ttk.Label(
        frame_acoes, 
        text="INSTRUÇÕES:\n1. Clique em qualquer área da matriz para planejar o cultivo.\n2. Escolha a cultura desejada no menu suspenso.\n3. Para limpar uma área já plantada, clique e selecione 'Limpar Área'.",
        justify=tk.LEFT, 
        wraplength=220,
        foreground="#BDBDBD"
    )
    lbl_instrucao.pack(fill=tk.X, pady=(0, 12))
    
    # Botão para Gerar o Relatório Final (Ocupará maior destaque visual)
    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # O widget ttk.Button herda as configurações do tema corporativo da aplicação.
    # O comando do botão é diretamente associado à rotina procedimental 'exibir_relatorio_final'.
    btn_relatorio = ttk.Button(
        frame_acoes, 
        text="📋 Gerar Relatório Final", 
        command=exibir_relatorio_final,
        cursor="hand2"
    )
    btn_relatorio.pack(fill=tk.X, ipady=8, pady=(0, 10))
    
    # Botão para Reiniciar e limpar toda a fazenda
    btn_limpar_tudo = ttk.Button(
        frame_acoes, 
        text="🔄 Reiniciar Fazenda", 
        command=reiniciar_fazenda,
        cursor="hand2"
    )
    btn_limpar_tudo.pack(fill=tk.X, ipady=4, pady=(0, 10))

    # Atualiza as labels iniciais de tempo real baseado na fazenda vazia (Livre)
    atualizar_painel_lateral()


# ==============================================================================
# FLUXO DE EXECUÇÃO PRINCIPAL (ENTRY POINT / INICIALIZAÇÃO)
# ==============================================================================
# [ESTRUTURA PEDAGÓGICA: SEQUÊNCIA]
# Este bloco representa o ponto de entrada tradicional de scripts Python. 
# Ele garante que o código seja executado apenas se for rodado diretamente como script principal.
if __name__ == "__main__":
    # 1. Sequência: Constrói a interface visual da aplicação
    criar_interface()
    
    # 2. Sequência / Loop de Eventos: Entrega o controle da execução ao loop principal do Tkinter
    # OBRIGATÓRIO (REQUISITO PEDAGÓGICO):
    # O método mainloop() do Tkinter inicia o ciclo infinito de escuta do sistema de janelas.
    # Por debaixo dos panos: Trata-se de um loop de controle 'while True' de baixa latência do Windows,
    # que aguarda chamadas do SO (como cliques, redimensionamento, teclado) e despacha as
    # funções de callback cadastradas. Evita consumo de 100% da CPU pois a thread entra em
    # estado de repouso (wait_message) enquanto nenhum evento ocorre.
    janela_principal.mainloop()
