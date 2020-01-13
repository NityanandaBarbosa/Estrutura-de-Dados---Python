class No:
    
    def __init__(self):
        self.valor = None
        self.prox = None
        self.anterior = None
    
    def setValor(self,valor):
        self.valor = valor
    
    def getValor(self):
        return self.valor
    
    def setProx(self, prox):
        self.prox = prox
    
    def getProx(self):
        return self.prox
    
    def setAnterior(self, anterior):
        self.anterior = anterior

    def getAnterior(self):
        return self.anterior
        
class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0
    
    def isFull(self):
        return False
    
    def isEmpty(self):
        if(self.quantidade == 0):
            return True
        else:
            return False
    
    def size(self):
        return self.quantidade
    
    def buscar(self, chave):
        Aux = self.inicio
        for i in range(self.quantidade):
            if(Aux.getValor() == chave):
                return True
            else:
                Aux = Aux.getProx()
        return False

    def get(self, posicao):
        if(posicao < self.quantidade and posicao >=0):
            Aux = self.inicio
            if(posicao == 0):
                return self.inicio.getValor()
            else:
                for i in range(posicao - 1):
                    Aux = Aux.getProx()
            return Aux.getValor()
        else:
            print("Posicao invalida !")
            return None

    def inserir(self, valor):
        novoNo = No()
        novoNo.setValor(valor)
        if(Lista.isEmpty(self)):
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.setProx(novoNo)
            novoNo.setAnterior(self.fim)
            self.fim = novoNo
        self.quantidade += 1

    def inserirPosicao(self, posicao, valor):
        if(Lista.isEmpty(self)):
            print("Lista esta vazia !!")
        else:
            novoNo = No()
            novoNo.setValor(valor)
            if(posicao>=0 and posicao <= self.quantidade):
                aux = self.inicio
                anterior = None
                for i in range(posicao):
                    anterior = aux
                    aux = aux.getProx()
                novoNo.setProx(aux)
                if(aux == self.inicio):
                    aux.setAnterior(novoNo)
                    self.inicio = novoNo
                else:
                    anterior.setProx(novoNo)
                    novoNo.setAnterior(anterior)
                    if(posicao == self.quantidade):
                       self.fim = novoNo
                    else:
                        aux.setAnterior(novoNo)
                self.quantidade += 1
            else:
                print("Posicao invalida !!")

    def remover(self, posicao):
        anterior = self.inicio

        if(Lista.isEmpty(self)):
            print("Lista esta vazia impossivel remover !!")
        else:
            if(posicao>=0 and posicao < self.quantidade):
                if(posicao == 0):
                    self.inicio = self.inicio.getProx()
                else:
                    for i in range(posicao - 1):
                        anterior = anterior.getProx()
                    retorno = anterior.getProx()
                    aux = retorno.getProx()
                    anterior.setProx(aux)
                    if(posicao == self.quantidade):
                        self.fim = aux
                self.quantidade -= 1
            else:
                print("Posicao invalida")

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

    def imprimirInverso(self):
        noAux = self.fim        
        impressao = True
        saida = ''
        while(impressao == True):
            if(noAux.getAnterior() != None):
                saida += str(noAux.getValor()) + " "
                noAux = noAux.getAnterior()
            else:
                saida += str(noAux.getValor())
                impressao = False
                print(saida)
                print("")

p1 = Lista()
p1.inserir(45)
p1.inserir(12)
p1.imprimirInverso()
p1.inserirPosicao(0,25)
p1.imprimir()
p1.inserirPosicao(3,9)
p1.inserir(987)
p1.inserirPosicao(4,456)
p1.inserir(321)
p1.imprimir()
p1.imprimirInverso()
print(p1.size())