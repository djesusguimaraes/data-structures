"""
    Árvore AVL em Python
    
    Copyright (c) 2009 Vindemiatrix Almuredin.
    É dada permissão para copiar, distribuir e/ou modificar este documento
    sob os termos da Licença de Documentação FAIL,
    Versão 97.545.668.112.666.002 Build 69 Release 42;
    Uma cópia da licença talvez esteja inclusa na seção entitulada
    "Licença de Documentação FAIL".
"""

class No:
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, left, right):
        self.left = left
        self.right = right

    def balanco(self):
        deep_left = 0
        if self.left:
            deep_left = self.left.deep()
        deep_right = 0
        if self.right:
            deep_right = self.right.deep()
        return deep_left - deep_right

    def deep(self):
        deep_left = 0
        if self.left:
            deep_left = self.left.deep()
        deep_right = 0
        if self.right:
            deep_right = self.right.deep()
        return 1 + max(deep_left, deep_right)

    def rotacaoEsquerda(self):
        self.data, self.right.data = self.right.data, self.data
        old_esquerda = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_esquerda, self.left.left)

    def rotacaoright(self):
        self.data, self.left.data = self.left.data, self.data
        old_right = self.right
        self.setaFilhos(self.left.left, self.left)
        self.right.setaFilhos(self.right.right, old_right)

    def rotacaoEsquerdaright(self):
        self.left.rotacaoEsquerda()
        self.rotacaoright()

    def rotacaorightEsquerda(self):
        self.right.rotacaoright()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.left.balanco() > 0:
                self.rotacaoright()
            else:
                self.rotacaoEsquerdaright()
        elif bal < -1:
            if self.right.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaorightEsquerda()

    def insere(self, data):
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
        self.executaBalanco()   

    def Preorder( self, ipe ):

        if( ipe is None ):
            return
        print(ipe.data,end = ' ')
        self.Preorder(ipe.left)
        self.Preorder(ipe.right) 

    def search(self, data, flag):
        flag = flag + 1
        if not self:
            return None
        
        if self.data == data:
            return self.data, flag 

        if data < self.data:
            return self.left.search(data, flag)
        
        return self.right.search(data, flag) 

if __name__ == "__main__":
    ipe = No(8)

    arquivo = open('menor.txt', 'r')
    for linha in arquivo:
        ipe.insere(int(linha))
    arquivo.close()

    #flag = 0
    #print('\n\nPonta: \n')
    #arquivo = open('ponta.txt', 'r')
    #for linha in arquivo:
    #    print(ipe.search(int(linha), flag))
    #arquivo.close()

    #flag = 0
    #print('\n\nMeio à esquerda: \n')
    #arquivo = open('meioL.txt', 'r')
    #for linha in arquivo:
    #    print(ipe.search(int(linha), flag))
    #arquivo.close()

    #flag = 0
    #print('\n\nMeio à direita: \n')
    #arquivo = open('meioR.txt', 'r')
    #for linha in arquivo:
    #    print(ipe.search(int(linha), flag))
    #arquivo.close()

    ipe.Preorder(ipe)
