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
            print(flag)
            return self.value, flag 

        if value < self.value:
            return self.left.search(value, flag)
        
        return self.right.search(value, flag)

    def Preorder( self, Root):
        if not Root:
            return
        print(Root.value)
        self.Preorder(Root.left)
        self.Preorder(Root.right)

import sys

arquivo = open('arrayFull.txt', 'r')
Root = No(int(arquivo.readline()))
for linha in arquivo:
    Root.insere(int(linha))
arquivo.close()

flag = 0
sys.stdout = open('BinariaOutPontas.txt', 'w')
arquivo = open('arrayPontas.txt', 'r')
for linha in arquivo:
    Root.search(int(linha), flag)
arquivo.close()
sys.stdout.close()

flag = 0
sys.stdout = open('BinariaOutMid_L.txt', 'w')
arquivo = open('arrayMid_L.txt', 'r')
for linha in arquivo:
    Root.search(int(linha), flag)
arquivo.close()
sys.stdout.close()

flag = 0
sys.stdout = open('BinariaOutMid_R.txt', 'w')
arquivo = open('arrayMid_R.txt', 'r')
for linha in arquivo:
    Root.search(int(linha), flag)
arquivo.close()
sys.stdout.close()