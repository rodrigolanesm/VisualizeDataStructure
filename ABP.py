# Implementação da interface para árvore binária de pesquisa

import tkinter as tk
import ArvImplem
import time

class InterfaceGrafica:
    def __init__(self, master):
        self.arvore_binaria_pesquisa = ArvImplem.ArvoreBinariaPesquisa()

        # definimos o título da janela
        master.title("Árvore Binária de Pesquisa")

        # exibimos um label para "Árvore Binária de Pesquisa"
        self.label = tk.Label(master, text="Árvore Binária de Pesquisa", font=("Arial", 15))
        self.label.pack(padx=20, pady=10)

        # cria um frame pai para todos os objetos seguintes
        self.frame_caixas = tk.Frame(master)
        self.frame_caixas.pack(side="top", pady=5, fill="both", expand=True)

        # cria um frame para inserir um label para "Digite um Valor"
        self.frame_label_valor = tk.Frame(self.frame_caixas)
        self.frame_label_valor.pack(side="top", padx=20, pady=5, anchor="center")
        # label de valor a ser digitado
        self.label_inserir_valor = tk.Label(self.frame_label_valor, text="Digite um Valor")
        self.label_inserir_valor.pack(side="left", padx=5, anchor="center")

        # cria um frame para inserir um label para caixa e botão para Inserir
        self.frame_inserir = tk.Frame(self.frame_caixas)
        self.frame_inserir.pack(side="top", padx=20, pady=5, anchor="center")
        # caixa de valor a ser inserido
        self.caixa_inserir_valor = tk.Entry(self.frame_inserir)
        self.caixa_inserir_valor.pack(side="left", padx=5)
        # botão para Inserir
        self.button_inserir = tk.Button(self.frame_inserir, text="  Inserir  ", command=self.inserir)
        self.button_inserir.pack(side="left", padx=5)
        # label para indicar que um erro ocorreu
        self.label_erro_inserir = tk.Label(self.frame_inserir, text="", fg="red")
        self.label_erro_inserir.pack(side="left", padx=5)

        # cria um frame para inserir um label para caixa e botão para Remover
        self.frame_remover = tk.Frame(self.frame_caixas)
        self.frame_remover.pack(side="top", padx=20, pady=5, anchor="center")
        # caixa de valor a ser removido
        self.caixa_remover = tk.Entry(self.frame_remover)
        self.caixa_remover.pack(side="left", padx=5)
        # botão para Remover
        self.button_remover = tk.Button(self.frame_remover, text="Remover" , command=self.remover)
        self.button_remover.pack(side="left", padx=5, anchor="center")
        # label para indicar que um erro ocorreu
        self.label_erro_remover = tk.Label(self.frame_remover, text="", fg="red")
        self.label_erro_remover.pack(side="left", padx=5, anchor="center")

        # cria um frame para inserir um label para caixa e botão para Buscar
        self.frame_buscar = tk.Frame(self.frame_caixas)
        self.frame_buscar.pack(side="top", padx=20, pady=5)
        # caixa de valor a ser buscado
        self.caixa_buscar = tk.Entry(self.frame_buscar)
        self.caixa_buscar.pack(side="left", padx=5)
        # botão para Buscar
        self.button_buscar = tk.Button(self.frame_buscar, text="  Buscar  ", command=self.buscar)   
        self.button_buscar.pack(side="left", padx=5)
        self.label_erro_buscar = tk.Label(self.frame_buscar, text="", fg="red")
        # label para indicar que um erro ocorreu
        self.label_erro_buscar.pack(side="left", padx=5, anchor="center")

        # cria um frame para inserir os  botões para "Pre-Ordem", "In-Ordem" e "Pos-Ordem"
        self.frame_botoes = tk.Frame(self.frame_caixas)
        self.frame_botoes.pack(side="bottom", padx=20, pady=5, anchor="center")
        # botão para Buscar
        self.button_pre_ordem = tk.Button(self.frame_botoes, text="Pré-ordem", command=self.pre_ordem)
        self.button_pre_ordem.pack(side="left", padx=20)
        self.button_in_ordem = tk.Button(self.frame_botoes, text=" In-ordem " , command=self.in_ordem)
        self.button_in_ordem.pack(side="left", padx=20)
        self.button_pos_ordem = tk.Button(self.frame_botoes, text="Pós-ordem" , command=self.pos_ordem)
        self.button_pos_ordem.pack(side="left", padx=20)

        # cria um frame para exibir label para "Representação da Árvore"
        self.frame_label_apre_arvore = tk.Frame(self.frame_caixas)
        self.frame_label_apre_arvore.pack(side="top", padx=20, pady=5, anchor="center")
        # label para "Representação da Árvore"
        self.label_arvore = tk.Label(self.frame_label_apre_arvore, text="Representação da Árvore     ")
        self.label_arvore.pack(side="top", padx=5, anchor="center")

        #canvas para exibição da árvore
        self.frame_canvas_arvore = tk.Frame(self.frame_caixas)
        self.frame_canvas_arvore.pack(pady=20)
        self.canvas_arvore = tk.Canvas(self.frame_canvas_arvore, width=1080, height=300, bg='white', scrollregion=(0, 0, 2160, 720))
        self.canvas_arvore.pack(side="left", fill="both", expand=True)
        self.vbar_arvore = tk.Scrollbar(self.frame_canvas_arvore, orient="vertical", command=self.canvas_arvore.yview)
        self.vbar_arvore.pack(side="right", fill="y")
        self.canvas_arvore.configure(yscrollcommand=self.vbar_arvore.set)
        self.hbar_arvore = tk.Scrollbar(self.frame_caixas, orient="horizontal", command=self.canvas_arvore.xview)
        self.hbar_arvore.pack(side="top", fill="x")
        self.canvas_arvore.configure(xscrollcommand=self.hbar_arvore.set)

        # Canvas para exibir lista com elementos em lista da árvores Pre-Ordem, In-Ordem e Pos-Ordem
        self.frame_canvas_lista = tk.Frame(self.frame_caixas)
        self.frame_canvas_lista.pack(side="top", anchor="center", pady=20)
        self.canvas_lista = tk.Canvas(self.frame_canvas_lista, width=500, height=100, bg='white', scrollregion=(0, 0, 3000, 0))
        self.canvas_lista.pack(side="left", anchor="center")
        self.hbar_lista=tk.Scrollbar(self.frame_caixas,orient="horizontal")
        self.hbar_lista.pack(side="bottom",fill="x")
        self.hbar_lista.config(command=self.canvas_lista.xview)
        self.vbar_lista = tk.Scrollbar(self.frame_canvas_lista, orient="vertical")
        self.vbar_lista.pack(side="right", fill="y")
        self.vbar_lista.config(command=self.canvas_lista.yview)
        self.canvas_lista.config(yscrollcommand=self.vbar_lista.set)
        self.canvas_lista.config(xscrollcommand=self.hbar_lista.set)

    def inserir(self):
        valor = self.caixa_inserir_valor.get()
        if valor.isdigit():
            self.arvore_binaria_pesquisa.inserir(int(valor))
            self.label_erro_inserir.config(text="")
            self.desenhar()
        else:
            self.label_erro_inserir.config(text="ERROR")

    def remover(self):
        valor = self.caixa_remover.get()
        if valor.isdigit():
            self.arvore_binaria_pesquisa.remover(int(valor))
            self.label_erro_remover.config(text="")
            self.canvas_arvore.delete("all")

            self.desenhar()
        else:
            self.label_erro_remover.config(text="ERROR")

    def desenhar(self, no=None, x=1080, y=30 , deslocX = 300, deslocY = 50):
        tam = 30
        espaco = 2
        altura = self.arvore_binaria_pesquisa.altura()
        
        if (no==None): 
            no = self.arvore_binaria_pesquisa.raiz
            valor = no.valor
            circulo = self.canvas_arvore.create_oval(x - (tam/2), y- (tam/2), x+ (tam/2), y+ (tam/2), width = 2)
            self.canvas_arvore.create_text(x, y, text=valor)

        if no.esquerda is not None:
            valor = no.esquerda.valor
            #utilizar a altura para criar círculos de modo que não haja sobreposição de círculos
            self.canvas_arvore.create_oval(x-deslocX - (tam/2), y+deslocY- (tam/2), x-deslocX+ (tam/2), y+deslocY+ (tam/2), width = 2)
            self.canvas_arvore.create_line(x-15, y+15, x-deslocX+15, y+deslocY-15, arrow="last")
            self.canvas_arvore.create_text(x-deslocX, y+deslocY, text=valor)
            self.desenhar(no.esquerda, x-deslocX, y+deslocY, deslocX/1.9)

        if no.direita is not None:
            valor = no.direita.valor
            self.canvas_arvore.create_oval(x+deslocX - (tam/2), y+deslocY- (tam/2), x+deslocX+ (tam/2), y+deslocY+ (tam/2), width = 2)
            self.canvas_arvore.create_line(x+15, y+15, x+deslocX-15, y+deslocY-15, arrow="last")
            self.canvas_arvore.create_text(x+deslocX, y+deslocY, text=valor)
            self.desenhar(no.direita, x+deslocX, y+deslocY, deslocX/1.9)
    
    def buscar(self,  no=None, x=1080, y=30 , deslocX = 300, deslocY = 50):
        self.desenhar()
        circulo_esquerda = None
        circulo_direita = None
        tam = 30
        buscando = int(self.caixa_buscar.get())
        
        if no is None: 
            no = self.arvore_binaria_pesquisa.raiz
        
        if no.valor == buscando:
            circulo = self.canvas_arvore.create_oval(x - (tam/2), y- (tam/2), x+ (tam/2), y+ (tam/2), width = 2, fill="green")
            self.canvas_arvore.create_text(x, y, text=no.valor)
            self.canvas_arvore.after(3000, lambda: self.canvas_arvore.delete(circulo))
            return
        
        if no.esquerda is not None:
            if no.esquerda.valor == buscando:
                if circulo_esquerda is None:
                    circulo_esquerda = self.canvas_arvore.create_oval(x-deslocX - (tam/2), y+deslocY- (tam/2), x-deslocX+ (tam/2), y+deslocY+ (tam/2), width = 2, fill="green")
                    self.canvas_arvore.create_line(x-15, y+15, x-deslocX+15, y+deslocY-15, arrow="last")
                    self.canvas_arvore.create_text(x-deslocX, y+deslocY, text=no.esquerda.valor)
                    self.canvas_arvore.after(3000, lambda: self.canvas_arvore.delete(circulo_esquerda))
                return
            self.buscar(no.esquerda, x-deslocX, y+deslocY, deslocX/1.9)
        if no.direita is not None:
            if no.direita.valor == buscando:
                if circulo_direita is None:
                    circulo_direita = self.canvas_arvore.create_oval(x+deslocX - (tam/2), y+deslocY- (tam/2), x+deslocX+ (tam/2), y+deslocY+ (tam/2), width = 2, fill="green")
                    self.canvas_arvore.create_line(x+15, y+15, x+deslocX-15, y+deslocY-15, arrow="last")
                    self.canvas_arvore.create_text(x+deslocX, y+deslocY, text=no.direita.valor)
                    self.canvas_arvore.after(3000, lambda: self.canvas_arvore.delete(circulo_direita))
                return
            self.buscar(no.direita, x+deslocX, y+deslocY, deslocX/1.9)

    def atualizar_lista_ordem(self):
        # Limpando o canvas e redesenhando as caixas e linhas
        self.canvas_lista.delete("all")

        x, y = 160, 35
        lista_ordem = self.arvore_binaria_pesquisa.retorna_lista()

        for i, valor in enumerate(lista_ordem):
            # Desenhando a caixa
            caixa = self.canvas_lista.create_rectangle(x, y, x+50, y+30, fill="white", outline="black")
            self.canvas_lista.create_text(x+25, y+15, text=valor)
            x+= 60

    def pre_ordem(self):
        self.arvore_binaria_pesquisa.pre_ordem()
        self.atualizar_lista_ordem()

    def in_ordem(self):
        self.arvore_binaria_pesquisa.in_ordem()
        self.atualizar_lista_ordem()
        
    def pos_ordem(self):
        self.arvore_binaria_pesquisa.pos_ordem()
        self.atualizar_lista_ordem()

def ABP():        
    root = tk.Tk()
    root.geometry("600x780")
    app = InterfaceGrafica(root)
    root.mainloop()