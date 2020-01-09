class No:
    
    def __init__(self):
        self.valor = None
        self.prox = None
    
    def setValor(self,valor):
        self.valor = valor
    
    def getValor(self):
        return self.valor
    
    def setProx(self, prox):
        self.prox = prox
    
    def getProx(self):
        return self.prox

class Fila:
    
    def __init__(self):
        self.fim = None
        self.inicio = None
    
    def setInicio(self, inicio):
        self.inicio = inicio
    def setFim(self, fim):
        self.fim = fim
        
    def push(self, valor):
        novoNo = No()
        novoNo.setValor(valor)
        if(Fila.isEmpty(self)):
            self.setInicio(novoNo)
            self.setFim(novoNo)
        else:
            self.fim.setProx(novoNo)
            self.setFim(novoNo)
    
    def pop(self):
        if(Fila.isEmpty(self)):
            print("Pilha esta vazia, impossivel remover dado!")
        else:
            self.setInicio(self.inicio.getProx())

    def imprimir(self):
        noAux = self.inicio
        impressao = True
        saida = ''
        while(impressao == True):
            if(noAux.getProx() != None):
                saida += str(noAux.getValor()) + " "
                noAux = noAux.getProx()
            else:
                saida += str(noAux.getValor())
                impressao = False
                print(saida)
                print("")

    def isFull(self):
        return False
    
    def isEmpty(self):
        if(self.inicio == None):
            return True
        else:
            return False

p1 = Fila()
p1.push(45)
p1.push(55)
p1.push(49)
p1.imprimir()
p1.pop()
p1.imprimir()
p1.push(499)
p1.imprimir()