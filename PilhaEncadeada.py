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

class Pilha:
    
    def __init__(self):
        self.topo = None
    
    def setTopo(self, topo):
        self.topo = topo
        
    def push(self, valor):
        novoNo = No()
        novoNo.setValor(valor)
        novoNo.setProx(self.topo)
        self.setTopo(novoNo)
    
    def pop(self):
        if(Pilha.isEmpty(self)):
            print("Pilha esta vazia, impossivel remover dado!")
        else:
            self.setTopo(self.topo.getProx())

    def imprimir(self):
        noAux = self.topo
        impressao = True
        while(impressao == True):
            if(noAux.getProx() != None):
                print(noAux.getValor())
                noAux = noAux.getProx()
            else:
                print(noAux.getValor())
                print("")
                impressao = False

    def isFull(self):
        return False
    
    def isEmpty(self):
        if(self.topo == None):
            return True
        else:
            return False

p1 = Pilha()
p1.push(45)
p1.push(49)
p1.imprimir()
p1.pop()
p1.imprimir()
p1.push(499)
p1.imprimir()