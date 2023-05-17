from tkinter import *

#Classe que cria a lista sequencial
class ListaSequencial:
    #Inicializa a lista
    def __init__(self):
        self.lista = []
        #Define o tamanho máximo da lista (20 no caso)
        self.tamanho_maximo = 20
        for i in range(self.tamanho_maximo):
            self.lista.insert(i, "")

    #Verifica se a lista está cheia, retorna True se está e False se não
    def lista_cheia(self):
        tam = self.tamanho_maximo
        for i in range(self.tamanho_maximo):
            if i == self.tamanho_maximo - 1 and self.lista[tam - 1] != "":
                return True
            else:
                return False

    #Define um tamanho máximo para a lista
    def definir_tamanho_maximo(self, tamanho):
        self.tamanho_maximo = tamanho
        if len(self.lista) > tamanho:
            self.lista = self.lista[:tamanho]

    #Insere elementos novos na lista, retorna True caso consiga e False caso não
    def inserir(self, valor, posicao):
        tam = len(self.lista)
        #Verifica se a lista possui tamanho máximo e se está cheia
        if self.tamanho_maximo is not None and ListaSequencial.lista_cheia(self):
            return False
        else:
          #Verifica se o elemento anterior ao da posição especificada está vazio,
          #excluindo as posições 1 e 2 para a subtração do índice
          if posicao != 2 and posicao != 1 and self.lista[posicao - 2] == "":
              return False
          else:
            #Verifica se o elemento 1 está vazio para que seja possível
            #inserir na posição 2
            if posicao == 2 and self.lista[0] == "":
                return False
            else:
              #Verifica se o último elemento está vazio para ser inserido nessa posição
              if self.lista[self.tamanho_maximo - 1] != "":
                  return False
              else:
                #Move os elementos para a direita da posição especificada
                for i in range(tam - 1, posicao - 1, -1):
                    aux = self.lista[i - 1]
                    if self.lista[i] == "" and self.lista[i - 1] == "":
                        continue
                    else:
                        self.lista.pop(i)
                        self.lista.insert(i, aux)
                
                #Adiciona o novo elemento
                self.lista.pop(posicao - 1)
                self.lista.insert(posicao - 1, valor)

                return True

    #Remove elementos da lista, retorna True caso o elemento esteja na lista e False caso não
    def remover(self, posicao):
        tam = len(self.lista)

        #Verifica se a posição está dentro dos limites da lista
        if posicao > 0 and posicao <= tam:
            #Verifica se o elemento após a posição especificada está vazio (seria o último elem.)
            if self.lista[posicao] != "":
                del self.lista[posicao - 1]
                self.lista.insert(posicao - 1, "")

                for i in range(posicao - 1, tam - 1):
                    aux = self.lista[i + 1]
                    self.lista.pop(i)
                    self.lista.insert(i, aux)
                    self.lista.pop(i + 1)
                    self.lista.insert(i + 1, "")
            #Remoção do último elemento apenas
            else:
                self.lista.pop(posicao - 1)
                self.lista.insert(posicao - 1, "")

            return True
        else:
            return False
    
    #Consulta o elemento através do seu valor inserido, retorna a posiçao caso esteja na lista
    #ou -1 caso não
    def consulta_por_valor(self, valor):
        for i in range(len(self.lista)):
            if self.lista[i] == valor and valor != "":
                return i + 1  
        return -1  
    
    #Consulta o elemento pela posição especificada, retorna o valor caso a posiçao seja válida
    #ou None se for inválida
    def consulta_por_posicao(self, posicao):
        if posicao >= 0 and posicao < len(self.lista) and self.lista[posicao] != "":
            valor = self.lista[posicao]
            return valor
        else:
            return None

