from tkinter import *

#Classe que cria a fila sequencial
class FilaSequencial:
    #Inicializa a fila
    def __init__(self):
        self.fila = []
        #Define o tamanho máximo da fila (12 no caso)
        self.tamanho_maximo = 12

    #Verifica se a fila está cheia, retorna True se está e False se não
    def fila_cheia(self):
        if len(self.fila) == self.tamanho_maximo:
            return True
        else:
            return False
            
    #Verifica se a fila está vazia, retorna True se está e False se não
    def fila_vazia(self):
        if len(self.fila) == 0:
            return True
        else:
            return False

    #Insere um novo elemento no final da fila, retorna True caso consiga e False caso não
    def inserir(self, valor):
        
        #Verifica se a fila possui tamanho máximo e se está cheia
        if self.tamanho_maximo is not None and FilaSequencial.fila_cheia(self):
            return False
        else:
            #Adiciona o novo elemento no final da fila
            self.fila.append(valor)
            return True

    #Remove o primeiro elemento da fila, retorna True caso consiga e False caso não
    def remover(self):

        #Verifica se a fila está vazia, retorna False se está
        if FilaSequencial.fila_vazia(self):
            return False
        else:
            self.fila.pop(0)          
            return True
        
    #Consulta o primeiro elemento da fila, retorna o elemento se a fila não estiver vazia
    #e None se estiver
    def consulta_primeiro(self):
        #Verifica se a fila está vazia, retorna None se estiver
        if FilaSequencial.fila_vazia(self):
            return None
        else:
            return self.fila[0]

#Criação da interface gráfica em si
class InterfaceGrafica:
    #Inicialização da interface gráfica e de seus prompts(labels), botões e caixas de
    #inserção de valores(check box)
    def __init__(self, master):
        self.fila_sequencial = FilaSequencial()

        master.title("Lista")

        self.label = Label(master, text="Lista", font=("Arial", 15))
        self.label.pack(padx=20, pady=20)

        self.frame_caixas = Frame(master)
        self.frame_caixas.pack(side=TOP, pady=10)

        self.label_inserir_valor = Label(self.frame_caixas, text="Valor")
        self.label_inserir_valor.pack(side=LEFT, padx=10, pady=20)
        self.caixa_inserir_valor = Entry(self.frame_caixas)
        self.caixa_inserir_valor.pack(side=LEFT)
        self.button_inserir = Button(self.frame_caixas, text="Inserir", command=self.inserir)
        self.button_inserir.pack(side=LEFT, padx=10)
        self.label_erro_inserir = Label(self.frame_caixas, text="", fg="red")
        self.label_erro_inserir.pack(side=LEFT)

        self.label_remover = Label(master, text="Remover 1º elemento da fila")
        self.label_remover.pack()
        self.button_remover = Button(master, text="Remover", command=self.remover)
        self.button_remover.pack(pady=10)
        self.label_erro_remover = Label(master, text="", fg="red")
        self.label_erro_remover.pack()

        self.label_consulta_primeiro = Label(master, text="Consultar 1º elemento da fila")
        self.label_consulta_primeiro.pack()
        self.button_consulta = Button(master, text="Consultar", command=self.consulta_primeiro)
        self.button_consulta.pack(pady=10)
        self.label_resultado_consulta = Label(master, text="", fg="green")
        self.label_resultado_consulta.pack()

        self.frame_fila = Frame(master)
        self.frame_fila.pack()

        self.atualizar_listbox()

    #Exibição do elemento inserido, erro caso não for bem sucedido
    def inserir(self):
        valor = self.caixa_inserir_valor.get()
        if self.fila_sequencial.inserir(valor):
            self.label_erro_inserir.config(text="")
            self.atualizar_listbox()
        else:
            self.label_erro_inserir.config(text="ERROR!")

    #Remoção do primeiro elemento da fila, erro caso não for bem sucedido
    def remover(self):
        if self.fila_sequencial.remover():
            self.label_erro_remover.config(text="")
            self.atualizar_listbox()
        else:
            self.label_erro_remover.config(text="ERROR!")
            

    #Exibição do primeiro elemento da fila
    def consulta_primeiro(self):
        valor = self.fila_sequencial.consulta_primeiro()
        if self.fila_sequencial.consulta_primeiro():
            self.label_resultado_consulta.config(text=f"Valor encontrado: {valor}.", fg="green")
        else:
            self.label_resultado_consulta.config(text="Fila vazia!", fg="red")

    #Atualiza a tela
    def atualizar_listbox(self):
        for widget in self.frame_fila.winfo_children():
            widget.destroy()

        for i in range(len(self.fila_sequencial.fila)):
            caixa = Label(self.frame_fila, text=self.fila_sequencial.fila[i], width=4, height=2, borderwidth=2, relief="solid", padx=5)
            caixa.pack(side=LEFT, padx=5, pady=10)

def SQ():
    root = Tk()
    root.geometry("400x400")
    interface = InterfaceGrafica(root)
    root.mainloop()