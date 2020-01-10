class Fila:

    def __init__(self, tamanho):
        self.inicio = 0
        self.fim = 0
        self.tamanho = tamanho
        self.elementos = [None] * tamanho
        self.quantidade = 0

    def push(self, valor):
        if(Fila.isFull(self)):
            print("Fila ta cheia !!")
        else:
            self.elementos[self.fim] = valor
            self.fim += 1
            self.quantidade += 1
            if(self.fim == self.tamanho):
                self.fim = 0
    
    def pop(self):
        if(Fila.isEmpty(self)):
            print("Fila esta vazia, impossivel remover dado!")
        else:
            print("Removendo elemento do inicio.")
            self.elementos[self.inicio] = None
            self.inicio += 1
            self.quantidade -= 1
            if(self.inicio == self.tamanho):
                self.inicio = 0

    def imprimir(self):
        if(Fila.isEmpty(self)):
            print("Pilha esta vazia!!")
        else:
            saida = ''
            for i in self.elementos:
                saida += str(i)+" "
            print(saida)
        
    def isFull(self):
        if self.quantidade == self.tamanho:
            return True
        else:
            return False
    
    def isEmpty(self):
        if(self.quantidade == 0):
            return True
        else:
            return False

p1 = Fila(5)
p1.push(45)
p1.push(55)
p1.push(50)
p1.imprimir()
p1.pop()
p1.imprimir()
p1.push(60)
p1.push(12)
p1.push(17)
p1.imprimir()
p1.push(152)
p1.pop()
p1.pop()
p1.imprimir()
p1.push(45)
p1.push(55)
p1.imprimir()