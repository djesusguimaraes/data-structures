
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
print(desvio)
digitos = list(range(3))
aux = max(desvio)
while i < len(desvio):
    if desvio[i] < aux:
        digitos[j] = i
        j += 1
    i += 1
print(digitos)

item = 5971
i = 0
digkey = list(range(3)) 
while i < len(digitos):
    if digitos[i] == 0:
        digkey[i] = int(item / pow(decimal, 3))
    elif digitos[i] == 1:
        digkey[i] = int((item / pow(decimal, 2)) % decimal)
    elif digitos[i] == 2:
        digkey[i] = int((item / decimal) % decimal)
    else:
        digkey[i] = int(item % decimal)
    i += 1
print(digkey)
key = 0
j = 100
i = 0
while i < len(digkey):
    key += int(digkey[i]*j) 
    j = j / 10
    i += 1
if key > len(array):
    key = key % len(array)
print(key)