# Criado por: profa. Divani Barbosa Gavinier
# Curriculo Lattes: http://lattes.cnpq.br/8503400830635447
# divanibarbosa@gmail.com

class No:
     def __init__(self, item, next = None):
          self.item = item
          self.next = next

class Hash(No):

     def __init__(self, tam):
          No. __init__(self, item = None, next = None)
          self.tab = {}
          self.tam_max = tam
          self.inicio = None

     def divisao(self, key):
          return int(key) % int(self.tam_max)

     def dobra(self, key):
          v = f'{key:010b}'
          y = [v[i:i+5] for i in range(0, len(v), 5)]
          result = str(int(y[0]) ^ int(y[1]))[::-1]

          soma = 0
          for i in range(len(result)):
               if int(result[i]) != 0:
                    soma += pow(2,i)
          return soma

     def digitos(self):
          decimal = 10
          array = list(range(500))
          arquivo = open('input.txt', 'r')
          i = 0 
          for linha in arquivo:
               array[i] = int(linha)
               i += 1
          arquivo.close()

          flag1 = list(range(decimal))
          flag2 = list(range(decimal))
          flag3 = list(range(decimal))
          flag4 = list(range(decimal))
          for i in range(decimal):
               flag1[i] = 0
               flag2[i] = 0
               flag3[i] = 0
               flag4[i] = 0

          i = 0
          while i < len(array):
               flag1[int(array[i] / pow(decimal, 3))] += 1
               flag2[int((array[i] / pow(decimal, 2)) % decimal)] += 1
               flag3[int((array[i] / decimal) % decimal)] += 1
               flag4[int(array[i] % decimal)] += 1
               i += 1

          i = 0
          d1 = 0
          d2 = 0
          d3 = 0
          d4 = 0
          while i < decimal:
               d1 += abs(flag1[i]-len(array)/decimal)  
               d2 += abs(flag2[i]-len(array)/decimal)  
               d3 += abs(flag3[i]-len(array)/decimal)  
               d4 += abs(flag4[i]-len(array)/decimal)  
               i += 1

          i = 0
          j = 0
          desvio = [d1, d2, d3, d4]
          digitos = list(range(3))
          aux = max(desvio)
          while i < len(desvio):
               if desvio[i] < aux:
                    digitos[j] = i
                    j += 1
               i += 1

          return digitos

     def encadeia(self, item, colisaoSecundaria):
          if self.inicio is None:
               self.inicio = No(item, None)
          aux = self.inicio
          while aux.next is not None:
               aux = aux.next
          aux.next = No(item, None)
          return colisaoSecundaria

     def cheia(self):
          return len(self.tab) == self.tam_max

     def insere(self, item, flag):
          decimal = 10
          colidiu = 0
          if self.cheia():
               return

          key = 0
          if flag == -1:
               key = self.divisao(item)
          elif flag == -2:
               key = self.dobra(item)
          else:
               i = 0
               digkey = list(range(3)) 
               while i < len(flag):
                    if flag[i] == 0:
                         digkey[i] = int(item / pow(decimal, 3))
                    elif flag[i] == 1:
                         digkey[i] = int((item / pow(decimal, 2)) % decimal)
                    elif flag[i] == 2:
                         digkey[i] = int((item / decimal) % decimal)
                    else:
                         digkey[i] = int(item % decimal)
                    i += 1
               i = 0
               j = 100
               while i < len(digkey):
                    key += int(digkey[i]*j) 
                    j = j / 10
                    i += 1
               if key > self.tam_max - 1:
                    key = key % self.tam_max

          if self.tab.get(key) == None: # se posicao vazia
               self.tab[key] = item
               return colidiu
          else: # se posicao ocupada
               colidiu += 1
               return colidiu + self.tratamento(key, item)

     def tratamento(self, key, item):
          key = self.tam_max - 1 #seta a chave para a ultima posição da tabela
          while True:
               key -= 1 # decrementa mais uma posição
               if self.tab.get(key) == None:
                    self.tab[key] = item
                    return self.encadeia(item, 1)

# fim Classe Hash
import sys

tamanhoHash = 500
tab = Hash(tamanhoHash)
tabe = Hash(tamanhoHash)
taby = Hash(tamanhoHash)

colisoesDivisao = 0
colisoesDobra = 0
colisoesDigitos = 0

sys.stdout = open('output.txt', 'w')
arquivo = open('input.txt', 'r')
for linha in arquivo:
     colisoesDivisao += tab.insere(int(linha), -1)
print('Divisao:',colisoesDivisao,'colisoes')
arquivo.close()

arquivo = open('input.txt', 'r')
for linha in arquivo:
     colisoesDobra += tabe.insere(int(linha), -2)
print('Dobra:', colisoesDobra,'colisoes')
arquivo.close()

arquivo = open('input.txt', 'r')
flag = tab.digitos()                   
for linha in arquivo:
    colisoesDigitos += taby.insere(int(linha), flag)
print('Analise de Digitos: %d colisoes usando os digitos d%d, d%d, d%d' % (colisoesDigitos, flag[0]+1, flag[1]+1, flag[2]+1))
arquivo.close()
sys.stdout.close()