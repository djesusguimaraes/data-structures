from os import close


class Tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insere(self,value):
        if (self.value is None):
            self.value = value
        else:
            if( value < self.value ):
                if (self.left is None): 
                    self.left = Tree(value)
                else:
                    self.left.insere(value)
            elif( value > self.value ):
                if ( self.right is None):
                    self.right = Tree(value)
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

Root = Tree(5767)

arquivo = open('vetorCompleto.txt', 'r')
for linha in arquivo:
    Root.insere(int(linha))
arquivo.close()
#lista = arquivo.readlines() # readlinesssssss
flag = 0

print('\n\nPonta: \n')
arquivo = open('ponta.txt', 'r')
for linha in arquivo:
    print(Root.search(int(linha), flag))
arquivo.close()

print('\n\nMeio à esquerda: \n')
flag = 0

arquivo = open('meioL.txt', 'r')
for linha in arquivo:
    print(Root.search(int(linha), flag))
arquivo.close()

print('\n\nMeio à direita: \n')
flag = 0
arquivo = open('meioR.txt', 'r')
for linha in arquivo:
    print(Root.search(int(linha), flag))
arquivo.close()