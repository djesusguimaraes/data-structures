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
        self.data, self.right.data = self.right.data, self.data
        old_esquerda = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_esquerda, self.left.left)

    def rotacaoDireita(self):
        self.data, self.left.data = self.left.data, self.data
        old_direita = self.right
        self.setaFilhos(self.left.left, self.left)
        self.right.setaFilhos(self.right.right, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.left.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
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

    def insere(self, data):
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
        self.executaBalanco()

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
    ipe.insere(int(linha))
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