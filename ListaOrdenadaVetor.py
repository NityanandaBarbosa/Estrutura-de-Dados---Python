class Lista:

    def __init__(self, tamanho):
        self.elementos = [None]*tamanho
        self.quantidade = 0
        self.tamanho = tamanho
    
    def isFull(self):
        if(self.quantidade == self.tamanho):
            return True
        else:
            return False
    
    def isEmpty(self):
        if(self.quantidade == 0):
            return True
        else:
            return False
    
    def size(self):
        return self.quantidade
    
    def buscar(self, chave):
        for i in range(self.quantidade):
            if(self.elementos[i] == chave):
                return True
        return False

    def get(self, posicao):
        if(posicao < self.quantidade and posicao >= 0):
            return self.elementos[posicao]
        else:
            print("Posicao invalida!!")
            return None
    
    def inserir(self, valor):
        if(Lista.isFull(self)):
            print("Lista esta cheia !!")
        else:
            if(self.quantidade == 0):
                self.elementos[self.quantidade] = valor
            else:
                posiOrdem = 0 
                while(posiOrdem < self.quantidade):
                    if(self.elementos[posiOrdem] <= valor):
                        posiOrdem += 1
                    else:
                        break
                i = self.quantidade -1
                while(i >= posiOrdem):
                    self.elementos[i+1] = self.elementos[i]
                    i -= 1
                self.elementos[posiOrdem] = valor
        self.quantidade += 1

    def remover(self, posicao):
        if(Lista.isEmpty(self)):
            print("Lista esta vazia impossivel remover !!")
        else:
            if(posicao>=0 and posicao <= self.quantidade):
                while(posicao < self.quantidade):
                    self.elementos[posicao] = self.elementos[posicao + 1]
                    posicao += 1
                self.elementos[self.quantidade - 1] = None
                self.quantidade -= 1
            else:
                print("Posicao invalida")

    def imprimir(self):
        if(Lista.isEmpty(self)):
            print("Pilha esta vazia!!")
        else:
            saida = ''
            for i in self.elementos:
                saida += str(i)+" "
            print(saida)

p1 = Lista(5)
p1.inserir(45)
p1.imprimir()
p1.inserir(12)
p1.imprimir()
p1.inserir(1)
p1.imprimir()
p1.inserir(50)
p1.imprimir()
p1.inserir(30)
p1.imprimir()
print(p1.size())
