v = f'{key:010b}'
print(v)
y = [v[i:i+5] for i in range(0, len(v), 5)]
result = str(int(y[0]) ^ int(y[1]))[::-1]

soma = 0
x = 1
for i in range(len(result)):
    soma += int(result[i])*x    
    x *= 2
print(soma)