class Pilha:

    def __init__(self, tamanho):
        self.topo = -1
        self.tamanho = tamanho
        self.elementos = ["None"] * tamanho

    def push(self, valor):
        if(Pilha.isFull(self)):
            print("Pilha ta cheia !!")
        else:
            self.topo += 1
            self.elementos[self.topo] = valor
    
    def pop(self):
        if(Pilha.isEmpty(self)):
            print("Pilha esta vazia, impossivel remover dado!")
        else:
            print("Removendo elemento do topo.")
            self.elementos[self.topo] = "None"
            self.topo += -1
            
    def imprimir(self):
        tam = self.topo
        for i in range(tam+1):
            print(self.elementos[tam])
            tam += -1

    def isFull(self):
        if self.topo == self.tamanho:
            return True
        else:
            return False
    
    def isEmpty(self):
        if(self.topo == -1):
            return True
        else:
            return False

p1 = Pilha(5)
p1.push(45)
p1.push(55)
p1.imprimir()
p1.pop()
p1.imprimir()
