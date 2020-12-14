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
    def __init__(self, value):
        self.value = value
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
        self.value, self.right.value = self.right.value, self.value
        old_esquerda = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_esquerda, self.left.left)

    def rotacaoDireita(self):
        self.value, self.left.value = self.left.value, self.value
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

    def insert(self, value):
        if value == self.value:
            return 
        if value <= self.value:
            if not self.left:
                self.left = No(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = No(value)
            else:
                self.right.insert(value)
        self.verify()

    def Preorder( self, ipe ):
        if( ipe is None ):
            return
        print(ipe.value)
        self.Preorder(ipe.left)
        self.Preorder(ipe.right) 

    def search(self, value, flag):
        flag += 1
        if self.value == value:
            return flag 
        if value < self.value:
            return self.left.search(value, flag)
        return self.right.search(value, flag) 

import sys

arquivo = open('input.txt', 'r')
ipe = No(int(arquivo.readline()))
for linha in arquivo:
    ipe.insert(int(linha))
arquivo.close()

flag = 0
count = 0
sys.stdout = open('AVLoutput.txt', 'w')
arquivo = open('search.txt', 'r')
for linha in arquivo:
    if count >= 50:
        print('\n')
        count = 0
    print(ipe.search(int(linha), flag))
    count += 1
arquivo.close()
sys.stdout.close()