import random
import sys
array = list(range(500))

sys.stdout = open('input.txt', 'w')
array = random.sample(range(1000, 10000), len(array))
i = 0
while i < len(array):
    print(array[i])
    i += 1
sys.stdout.close()