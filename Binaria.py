from os import close


class Tree:
    def __init__(self):
        self.setaTree(None)
        self.right = None
        self.left = None

    def setaTree(self, value):
        self.value = value

    def insere(self, value):
        if not self.value:
            self.value = int(value)
        else:
            if( value < self.value ):
                if (self.left is None): 
                    self.left = value
                else:
                    self.left.insere(value)
            elif( value > self.value ):
                if ( self.right is None):
                    self.right = value
                else:
                    self.right.insere(value)

    def search(self, value, flag):
        flag = flag + 1
        if not self:
            return None
        
        if self.value == value:
            return self.value, flag 

        if value < self.value:
            return self.left.search(value, flag)
        
        return self.right.search(value, flag)

    def Preorder( self, Root ):

        if( Root is None ):
            return
        print(Root.value,end = ' ')
        self.Preorder(Root.left)
        
        self.Preorder(Root.right)

import sys

Root = Tree()

arquivo = open('arrayFull.txt', 'r')
for linha in arquivo:
    Root.insere(int(linha))
arquivo.close()

Root.Preorder(Root)

#flag = 0
#sys.stdout = open('BinariaOutPontas.txt', 'w')
#arquivo = open('arrayPontas.txt', 'r')
#for linha in arquivo:
#    print(Root.search(int(linha), flag))
#arquivo.close()
#sys.stdout.close()


#flag = 0
#sys.stdout = open('BinariaOutMid_L.txt', 'w')
#arquivo = open('arrayMid_L.txt', 'r')
#for linha in arquivo:
#    print(Root.search(int(linha), flag))
#arquivo.close()
#sys.stdout.close()

#flag = 0
#sys.stdout = open('BinariaOutMid_R.txt', 'w')
#arquivo = open('arrayMid_R.txt', 'r')
#for linha in arquivo:
#    print(Root.search(int(linha), flag))
#arquivo.close()
#sys.stdout.close()