#Criação da interface gráfica em si
class InterfaceGrafica:
    #Inicialização da interface gráfica e de seus prompts(labels), botões e caixas de
    #inserção de valores(check box)
    def __init__(self, master):
        self.lista_sequencial = ListaSequencial()

        master.title("Lista Sequencial")

        self.label = Label(master, text="Lista Sequencial", font=("Arial", 15))
        self.label.pack(padx=20, pady=20)

        self.frame_caixas = Frame(master)
        self.frame_caixas.pack(side=TOP, pady=10)

        self.label_inserir_valor = Label(self.frame_caixas, text="Valor")
        self.label_inserir_valor.pack(side=LEFT, padx=5)
        self.caixa_inserir_valor = Entry(self.frame_caixas)
        self.caixa_inserir_valor.pack(side=LEFT)
        self.label_inserir_posicao = Label(self.frame_caixas, text="Posição")
        self.label_inserir_posicao.pack(side=LEFT)
        self.caixa_inserir_posicao = Entry(self.frame_caixas)
        self.caixa_inserir_posicao.pack(side=LEFT, padx=5)
        self.button_inserir = Button(self.frame_caixas, text="Inserir", command=self.inserir)
        self.button_inserir.pack(side=LEFT, padx=5)
        self.label_erro_inserir = Label(self.frame_caixas, text="", fg="red")
        self.label_erro_inserir.pack(side=LEFT)

        self.label_remover_posicao = Label(master, text="Posição")
        self.label_remover_posicao.pack()
        self.caixa_remover_posicao = Entry(master)
        self.caixa_remover_posicao.pack()
        self.button_remover = Button(master, text="Remover", command=self.remover)
        self.button_remover.pack(pady=10)
        self.label_erro_remover = Label(master, text="", fg="red")
        self.label_erro_remover.pack()

        self.label_consulta_valor = Label(master, text="Valor")
        self.label_consulta_valor.pack()
        self.caixa_consulta_valor = Entry(master)
        self.caixa_consulta_valor.pack()
        self.button_consulta = Button(master, text="Consultar", command=self.consulta_por_valor)
        self.button_consulta.pack(pady=10)
        self.label_resultado_consulta = Label(master, text="", fg="green")
        self.label_resultado_consulta.pack()

        self.label_consulta_posicao = Label(master, text="Posição")
        self.label_consulta_posicao.pack()
        self.caixa_consulta_posicao = Entry(master)
        self.caixa_consulta_posicao.pack()
        self.button_consulta_posicao = Button(master, text="Consultar por Posição", command=self.consulta_por_posicao)
        self.button_consulta_posicao.pack(pady=10) 
        self.label_resultado_consulta_posicao = Label(master, text="", fg="green")
        self.label_resultado_consulta_posicao.pack()

        self.frame_lista = Frame(master)
        self.frame_lista.pack()

        self.atualizar_listbox()

    #Exibição do elemento inserido, erro caso não for bem sucedido
    def inserir(self):
        valor = self.caixa_inserir_valor.get()
        posicao = int(self.caixa_inserir_posicao.get())
        if self.lista_sequencial.inserir(valor, posicao):
            self.label_erro_inserir.config(text="")
            self.atualizar_listbox()
        else:
            self.label_erro_inserir.config(text="ERROR")

    #Remoção visual do elemento na lista, erro caso não for bem sucedido
    def remover(self):
        posicao = int(self.caixa_remover_posicao.get())
        if self.lista_sequencial.remover(posicao):
            self.label_erro_remover.config(text="")
            self.atualizar_listbox()
        else:
            self.label_erro_remover.config(text="ERROR")

    #Exibição da posição do valor especificado na tela, erro caso não for bem sucedido
    def consulta_por_valor(self):
        valor = self.caixa_consulta_valor.get()
        posicao = self.lista_sequencial.consulta_por_valor(valor)
        if posicao != -1:
            self.label_resultado_consulta.config(text=f"Valor encontrado na posição {posicao} da lista.", fg="green")
        else:
            self.label_resultado_consulta.config(text="Valor não encontrado na lista.", fg="red")
    
    #Exibição do valor na posição especificada, erro caso não for bem sucedido
    def consulta_por_posicao(self):
        posicao = self.caixa_consulta_posicao.get()  
        if posicao.isdigit():
            posicao = int(posicao)
            valor = self.lista_sequencial.consulta_por_posicao(posicao-1)  
            if valor is not None:
                self.label_resultado_consulta_posicao.configure(text=f"Valor na posição {posicao} = {valor}", fg="green")
            else:
                self.label_resultado_consulta_posicao.configure(text="Posição inválida", fg="red")
        else:
            self.label_resultado_consulta_posicao.configure(text="Posição inválida", fg="red")

    #Atualiza a tela
    def atualizar_listbox(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        for i in range(len(self.lista_sequencial.lista)):
            caixa = Label(self.frame_lista, text=self.lista_sequencial.lista[i], width=4, height=2, borderwidth=2, relief="solid", padx=1)
            caixa.pack(side=LEFT, pady=15)

def LSeq():
    root = Tk()
    interface = InterfaceGrafica(root)
    root.mainloop()