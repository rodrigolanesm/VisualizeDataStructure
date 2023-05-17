from tkinter import *

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor, posicao):
        # Cria um novo nó
        novo_no = Node(valor)
        
        # Verifica se os parâmetros de entrada são inteiros
        if not str(valor).isdigit() or not str(posicao).isdigit():
            return False
        
        if posicao < 1:
            return False
        elif posicao == 1:
            # Insere na cabeça
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            
            return True
        else:
            # Insere em uma posição específica
            no_anterior = self.cabeca
            for i in range(posicao - 2):
                if no_anterior is None:
                    return False
                no_anterior = no_anterior.proximo

            if no_anterior is None:
                return False

            novo_no.proximo = no_anterior.proximo
            no_anterior.proximo = novo_no
            return True

    def remover_por_posicao(self, posicao):
        if self.cabeca is None:
            return False
        if posicao == 1:
            # Remove o primeiro elemento da lista
            self.cabeca = self.cabeca.proximo
            return True

        no_anterior = self.cabeca
        for i in range(posicao - 2):
            if no_anterior is None:
                return False
            no_anterior = no_anterior.proximo

        if no_anterior is None or no_anterior.proximo is None:
            return False

        no_anterior.proximo = no_anterior.proximo.proximo
        return True
    
    def remover_por_valor(self, valor):
        # Inicia o no anterior como None e o no atual como a cabeça da lista
        no_anterior = None
        no_atual = self.cabeca

        while no_atual is not None:
            # Verifica se o valor do nó atual é igual ao valor que se quer remover
            valAtual = int(no_atual.valor)
            if valAtual == valor:
                if no_anterior is None:
                    # Caso o valor a ser removido esteja na cabeça
                    self.cabeca = no_atual.proximo
                else:
                    # Caso o valor a ser removido esteja em algum nó do meio ou fim da lista
                    no_anterior.proximo = no_atual.proximo
                return True
            no_anterior = no_atual
            no_atual = no_atual.proximo
        
        return False

    def consulta_por_valor(self, valor):
        # Inicia o no atual como a cabeça da lista e a posição como 1
        no_atual = self.cabeca
        posicao = 1
        while no_atual is not None:
            if no_atual.valor == valor:
                # Retorna a posição em que o valor foi encontrado
                return posicao
            no_atual = no_atual.proximo
            posicao += 1
        return None

    #Define o método "consulta_por_posicao" que recebe uma posição como argumento e retorna o valor do nó nessa posição
    def consulta_por_posicao(self, posicao):
        if posicao < 1:
            return None
        #Se a posição for inválida ou não houver nenhum nó na posição informada, retorna None
        no_atual = self.cabeca
        for i in range(posicao - 1):
            if no_atual is None:
                return None
            no_atual = no_atual.proximo

        if no_atual is None:
            return None

        return no_atual.valor

    # Define o método "tamanho" que retorna o tamanho atual da lista percorrendo todos os nós
    def tamanho(self):
        """Retorna o tamanho atual da lista."""
        tamanho = 0
        no_atual = self.cabeca
        while no_atual is not None:
            tamanho += 1
            no_atual = no_atual.proximo
        return tamanho

    # Define o método "obter_valores" que retorna todos os valores dos nós da lista em forma de lista
    def obter_valores(self):
        valores = []
        atual = self.cabeca
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        return valores
    

