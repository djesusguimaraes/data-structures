import random
m = list(range(10))

for i in m:
    m[i] = random.randrange(1, 100)
print(m,'\n')
l = min(m)
print(l)
iMaior = 0
iMenor = 0
i = 0
while i < len(m):
    if m[i] > m[iMaior]:
        iMaior = i
    if m[i] < m[iMenor]:
        iMenor = i
    i += 1
print(iMenor)