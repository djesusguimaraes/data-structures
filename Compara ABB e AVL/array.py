from abc import abstractproperty
import sys
import random

array = list(range(10000))

for i in array:
    array[i] = i + 1
random.shuffle(array)

flag = 0
arrayReversed = array.copy()
arrayReversed.reverse()
arrayMed = int(len(array)/2)

sys.stdout = open('search.txt', 'w')
while flag < 25:
    print(array[flag])
    print(arrayReversed[flag])
    flag += 1
   
count = 0
flag = 0
while flag < 50:
    if arrayReversed[count] < arrayMed:
        print(arrayReversed[count])
        flag += 1
    count += 1        

count = 0
flag = 0
while flag < 50:
    if arrayReversed[count] > arrayMed:
        print(arrayReversed[count])
        flag += 1
    count += 1        
sys.stdout.close()

sys.stdout = open('input.txt', 'w')
count = 0
while count < int(len(array)):
    print(array[count])
    count += 1
sys.stdout.close()