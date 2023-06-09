# temos uma linha corretamente apresentada

from tkinter import *

# definimos a classe do nó
class Node:
    # a classe é inicializada
    def __init__(self, valor):
        self.valor = valor      # o conteúdo do nó
        self.proximo = None     # aponta para o próximo nó
        self.anterior = None    # aponta para o nó anterior

# definimos a classe da lista duplamente encadeada
class ListaDuplamenteEncadeada:
    # a classe é inicializada
    def __init__(self):
        self.inicio = None      # primeiro nó
        self.fim = None         # último nó

    # método que retorna True se a lista estiver vazia; False, caso contrário
    def vazia(self):
        if (self.obter_tamanho() == 0):
            return True
        else:
            return False

    # método para inserir novos elementos; recebe como parâmetros o valor do novo elemento e sua posição na lista
    def inserir(self, valor, posicao):
        novo_no = Node(valor)

        # tratamento de erro para não aceitar posição nula ou negativa
        if posicao <= 0:
            return False
        
        # se inserimos o elemento na primeira posição
        if posicao == 1:
            # o novo nó tem como próximo nó o nó do início; nos certificamos de que o nó anterior do novo nó aponta para None
            novo_no.proximo = self.inicio
            novo_no.anterior = None

            # lista está vazia e inserimos o primeiro elemento da lista no fim
            if(self.vazia()):
                self.fim = novo_no
            else: # caso contrário: lista não vazia; nó do início tem como nó anterior o novo nó inserido
                self.inicio.anterior = novo_no
            
            # o novo nó é o nó do início
            self.inicio = novo_no
            return True
        else: # se inserimos elemento no meio ou fim da lista
            # percorremos os nós da lista e auxiliar recebe o nó anterior ao da posição indicada pelo usuário 
            auxiliar = self.inicio
            for i in range(posicao - 2):
                if auxiliar is None:
                    return False
                auxiliar = auxiliar.proximo

            # se o nó da posição indicada estiver vazio, retorna False
            if auxiliar is None:
                return False

            # o novo nó tem como nó anterior o auxiliar; o próximo nó é o próximo do auxiliar
            novo_no.anterior = auxiliar
            novo_no.proximo = auxiliar.proximo

            if auxiliar.proximo is not None:
                # o nó seguinte ao auxiliar agora tem como nó anterior o novo nó criado
                auxiliar.proximo.anterior = novo_no

            # por fim, o nó auxiliar tem como próximo nó o novo nó
            auxiliar.proximo = novo_no

            return True

    # método para remover elementos; recebe como parâmetro a posição na lista do elemento a ser removido
    def remover_por_posicao(self, posicao):
        # não é possível remover elementos quando a lista está vazia
        if self.vazia() == True:
            return False
        # não é possível remover elemento em posição nula ou negativa; só acessamos elementos nas posições 1, 2, 3, etc;
        if posicao <= 0:
            return False
        # se removemos o primeiro elemento da lista
        if posicao == 1:
            # o nó do início passa a ser o segundo nó (ou seja, o nó próximo ao início)
            self.inicio = self.inicio.proximo
            if self.inicio is not None:
                # o nó anterior ao início é None (não aponta para nenhum nó)
                self.inicio.anterior = None
            return True
        else: # se removemos um elemento no meio ou fim da lista
            # percorremos os nós da lista do começo até o nó da (posição indicada - 1)
            no_anterior = self.inicio
            for i in range(posicao - 2):
                if no_anterior is None:
                    return False
                no_anterior = no_anterior.proximo

            # se o nó da (posição indicada - 1) não é vazio e se seu próximo nó não é vazio
            if no_anterior is not None and no_anterior.proximo is not None:
                # fazemos as devidas alterações nos nós próximo e anterior para os quais no_anterior.proximo aponta
                no_anterior.proximo = no_anterior.proximo.proximo
                if no_anterior.proximo is not None:
                    no_anterior.proximo.anterior = no_anterior
                else:
                    self.fim = no_anterior
                return True
            else:
                return False
        
    def remover_por_valor(self, valor):
        no_anterior = None

        # percorremos os nós da lista do começo até o nó da (posição indicada - 1)
        no_atual = self.inicio
        while no_atual is not None:
            # valor_atual recebe o conteúdo do nó em que estamos na iteração atual
            valor_atual = int(no_atual.valor)
            # encontramos o valor que desejamos remover da lista
            if valor_atual == valor:
                # no_anterior is None significa que o nó atual é o início da lista
                if no_anterior is None:
                    self.inicio = no_atual.proximo
                    if no_atual.proximo is not None:
                        no_atual.proximo.anterior = None
                else: # Caso o valor a ser removido esteja em algum nó do meio ou fim da lista
                    no_anterior.proximo = no_atual.proximo
                    if no_atual.proximo is not None:
                        no_atual.proximo.anterior = no_anterior
                return True
            
            # nas iterações, temos o nó da iteração atual e o nó anterior ao atual
            no_anterior = no_atual
            no_atual = no_atual.proximo
        
        return False

    # método para consultar elementos; recebe como parâmetro o valor do elemento a ser consultado
    def consulta_por_valor(self, valor):
        no_atual = self.inicio
        posicao = 1
        while no_atual is not None:
            if no_atual.valor == valor:
                return posicao
            no_atual = no_atual.proximo
            posicao += 1
        return None

    # método para consultar elementos; recebe como parâmetro a posição do elemento a ser consultado
    def consulta_por_posicao(self, posicao):
        if posicao < 1:
            return None

        no_atual = self.inicio
        for i in range(posicao - 1):
            if no_atual is None:
                return None
            no_atual = no_atual.proximo

        if no_atual is None:
            return None

        return no_atual.valor

    # método que retorna a quantidade de elementos da lista
    def obter_tamanho(self):
        tamanho = 0
        no_atual = self.inicio
        while no_atual is not None:
            tamanho += 1
            no_atual = no_atual.proximo
        return tamanho

    # método que retorna todos os valores de uma lista
    def obter_valores(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        return valores

class InterfaceGrafica:
    def __init__(self, master):
        self.lista_duplamente_encadeada = ListaDuplamenteEncadeada()

        master.title("Lista Duplamente Encadeada")

        self.label = Label(master, text="Lista Duplamente Encadeada", font=("Arial", 15))
        self.label.pack(padx=20, pady=20)

        self.frame_caixas = Frame(master)
        self.frame_caixas.pack(side=TOP, pady=10)

        self.label_inserir_valor = Label(self.frame_caixas, text="Valor")
        self.label_inserir_valor.grid(row=0, column=0, padx=5)
        self.caixa_inserir_valor = Entry(self.frame_caixas)
        self.caixa_inserir_valor.grid(row=0, column=1)
        self.label_inserir_posicao = Label(self.frame_caixas, text="Posição")
        self.label_inserir_posicao.grid(row=1, column=0, padx=5)
        self.caixa_inserir_posicao = Entry(self.frame_caixas)
        self.caixa_inserir_posicao.grid(row=1, column=1)
        self.button_inserir = Button(self.frame_caixas, text="Inserir", command=self.inserir)
        self.button_inserir.grid(row=0, column=2, rowspan=2, padx=15)
        self.label_erro_inserir = Label(self.frame_caixas, text="", fg="red")
        self.label_erro_inserir.grid(row=0, column=3, rowspan=2)

        self.label_remover_posicao = Label(master, text="Posição")
        self.label_remover_posicao.pack()
        self.caixa_remover_posicao = Entry(master)
        self.caixa_remover_posicao.pack()
        self.button_remover = Button(master, text="Remover", command=self.remover_por_posicao)
        self.button_remover.pack(pady=10)
        self.label_erro_remover_posicao = Label(master, text="", fg="red")
        self.label_erro_remover_posicao.pack()
        
        self.label_remover_valor = Label(master, text="Valor a ser removido")
        self.label_remover_valor.pack()
        self.caixa_remover_valor = Entry(master)
        self.caixa_remover_valor.pack()
        self.button_remover_valor = Button(master, text="Remover", command=self.remover_por_valor)
        self.button_remover_valor.pack(pady=10)
        self.label_erro_remover_valor = Label(master, text="", fg="red")
        self.label_erro_remover_valor.pack()

        self.label_consulta_valor = Label(master, text="Consultar por Valor")
        self.label_consulta_valor.pack()
        self.caixa_consulta_valor = Entry(master)
        self.caixa_consulta_valor.pack()
        self.button_consulta = Button(master, text="Consultar", command=self.consulta_por_valor)
        self.button_consulta.pack(pady=10)
        self.label_resultado_consulta = Label(master, text="", fg="green")
        self.label_resultado_consulta.pack()

        self.label_consulta_posicao = Label(master, text="Consultar por Posição")
        self.label_consulta_posicao.pack()
        self.caixa_consulta_posicao = Entry(master)
        self.caixa_consulta_posicao.pack()
        self.button_consulta_posicao = Button(master, text="Consultar", command=self.consulta_por_posicao)
        self.button_consulta_posicao.pack(pady=10)
        self.label_resultado_consulta_posicao = Label(master, text="", fg="green")
        self.label_resultado_consulta_posicao.pack()

        self.label_tamanho = Label(master, text="Tamanho")
        self.label_tamanho.pack()
        self.label_valor_tamanho = Label(master, text="")
        self.label_valor_tamanho.pack()

        self.frame_lista = Frame(master)
        self.frame_lista.pack(pady = 10)

        i = self.lista_duplamente_encadeada.obter_tamanho()
        while i:
            print( self.lista_duplamente_encadeada.consulta_por_posicao(i) )
            i -= 1
        
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
        valor = self.caixa_inserir_valor.get()
        posicao = int(self.caixa_inserir_posicao.get())
        if self.lista_duplamente_encadeada.inserir(valor, posicao):
            self.label_erro_inserir.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            self.label_erro_inserir.config(text="ERROR")

    def remover_por_posicao(self):
        posicao = int(self.caixa_remover_posicao.get())
        if self.lista_duplamente_encadeada.remover_por_posicao(posicao):
            self.label_erro_remover_posicao.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            self.label_erro_remover_posicao.config(text="ERROR")
    
    def remover_por_valor(self):
        valor = int(self.caixa_remover_valor.get())
        if self.lista_duplamente_encadeada.remover_por_valor(valor):
            self.label_erro_remover_valor.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            self.label_erro_remover_valor.config(text="ERROR")

    def consulta_por_valor(self):
        valor = self.caixa_consulta_valor.get()
        posicoes = self.lista_duplamente_encadeada.consulta_por_valor(valor)
        if posicoes is not None:
            self.label_resultado_consulta.config(text="Valor encontrado na(s) posição(ões): {}".format(posicoes))
        else:
            self.label_resultado_consulta.config(text="Valor não encontrado")

    def consulta_por_posicao(self):
        posicao = int(self.caixa_consulta_posicao.get())
        valor = self.lista_duplamente_encadeada.consulta_por_posicao(posicao)
        if valor is not None:
            self.label_resultado_consulta_posicao.config(text="Valor na posição {}: {}".format(posicao, valor))
        else:
            self.label_resultado_consulta_posicao.config(text="Posição inválida")

    def desenhar_caixas(self):
        # Limpando o canvas e redesenhando as caixas e linhas
        self.canvas.delete("all")

        x, y = 50, 10
        valores = self.lista_duplamente_encadeada.obter_valores()

        if self.lista_duplamente_encadeada.obter_tamanho() != 0:
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
            if i < self.lista_duplamente_encadeada.obter_tamanho()-1:
                x2, y2 = x+50, y+10
                x3, y3 = x+100, y+10
                self.canvas.create_line(x2, y2, x3, y3, arrow="last", fill="blue")
                self.canvas.create_line(x2, y2+10, x3, y3+10, arrow="first", fill="red")

            x += 100
            if i is self.lista_duplamente_encadeada.obter_tamanho()-1:
                caixa = self.canvas.create_rectangle(x-50, y, x, y+30, fill="white", outline="black")
                self.canvas.create_text(x-25, y+15, text="Cauda")

    """
    def atualizar_lista(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        valores = self.lista_duplamente_encadeada.obter_valores()
        x, y = 50, 50
        for i, valor in enumerate(valores):
            label_valor = Label(self.frame_lista, text=valor, relief=SUNKEN, padx=10, pady=5)
            label_valor.pack(side=LEFT, padx=5)

            if i < len(valores) - 1:
                self.adicionar_seta_direita()

    def atualizar_listbox(self):
        self.listbox = Listbox(self.frame_lista, width=40)
        for i in range(self.lista_duplamente_encadeada.obter_tamanho()):
            self.listbox.insert(END, "Posição {}: {}".format(i, self.lista_duplamente_encadeada.consulta_por_posicao(i)))
        self.listbox.pack(side=LEFT, padx=5)

    def adicionar_seta_direita(self):
        linha = Canvas(self.frame_lista, width=10, height=5, highlightthickness=0)
        linha.create_line(0, 0, 30, 0, arrow=LAST)
        linha.pack(side=LEFT)
    """

def LDE():
    root = Tk()
    root.geometry("500x750")
    app = InterfaceGrafica(root)
    root.mainloop()