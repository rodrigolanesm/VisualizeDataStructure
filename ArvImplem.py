# Implementação da árvore binária de pesquisa

ROOT = "root"

# definimos a classe nó
class No:
    def __init__(self, valor):
        self.valor = valor      # conteúdo do nó
        self.esquerda = None    # aponta para o nó da esquerda
        self.direita = None     # aponta para o nó da direita

# definimos a classe Árvore Binária de Pesquisa
class ArvoreBinariaPesquisa:
    def __init__(self):
        self.raiz = None        # indica nó raiz da árvore; a partir dele, buscamos os outros nós
        self.lista_ordem = []   # a árvore guarda uma lista para pre-ordem, in-ordem e pos-ordem

    # verificamos se a árvore está vazia; retorna True se a árvore está vazia; False, caso contrário
    def arvoreVazia(self):
        if(self.raiz == None):
            return True
        else:
            return False

    # inserimos um novo elemento na árvore; retorna True se inserção tiver sido feita com sucesso; False, caso contrário
    def inserir(self, valor):
        novo_no = No(valor)

        # se a árvore está vazia, o novo nó é a raiz
        if self.arvoreVazia():
            self.raiz = novo_no
            return True
        
        # buscamos na árvore a posição adequada para inserção do novo nó
        auxiliar = self.raiz
        posicao = None

        # verificamos se o valor do novo elemento já existe na árvore
        while(auxiliar != None):
            posicao = auxiliar

            # se existe, a inserção não acontece
            if(valor == auxiliar.valor):
                return False
            
            # comparamos os valores para saber se seguimos para a direita ou esquerda nos ramos da árvore
            if(valor < auxiliar.valor):
                auxiliar = auxiliar.esquerda
            else:
                auxiliar = auxiliar.direita

        # entramos nesse if se o valor não existe e o inserimos
        if(valor < posicao.valor):
            posicao.esquerda = novo_no
        else:
            posicao.direita = novo_no

        return True

    # buscamos por um elemento na árvore; retorna o nó em que foi encontrado o valor de busca; False, caso contrário
    def buscar(self, no_busca, valor):

        # verificamos se o nó atual aponta para None
        if(no_busca == None):
            return None
        
        # verificamos se o elemento foi encontrado no nó atual
        if(valor == no_busca.valor):
            return no_busca
        
        # verificamos os nós à direita e esquerda com recursividade até encontrar o nó, se ele existir
        if(valor < no_busca.valor):
            return self.buscar(no_busca.esquerda, valor)
        else:
            return self.buscar(no_busca.direita, valor)
        
    # buscamos na árvore o nó de menor valor
    def menor_valor(self, no=ROOT):
        
        if no == ROOT:
            no = self.raiz

        while no.esquerda != None:
            no = no.esquerda
        return no.valor

    # buscamos na árvore o nó de maior valor
    def maior_valor(self, no=ROOT):

        if no == ROOT:
            no = self.raiz

        while no.direita != None:
            no = no.direita
        return no.valor

    # removemos um elemento da ávore
    def remover(self, valor, no_remover=ROOT):

        # se a árvore está vazia, retorna False
        if self.arvoreVazia() == True:
            return False

        no_pai = None
        if no_remover == ROOT:
            no_remover = self.raiz

        # buscamos e salvamos o nó a ser removido e seu nó pai
        while True:
            if valor < no_remover.valor:
                no_pai = no_remover
                no_remover = no_remover.esquerda
            elif valor > no_remover.valor:
                no_pai = no_remover
                no_remover = no_remover.direita
            elif valor == no_remover.valor: # valor é encontrado
                break
            elif no_remover == None: # valor não é encontrado na ávore; remover retorna False
                return False

        # se o nó a ser removido não tem filhos
        if no_remover.esquerda == None and no_remover.direita == None:            
            if no_pai is None: # se o nó a ser removido é raiz
                self.raiz = None
            elif no_pai.esquerda == no_remover: # nó a ser removido é o nó à esquerda do pai
                no_pai.esquerda = None # nó à esquerda do pai aponta para None 
            elif no_pai.direita == no_remover: # nó a ser removido é o nó à direita do pai
                no_pai.direita = None # nó à direita do pai aponta para None 
        # se o nó a ser removido tem um filho à direita
        elif no_remover.esquerda == None: 
            if no_pai == None:
                self.raiz = no_remover.direita
            elif no_pai.esquerda == no_remover:
                no_pai.esquerda = no_remover.direita
            elif no_pai.direita == no_remover:
                no_pai.direita = no_remover.direita
        # se o nó a ser removido tem um filho à esquerda
        elif no_remover.direita == None: 
            if no_pai == None:
                self.raiz = no_remover.esquerda
            elif no_pai.esquerda == no_remover:
                no_pai.esquerda = no_remover.esquerda
            elif no_pai.direita == no_remover:
                no_pai.direita = no_remover.esquerda
        # se o nó a ser removido tem filhos à esquerda e à direita
        else:
            # buscamos o substituto do nó a ser removido na subarvore direita
            substituto_pai = no_remover
            substituto = no_remover.direita
            # buscamos o substituto
            while substituto.esquerda is not None:
                substituto_pai = substituto
                substituto = substituto.esquerda
            # verifica se o nó pai do substituto é diferente do nó a ser removido
            if substituto_pai != no_remover:
                substituto_pai.esquerda = substituto.direita
            # o nó pai do sucessor é o nó a ser removido
            else:
                substituto_pai.direita = substituto.direita
            no_remover.valor = substituto.valor
        return no_remover

    # quando executamos pre_ordem, pos_ordem e in_ordem, o resultado é salvo em lista_ordem da árvore
    # salva o conteúdo de uma árvore em pré-ordem
    def pre_ordem(self):
        self.lista_ordem = resultado = []
        self._pre_ordem_(self.raiz, resultado)
    
    # auxilia o método pre_ordem
    def _pre_ordem_(self, no, resultado):
        if no:
            resultado.append(no.valor)
            self._pre_ordem_(no.esquerda, resultado)
            self._pre_ordem_(no.direita, resultado)

    # salva o conteúdo de uma árvore em pos-ordem
    def pos_ordem(self):
        self.lista_ordem = resultado = []
        self._pos_ordem_(self.raiz, resultado)

    # auxilia o método pos_ordem
    def _pos_ordem_(self, no, resultado):
        if no:
            self._pos_ordem_(no.esquerda, resultado)
            self._pos_ordem_(no.direita, resultado)
            resultado.append(no.valor)

    # salva o conteúdo de uma árvore em in-ordem
    def in_ordem(self):
        self.lista_ordem = resultado = []
        self._in_ordem_(self.raiz, resultado)

    # auxilia o método in_ordem
    def _in_ordem_(self, no, resultado):
        if no:
            self._in_ordem_(no.esquerda, resultado)
            resultado.append(no.valor)
            self._in_ordem_(no.direita, resultado)

    def retorna_lista(self):
        return self.lista_ordem
    
    # retorna a altura da árvore
    def altura(self, no=ROOT):
        if no == ROOT:
            no = self.raiz

        if no == None:
            return -1
        else:
            return 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        
    
        