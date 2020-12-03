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

    def balance(self):
        deepLeft = 0
        if self.left:
            deepLeft = self.left.deep()
        deepRight = 0
        if self.right:
            deepRight = self.right.deep()
        return deepLeft - deepRight

    def deep(self):
        deepLeft = 0
        if self.left:
            deepLeft = self.left.deep()
        deepRight = 0
        if self.right:
            deepRight = self.right.deep()
        return 1 + max(deepLeft, deepRight)

    def rotacaoEsquerda(self):
        self.data, self.right.data = self.right.data, self.data
        old_esquerda = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_esquerda, self.left.left)

    def rotacaoDireita(self):
        self.data, self.left.data = self.left.data, self.data
        old_direita = self.right
        self.setaFilhos(self.left.left, self.left)
        self.right.setaFilhos(self.right.right, old_direita)

    def rotacaoDuplaDireita(self):
        self.left.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDuplaEsquerda(self):
        self.right.rotacaoDireita()
        self.rotacaoEsquerda()

    def verify(self):
        bal = self.balance()
        if bal > 1:
            if self.left.balance() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoDuplaDireita()
        elif bal < -1:
            if self.right.balance() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDuplaEsquerda()

    def insert(self, data):
        if data == self.data:
            return
        if data <= self.data:
            if not self.left:
                self.left = No(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = No(data)
            else:
                self.right.insert(data)
        self.verify()

    def Preorder( self, ipe ):
        if( ipe is None ):
            return
        print(ipe.data)
        self.Preorder(ipe.left)
        self.Preorder(ipe.right) 

    def search(self, data, flag):
        flag += 1
        if self.data == data:
            print(flag)
            return self.data, flag 
        if data < self.data:
            return self.left.search(data, flag)
        return self.right.search(data, flag) 

import sys

arquivo = open('arrayFull.txt', 'r')
ipe = No(int(arquivo.readline()))
for linha in arquivo:
    ipe.insert(int(linha))
arquivo.close()

flag = 0
sys.stdout = open('AVLConjInterno.txt', 'w')
arquivo = open('arrayConjInterno.txt', 'r')
for linha in arquivo:
    ipe.search(int(linha), flag)
arquivo.close()
sys.stdout.close()

flag = 0
sys.stdout = open('AVLConjMenor.txt', 'w')
arquivo = open('arrayConjMenor.txt', 'r')
for linha in arquivo:
    ipe.search(int(linha), flag)
arquivo.close()
sys.stdout.close()

flag = 0
sys.stdout = open('AVLConjMaior.txt', 'w')
arquivo = open('arrayConjMaior.txt', 'r')
for linha in arquivo:
    ipe.search(int(linha), flag)
arquivo.close()
sys.stdout.close()