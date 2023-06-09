import LDE
import LSE
import LSeq
import SQ
import SS
import ABP

import tkinter as tk

class InterfaceGrafica:
    def __init__(self, menu):
        self.menu = menu
        
        # Cria a janela principal
        self.root = tk.Tk()
        self.root.title("Visualização Gráfica das Estruturas de Dados")

        # Cria um label para "Visualização Gráfica das Estruturas de Dados"
        estrutura_label = tk.Label(self.root, text="Visualização Gráfica das Estruturas de Dados", font=("Arial", 15))
        estrutura_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Cria as opções com seus respectivos botões
        for i, opcao in enumerate(self.menu.opcoes):
            opcao_label = tk.Label(self.root, text=opcao)
            opcao_label.grid(row=i+1, column=0, padx=10, pady=10)
            opcao_button = tk.Button(self.root, text="Acessar", command=lambda op=opcao: self.menu.selecionar_opcao(op))
            opcao_button.grid(row=i+1, column=1, padx=10, pady=10)

        # Inicia a janela principal
        self.root.mainloop()

class Menu:
    def __init__(self, opcoes):
        self.opcoes = opcoes

    def selecionar_opcao(self, opcao):
        if opcao == "Lista Sequencial":
            run = LSeq.LSeq() 
        elif opcao == "Lista Simplesmente Encadeada":
            run = LSE.LSE()
        elif opcao == "Lista Duplamente Encadeada":
            run = LDE.LDE()
        elif opcao == "Fila":
            run = SQ.SQ()
        elif opcao == "Pilha":
            run = SS.SS()
        elif opcao == "Árvore Binária de Pesquisa":
            run = ABP.ABP()

# Cria um objeto da classe Menu com as opções desejadas
menu = Menu(["Lista Sequencial", "Lista Simplesmente Encadeada", "Lista Duplamente Encadeada", "Fila", "Pilha", "Árvore Binária de Pesquisa"])

# Cria um objeto da classe InterfaceGrafica com o objeto menu como argumento
interface = InterfaceGrafica(menu)
