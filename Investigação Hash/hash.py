# Criado por: profa. Divani Barbosa Gavinier
# Curriculo Lattes: http://lattes.cnpq.br/8503400830635447
# divanibarbosa@gmail.com

class Hash:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def divisao(self, key):
          v = int(key)
          return (v % int(self.tam_max))

     def dobra(self, key):
          v = f'{key:010b}'
          y = [v[i:i+5] for i in range(0, len(v), 5)]
          result = str(int(y[0]) ^ int(y[1]))[::-1]

          soma = 0
          x = 1
          for i in range(len(result)):
               soma += int(result[i])*x    
               x *= 2
          return soma

     def cheia(self):
          return len(self.tab) == self.tam_max

     def imprime(self):
          for i in self.tab:
               print("Hash[%d] = " %i, end="")
               print (self.tab[i])
     
     def busca(self, key):
          pos = self.divisao(key)
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == key: # se o item esta na posição indicada pela função hash
               return pos
          else:
               for i in self.tab: # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
                    if self.tab[i]==key:
                         return i
          return -1

     def insere(self, item, colidiu):
          if self.cheia():
               return colidiu

          pos = self.divisao(item)

          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
          else: # se posicao ocupada
               colidiu += 1
               while True:
                    if self.tab[pos] == item: # se o item ja foi cadastrado
                         print("-> ATENCAO Esse item ja foi cadastrado")
                         return
                    if pos == (self.tam_max - 1):
                         pos = -1
                    pos += 1 # incrementa mais uma posição
                    if self.tab.get(pos) == None:
                         self.tab[pos] = item
                         print("-> Inserido apos colisao HASH[%d]" %pos)
                         break              
# fim Classe Hash

tamanhoHash = 500
tab = Hash(tamanhoHash)

colidiu = 0
arquivo = open('input.txt', 'r')
for linha in arquivo:
     print(tab.insere(int(linha), colidiu))
arquivo.close()












"""
print("\n****************************************************")
print("      Tabela HASH Colisoes Linear (%d itens) " %tamanhoHash)
print("****************************************************")
for i in range (0,tamanhoHash,1):
     print("\nInserindo item %d" %(i + 1));
     item = input(" - Forneca valor: ")
     tab.insere(item)
item = input("\n - Forneca valor para buscar: ")
pos = tab.busca(item)
if pos == -1:
     print("-> Item nao encontrado")
else:
     print("-> Item encontrado na posicao: ", pos)
item = input("\n - Forneca valor para apagar: ")
tab.apaga(item)
print("\nImprimindo conteudo")
tab.imprime()
print("\n")
"""