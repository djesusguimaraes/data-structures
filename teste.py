class No:
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, left, right):
        self.left = left
        self.right = right

    def balanco(self):
        prof_esq = 0
        if self.left:
            prof_esq = self.left.profundidade()
        prof_dir = 0
        if self.right:
            prof_dir = self.right.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.left:
            prof_esq = self.left.profundidade()
        prof_dir = 0
        if self.right:
            prof_dir = self.right.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        print('Rotacao Esquerda', self.data)

        self.data, self.right.data = self.right.data, self.data
        old_esquerda = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_esquerda, self.left.left)

    def rotacaoDireita(self):
        print('Rotacao Direita', self.data)

        self.data, self.left.data = self.left.data, self.data
        old_direita = self.right
        self.setaFilhos(self.left.left, self.left)
        self.right.setaFilhos(self.right.right, old_direita)

    def rotacaoEsquerdaDireita(self):
        print('Rotacao Dupla a Direita')
        self.left.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        print('Rotacao Dupla a Esquerda')
        self.right.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.left.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.right.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()
        print('Executa Balanço')
        self.Preorder(ipe)        

    def insere(self, data):
        print('Insere', data)
        if data == self.data:
            return
        if data <= self.data:
            if not self.left:
                self.left = No(data)
            else:
                self.left.insere(data)
        else:
            if not self.right:
                self.right = No(data)
            else:
                self.right.insere(data)
        #self.Preorder(ipe)        
        self.executaBalanco()

    def Preorder( self, ipe ):
        if( ipe is None ):
            return
        print(ipe.data)
        self.Preorder(ipe.left)
        self.Preorder(ipe.right)

ipe = No(42)

arquivo = open('teste.txt', 'r')
for linha in arquivo:
    ipe.insere(int(linha))
arquivo.close()

print('\n')
ipe.Preorder(ipe)
