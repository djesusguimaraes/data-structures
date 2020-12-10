import random
import sys
array = list(range(500))

sys.stdout = open('input.txt', 'w')
for i in array:
    array[i] = random.randrange(500, 10000, 4)
    print(array[i])
sys.stdout.close()