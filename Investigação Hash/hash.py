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

     def digitos(self, item):

          return

     def apaga(self):
          pos = 0
          while pos < self.tam_max:
               del self.tab[pos]
               pos += 1

     def cheia(self):
          return len(self.tab) == self.tam_max

     def insere(self, item, flag):
          colidiu = 0
          if self.cheia():
               self.apaga()
               return 
          pos = 0
          if flag < 1:
               pos = self.divisao(item)
          elif flag < 2:
               pos = self.dobra(item)
          #else:
          #     pos = self.digitos(item)

          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
               return colidiu
          else: # se posicao ocupada
               colidiu += 1
               while True:
                    if self.tab[pos] == item: # se o item ja foi cadastrado
                         return colidiu
                    if pos == (self.tam_max - 1):
                         pos = -1
                    pos += 1 # incrementa mais uma posição
                    if self.tab.get(pos) == None:
                         self.tab[pos] = item
                         return colidiu
                    colidiu += 1
# fim Classe Hash
import sys

tamanhoHash = 500
tab = Hash(tamanhoHash)
tabe = Hash(tamanhoHash)

colisoesDivisao = 0
colisoesDobra = 0
colisoesDigitos = 0

sys.stdout = open('output.txt', 'w')
arquivo = open('input.txt', 'r')
for linha in arquivo:
     colisoesDivisao += tab.insere(int(linha), 0)
print('Divisao:',colisoesDivisao,'colisoes')
arquivo.close()

arquivo = open('input.txt', 'r')
for linha in arquivo:
     colisoesDobra += tabe.insere(int(linha), 1)
print('Dobra:', colisoesDobra,'colisoes')
arquivo.close()

'''arquivo = open('input.txt', 'r')
for linha in arquivo:
     colisoesDigitos += tabe.insere(int(linha), 2)
print('Dobra:', colisoesDigitos,'colisoes')
arquivo.close()'''
sys.stdout.close()












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