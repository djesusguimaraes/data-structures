from os import close

class No:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insere(self,value):
        if value == self.value:
            return 
        if value < self.value:
            if not self.left: 
                self.left = No(value)
            else:
                self.left.insere(value)
        elif value > self.value:
            if not self.right:
                self.right = No(value)
            else:
                self.right.insere(value)

    def search(self, value, flag):
        flag += 1
        if self.value == value:
            return flag 
        if value < self.value:
            return self.left.search(value, flag)
        
        return self.right.search(value, flag)

    def Preorder( self, ipe):
        if not ipe:
            return
        print(ipe.value)
        self.Preorder(ipe.left)
        self.Preorder(ipe.right)

import sys

arquivo = open('input.txt', 'r')
ipe = No(int(arquivo.readline()))
for linha in arquivo:
    ipe.insere(int(linha))
arquivo.close()

flag = 0
count = 0
sys.stdout = open('ABBoutput.txt', 'w')
arquivo = open('search.txt', 'r')
for linha in arquivo:
    if count >= 50:
        print('\n')
        count = 0
    print(ipe.search(int(linha), flag))
    count += 1
arquivo.close()
sys.stdout.close()