class InterfaceGrafica:
    def __init__(self, master):
        self.lista_simplesmente_encadeada = ListaSimplesmenteEncadeada()

        # Cria um título para a janela
        master.title("Lista Simplesmente Encadeada")

        # Cria um rótulo para exibir o título da lista
        self.label = Label(master, text="Lista Simplesmente Encadeada", font=("Arial", 15))
        self.label.pack(padx=20, pady=20)

        # Cria um frame para agrupar as caixas de entrada de valor e posição
        self.frame_caixas = Frame(master)
        self.frame_caixas.pack(side=TOP, pady=10)

        # Cria um rótulo e uma caixa de entrada para o valor a ser inserido
        self.label_inserir_valor = Label(self.frame_caixas, text="Valor")
        self.label_inserir_valor.grid(row=0, column=0, padx=5)
        self.caixa_inserir_valor = Entry(self.frame_caixas)
        self.caixa_inserir_valor.grid(row=0, column=1)

        # Cria um rótulo e uma caixa de entrada para a posição em que o valor será inserido
        self.label_inserir_posicao = Label(self.frame_caixas, text="Posição")
        self.label_inserir_posicao.grid(row=1, column=0, padx=5)
        self.caixa_inserir_posicao = Entry(self.frame_caixas)
        self.caixa_inserir_posicao.grid(row=1, column=1)

        # Cria um botão para inserir o valor na posição indicada e uma label para exibir erros
        self.button_inserir = Button(self.frame_caixas, text="Inserir", command=self.inserir)
        self.button_inserir.grid(row=0, column=2, rowspan=2, padx=5)
        self.label_erro_inserir = Label(self.frame_caixas, text="", fg="red")
        self.label_erro_inserir.grid(row=0, column=3, rowspan=2)

        # Cria um rótulo e uma caixa de entrada para a posição a ser removida
        self.label_remover_posicao = Label(master, text="Posição")
        self.label_remover_posicao.pack()
        self.caixa_remover_posicao = Entry(master)
        self.caixa_remover_posicao.pack()

        # Cria um botão para remover o valor na posição indicada e uma label para exibir erros
        self.button_remover = Button(master, text="Remover", command=self.remover_por_posicao)
        self.button_remover.pack(pady=10)
        self.label_erro_remover_posicao = Label(master, text="", fg="red")
        self.label_erro_remover_posicao.pack()

        # Cria um rótulo e uma caixa de entrada para o valor a ser removido
        self.label_remover_valor = Label(master, text="Valor a ser removido")
        self.label_remover_valor.pack()
        self.caixa_remover_valor = Entry(master)
        self.caixa_remover_valor.pack()
        
        #Cria o botão "Remover" e define o comando para remover um elemento da lista por valor
        self.button_remover_valor = Button(master, text="Remover", command=self.remover_por_valor)
        self.button_remover_valor.pack(pady=10)

        #Cria uma label para exibir erros na remoção de elementos da lista por valor
        self.label_erro_remover_valor = Label(master, text="", fg="red")
        self.label_erro_remover_valor.pack()
        
        #Cria um rótulo para indicar a seção de consulta por valor e uma caixa de entrada de texto para o valor a ser consultado
        self.label_consulta_valor = Label(master, text="Consultar por Valor")
        self.label_consulta_valor.pack()
        self.caixa_consulta_valor = Entry(master)
        self.caixa_consulta_valor.pack()

        #Cria o botão "Consultar" e define o comando para consultar a lista por valor
        self.button_consulta = Button(master, text="Consultar", command=self.consulta_por_valor)
        self.button_consulta.pack(pady=10)

        #Cria uma label para exibir o resultado da consulta por valor
        self.label_resultado_consulta = Label(master, text="", fg="green")
        self.label_resultado_consulta.pack()

        #Cria um rótulo para indicar a seção de consulta por posição e uma caixa de entrada de texto para a posição a ser consultada
        self.label_consulta_posicao = Label(master, text="Consultar por Posição")
        self.label_consulta_posicao.pack()
        self.caixa_consulta_posicao = Entry(master)
        self.caixa_consulta_posicao.pack()

        #Cria o botão "Consultar" e define o comando para consultar a lista por posição
        self.button_consulta_posicao = Button(master, text="Consultar", command=self.consulta_por_posicao)
        self.button_consulta_posicao.pack(pady=10)

        #Cria uma label para exibir o resultado da consulta por posição
        self.label_resultado_consulta_posicao = Label(master, text="", fg="green")
        self.label_resultado_consulta_posicao.pack()

        #Cria uma label para indicar a seção de exibição do tamanho da lista
        self.label_tamanho = Label(master, text="Tamanho")
        self.label_tamanho.pack()

        #Cria uma label para exibir o tamanho da lista
        self.label_valor_tamanho = Label(master, text="")
        self.label_valor_tamanho.pack()

        #Cria um frame para exibir a lista de elementos
        self.frame_lista = Frame(master)
        self.frame_lista.pack()

        # Criando o canvas para desenhar as caixas e linhas
        self.canvas = Canvas(master, bg="white", width=500, height=102, scrollregion=(0, 0, 5000, 0))
        self.canvas.pack(padx=10, pady=10)
        hbar=Scrollbar(self.canvas,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(self.canvas,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=300,height=300)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
        # Desenhando as caixas iniciais
        self.desenhar_caixas()

    def inserir(self):
        # Obter valor e posição da interface gráfica
        valor = self.caixa_inserir_valor.get()
        posicao = int(self.caixa_inserir_posicao.get())
        
        # Inserir valor na posição especificada na lista encadeada
        if self.lista_simplesmente_encadeada.inserir(valor, posicao):
            # Se a inserção foi bem-sucedida, atualizar a lista na interface gráfica
            self.label_erro_inserir.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            # Caso contrário, mostrar mensagem de erro na interface gráfica
            self.label_erro_inserir.config(text="ERROR")

    def remover_por_posicao(self):
        # Obter posição a ser removida da interface gráfica
        posicao = int(self.caixa_remover_posicao.get())
        
        # Remover valor na posição especificada na lista encadeada
        if self.lista_simplesmente_encadeada.remover_por_posicao(posicao):
            # Se a remoção foi bem-sucedida, atualizar a lista na interface gráfica
            self.label_erro_remover_posicao.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            # Caso contrário, mostrar mensagem de erro na interface gráfica
            self.label_erro_remover_posicao.config(text="Posição digitada não existe na lista")
    
    def remover_por_valor(self):
        # Obter valor a ser removido da interface gráfica
        valor = int(self.caixa_remover_valor.get())
        
        # Remover primeira ocorrência do valor na lista encadeada
        if self.lista_simplesmente_encadeada.remover_por_valor(valor):
            # Se a remoção foi bem-sucedida, atualizar a lista na interface gráfica
            self.label_erro_remover_valor.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            # Caso contrário, mostrar mensagem de erro na interface gráfica
            self.label_erro_remover_valor.config(text="Valor digitado não existe na lista")

    def consulta_por_valor(self):
        # Obtém o valor digitado pelo usuário
        valor = self.caixa_consulta_valor.get()
        # Chama o método "consulta_por_valor" da lista e armazena o resultado na variável "posicoes"
        posicoes = self.lista_simplesmente_encadeada.consulta_por_valor(valor)
        # Verifica se a lista retornou alguma posição e atualiza o label correspondente com o resultado
        if posicoes is not None:
            self.label_resultado_consulta.config(text="Valor encontrado na(s) posição(ões): {}".format(posicoes))
        else:
            self.label_resultado_consulta.config(text="Valor não encontrado")

    def consulta_por_posicao(self):
        # Obtém a posição digitada pelo usuário
        posicao = int(self.caixa_consulta_posicao.get())
        # Chama o método "consulta_por_posicao" da lista e armazena o resultado na variável "valor"
        valor = self.lista_simplesmente_encadeada.consulta_por_posicao(posicao)
        # Verifica se a lista retornou algum valor e atualiza o label correspondente com o resultado
        if valor is not None:
            self.label_resultado_consulta_posicao.config(text="Valor na posição {}: {}".format(posicao, valor))
        else:
            self.label_resultado_consulta_posicao.config(text="Posição inválida")

    def desenhar_caixas(self):
        # Limpando o canvas e redesenhando as caixas e linhas
        self.canvas.delete("all")

        x, y = 50, 10
        valores = self.lista_simplesmente_encadeada.obter_valores()

        if self.lista_simplesmente_encadeada.tamanho() != 0:
            caixa = self.canvas.create_rectangle(x, y, x+50, y+30, fill="white", outline="black")
            self.canvas.create_text(x+25, y+15, text="Cabeça")
            x2, y2 = x+50, y+10
            x3, y3 = x+100, y+10
            self.canvas.create_line(x2, y2, x3, y3, arrow="last")
            self.canvas.create_line(x2, y2+10, x3, y3+10, arrow="first")
            x += 50

        for i, valor in enumerate(valores):
            # Desenhando a caixa
            caixa = self.canvas.create_rectangle(x, y, x+50, y+30, fill="white", outline="black")
            self.canvas.create_text(x+25, y+15, text=valor)

            # Desenhando as linhas para a caixa seguinte, se houver
            if i < self.lista_simplesmente_encadeada.tamanho()-1:
                x2, y2 = x+50, y+15
                x3, y3 = x+100, y+15
                self.canvas.create_line(x2, y2, x3, y3, arrow="last", fill="blue")

            x += 100
            if i is self.lista_simplesmente_encadeada.tamanho()-1:
                caixa = self.canvas.create_rectangle(x-50, y, x, y+30, fill="white", outline="black")
                self.canvas.create_text(x-25, y+15, text="Cauda")

    """
    def atualizar_lista(self):
        # Remove todos os widgets do frame da lista
        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        # Obtém os valores da lista e adiciona um label para cada um deles
        valores = self.lista_simplesmente_encadeada.obter_valores()

        #adicionada a label para indicar onde que é a cabeça da lista
        label_valor = Label(self.frame_lista, text='Cabeça', relief=SUNKEN, padx=10, pady=5)
        label_valor.pack(side=LEFT, padx=5)
        self.adicionar_seta_direita()

        for i, valor in enumerate(valores):
            label_valor = Label(self.frame_lista, text=valor, relief=SUNKEN, padx=10, pady=5)
            label_valor.pack(side=LEFT, padx=5)

            if i < len(valores) - 1:
                self.adicionar_seta_direita()

            if i is len(valores)-1:
                self.adicionar_seta_direita()
                label_valor = Label(self.frame_lista, text='Null', relief=SUNKEN, padx=10, pady=5)
                label_valor.pack(side=LEFT, padx=5)

    def atualizar_listbox(self):
        
        # Cria uma nova lista para exibir na interface gráfica
        self.listbox = Listbox(self.frame_lista, width=40)
        
        # Itera sobre todas as posições da lista encadeada para inserir seus valores na lista criada anteriormente
        for i in range(self.lista_simplesmente_encadeada.tamanho()):
            self.listbox.insert(END, "Posição {}: {}".format(i, self.lista_simplesmente_encadeada.consulta_por_posicao(i)))
        
        # Adiciona a lista criada anteriormente ao frame_lista na interface gráfica
        self.listbox.pack(side=LEFT, padx=5)

    def adicionar_seta_direita(self):
        # Cria um label com a seta direita para separar visualmente cada elemento da lista
        seta_direita = Label(self.frame_lista, text="→")
        # Adiciona o label ao frame_lista na interface gráfica
        seta_direita.pack(side=LEFT)
    """

def LSE():
    root = Tk()
    root.geometry("500x750")
    app = InterfaceGrafica(root)
    root.mainloop()