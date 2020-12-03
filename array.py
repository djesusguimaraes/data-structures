import sys
import random

array = list(range(10000))


for i in array:
    array[i] = i + 1

flag = 0
arrayReversed = array.copy()
arrayReversed.reverse()
arrayMed = int(len(array)/2)

sys.stdout = open('arrayConjInterno.txt', 'w')
while flag < 25:
    print(array[flag])
    print(arrayReversed[flag])
    flag += 1
sys.stdout.close()


cont = 1
sys.stdout = open('arrayConjMenor.txt', 'w')
while cont <= 50:
    print(array[arrayMed - cont])
    cont += 1
sys.stdout.close()
   

cont = 0
sys.stdout = open('arrayConjMaior.txt', 'w')
while cont < 50:
    print(array[arrayMed + cont])
    cont += 1
sys.stdout.close()

random.shuffle(array)

sys.stdout = open('arrayFull.txt', 'w')
i = 0
while i < int(len(array)):
    print(array[i])
    i += 1
sys.stdout.close()