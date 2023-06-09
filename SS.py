from tkinter import *

#Classe que cria a pilha sequencial
class PilhaSequencial:
    #Inicializa a pilha
    def __init__(self):
        self.pilha = []
        #Define o tamanho máximo da pilha (12 no caso)
        self.tamanho_maximo = 12

    #Verifica se a pilha está cheia, retorna True se está e False se não
    def pilha_cheia(self):
        if len(self.pilha) == self.tamanho_maximo:
            return True
        else:
            return False
            
    #Verifica se a pilha está vazia, retorna True se está e False se não
    def pilha_vazia(self):
        if len(self.pilha) == 0:
            return True
        else:
            return False

    #Insere um novo elemento no topo da pilha, retorna True caso consiga e False caso não
    def inserir(self, valor):
        
        #Verifica se a pilha possui tamanho máximo e se está cheia
        if self.tamanho_maximo is not None and PilhaSequencial.pilha_cheia(self):
            return False
        else:
            #Adiciona o novo elemento no topo da pilha
            self.pilha.append(valor)
            return True

    #Remove o elemento no topo da pilha, retorna True caso consiga e False caso não
    def remover(self):
        tam = len(self.pilha)

        #Verifica se a pilha está vazia, retorna False se está
        if PilhaSequencial.pilha_vazia(self):
            return False
        else:
            self.pilha.pop(tam - 1)          
            return True
        
    #Consulta o elemento no topo da pilha, retorna o elemento se a pilha não estiver vazia
    #e None se estiver
    def consulta_topo(self):
        #Verifica se a pilha está vazia, retorna None se está
        if PilhaSequencial.pilha_vazia(self):
            return None
        else:
            tam = len(self.pilha)
            return self.pilha[tam - 1]

#Criação da interface gráfica em si
class InterfaceGrafica:
    #Inicialização da interface gráfica e de seus prompts(labels), botões e caixas de
    #inserção de valores(check box)
    def __init__(self, master):
        self.pilha_sequencial = PilhaSequencial()

        master.title("Pilha")

        self.label = Label(master, text="Pilha", font=("Arial", 15))
        self.label.pack(padx=20, pady=20)

        self.frame_caixas = Frame(master)
        self.frame_caixas.pack(side=TOP, pady=10)

        self.label_inserir_valor = Label(self.frame_caixas, text="Valor")
        self.label_inserir_valor.pack(side=LEFT, padx=5)
        self.caixa_inserir_valor = Entry(self.frame_caixas)
        self.caixa_inserir_valor.pack(side=LEFT)
        self.button_inserir = Button(self.frame_caixas, text="Inserir", command=self.inserir)
        self.button_inserir.pack(side=LEFT, padx=5)
        self.label_erro_inserir = Label(self.frame_caixas, text=" ", fg="red")
        self.label_erro_inserir.pack(side=LEFT)

        self.label_remover = Label(master, text="Remover topo")
        self.label_remover.pack()
        self.button_remover = Button(master, text="Remover", command=self.remover)
        self.button_remover.pack(pady=10)
        self.label_erro_remover = Label(master, text="", fg="red")
        self.label_erro_remover.pack()

        self.label_consulta_topo = Label(master, text="Consultar topo")
        self.label_consulta_topo.pack()
        self.button_consulta = Button(master, text="Consultar", command=self.consulta_topo)
        self.button_consulta.pack(pady=10)
        self.label_resultado_consulta = Label(master, text="", fg="green")
        self.label_resultado_consulta.pack()

        self.frame_pilha = Frame(master)
        self.frame_pilha.pack()

        self.atualizar_listbox()

    #Exibição do elemento inserido, erro caso não for bem sucedido
    def inserir(self):
        valor = self.caixa_inserir_valor.get()
        if self.pilha_sequencial.inserir(valor):
            self.label_erro_inserir.config(text="")
            self.atualizar_listbox()
        else:
            self.label_erro_inserir.config(text="ERROR!")

    #Remoção do topo da pilha, erro caso não for bem sucedido
    def remover(self):
        if self.pilha_sequencial.remover():
            self.label_erro_remover.config(text="")
            self.atualizar_listbox()
        else:
            self.label_erro_remover.config(text="ERROR!")

    #Exibição do valor no topo da pilha
    def consulta_topo(self):
        valor = self.pilha_sequencial.consulta_topo()
        if self.pilha_sequencial.consulta_topo():
            self.label_resultado_consulta.config(text=f"Valor encontrado: {valor}.", fg="green")
        else:
            self.label_resultado_consulta.config(text="Pilha vazia!.", fg="red")

    #Atualiza a tela
    def atualizar_listbox(self):
        for widget in self.frame_pilha.winfo_children():
            widget.destroy()

        for i in range(len(self.pilha_sequencial.pilha)):
            caixa = Label(self.frame_pilha, text=self.pilha_sequencial.pilha[i], width=5, borderwidth=1, relief="solid")
            caixa.pack(side=BOTTOM, padx=5)

def SS():
    root = Tk()
    root.geometry("400x400")
    interface = InterfaceGrafica(root)
    root.mainloop()