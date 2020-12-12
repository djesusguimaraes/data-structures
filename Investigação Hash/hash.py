# Criado por: profa. Divani Barbosa Gavinier
# Curriculo Lattes: http://lattes.cnpq.br/8503400830635447
# divanibarbosa@gmail.com

# class No:
#      def __init__(self, item, next = None):
#           self.item = item
#           self.next = next

class Hash():

     def __init__(self, tam):
          self.tab = {}
          self.tam_max = tam

     def divisao(self, key):
          return (int(key) % int(self.tam_max)-200)

     def dobra(self, key):
          v = f'{key:010b}'
          y = [v[i:i+5] for i in range(0, len(v), 5)]
          result = str(int(y[0]) ^ int(y[1]))[::-1]

          soma = 0
          for i in range(len(result)):
               if int(result[i]) != 0:
                    soma += pow(2,i) 
          return soma

     # def digitos(self):
     #      iMaior = 0
     #      iMenor = 0
     #      temp = 0
     #      decimal = 10
     #      array = list(range(self.tam_max))
     #      Md = []
     #      d1=[] # Milhar
     #      d2=[] # Centena
     #      d3=[] # Dezena
     #      d4=[] # Unidade

     #      sys.stdout = open('vetorfelipe.txt', 'w')
     #      arquivo = open('input.txt', 'r')
     #      i = 0
     #      for linha in arquivo:
     #           array[i] = int(linha)
     #      print(array)
     #      sys.stdout.close()
     #      aux = sum(array)

     #      k = int(aux / pow(decimal, 3))
     #      d1[k] += 1
     #      k = int((aux / pow(decimal,2)) % decimal)
     #      d2[k] += 1
     #      k = int((aux / decimal) % decimal)
     #      d3[k] += 1
     #      k = int(aux % decimal)
     #      d4[k] += 1  
          
     #      for j in range(decimal):
     #           Md[0] += abs((d1[j]*decimal)-self.tam_max)/decimal
     #           Md[1] += abs((d2[j]*decimal)-self.tam_max)/decimal
     #           Md[2] += abs((d3[j]*decimal)-self.tam_max)/decimal
     #           Md[3] += abs((d4[j]*decimal)-self.tam_max)/decimal
          
     #      i = 0
     #      while i < len(Md):
     #           if Md[i] > Md[iMaior]:
     #                iMaior = i
     #           if Md[i] < Md[iMenor]:
     #                iMenor = i
     #           i += 1

     #      return iMenor

     # def encadeia(self, item, colisaoSecundaria):
     #      if self.list is None:
     #           self.list = No(item, None)
     #      aux = self.list 
     #      while aux.next is not None:
     #           aux = aux.next
     #           colisaoSecundaria += 1
     #      aux.next = No(item, None)
     #      return colisaoSecundaria

     def cheia(self):
          return len(self.tab) == self.tam_max

     def insere(self, item, flag):
          #decimal = 10
          colidiu = 0
          if self.cheia():
               return
          
          key = 0
          if flag == -1:
               key = self.divisao(item)
          elif flag == -2:
               key = self.dobra(item)
          # else:
          #      if flag == 0:
          #           key = int(item / pow(decimal, 3))
          #      elif flag == 1:
          #           key = int((item / pow(decimal, 2)) % decimal)
          #      elif flag == 2:
          #           key= int((item / decimal) % decimal)
          #      else:
          #           key = int(item % decimal)

          if self.tab.get(key) == None: # se posicao vazia
               self.tab[key] = item
               return colidiu
          else: # se posicao ocupada
               colidiu += 1
               return colidiu + self.tratamento(key, item)
          
     def tratamento(self, key, item):
          colisaoSecundaria = 0
          # testa se key 0-99 vai pro final do P
          # 100-299 soma 200
          while True:
               if key > self.tam_max - 1:
                    key = -1
               key *= 2 # decrementa mais uma posição
               if self.tab.get(key) == None:
                    self.tab[key] = item
                    return colisaoSecundaria
               colisaoSecundaria += 1

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

# arquivo = open('input.txt', 'r')
# flag = tab.digitos()
# for linha in arquivo:
#      colisoesDigitos += taby.insere(int(linha), flag)
# print('Analise de Digitos:', colisoesDigitos,'colisoes usando os digitos')
# arquivo.close()
sys.stdout.close()
