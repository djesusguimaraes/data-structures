from operator import itemgetter
import operator
import sys
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