# Cada vetor é encarregado de fazer um tipo de hashing
Vetor_hash1 = []  # Dorrespondente ao metodo de Divisao
Vetor_hash2 = [] # Dorrespondente ao metodo de Dobramento
Vetor_hash3 = [] # Correspondente ao metodo de Analise numerica

# Abertura do arquivo
d = 0
array = []
with open('input.txt','r') as i: # Input
  while d < 500:
    f_content = i.readline()
    array.append([int(x) for x in f_content.split()])
    d+=1
#----------------------------------------------
# Caso 1 - Divisao
count_1 = 0
for j in range(500):
    aux = sum(array[j])
    key1 = aux%500

    if Vetor_hash1[key1] == None:
        Vetor_hash1[key1] = aux

    else:
        count_1 += 1
        for z in range(500):
            if Vetor_hash1[z] == None:
                Vetor_hash1[z] = aux
                break
            elif(Vetor_hash1[z] == aux):
                count_1 += 1
        

#----------------------------------------------
count_2 = 0
for j in range(500):
    # Dobramento por por XOR
    v = f'{(sum(array[j])):010b}'   
    y = [v[i:i+5] for i in range(0, len(v), 5)]
    result = str(int(y[0]) ^ int(y[1]))[::-1] # inversao do codigo binario para facilitar a convesao para decimal

    key2 = 0
    for i in range(len(result)):
        if int(result[i]) != 0: # caso o numeo seja 0 ele nao conta para conversão
            key2 += pow(2,i) # conversao para decimal

    # Insersao
    aux2 = sum(array[j])
    if Vetor_hash2[key2] == None:
        Vetor_hash2[key2] = aux2

    else:
        
        count_2 += 1
        for z in range(500):
            if Vetor_hash2[z] == None:
                Vetor_hash2[z] = aux2
                break
            elif(Vetor_hash1[z] == aux2):
                count_2 += 1

#----------------------------------------------
# Caso 3 - Analise Numerica
i = 0
d1=[0,0,0,0,0,0,0,0,0,0]
d2=[0,0,0,0,0,0,0,0,0,0]
d3=[0,0,0,0,0,0,0,0,0,0]
d4=[0,0,0,0,0,0,0,0,0,0]
for i in range(500):
    aux3 = sum(array[i])

    temp = int(aux3/1000)
    d1[temp] += 1
    temp = int((aux3/100)%10) 
    d2[temp] += 1
    temp = int((aux3/10)%10) 
    d3[temp] += 1
    temp = int(aux3%10) 
    d4[temp] += 1  
# Calculos
Md= []
for j in range(10):
    Md[0] += abs((d1[j]*10)-500)/10
    Md[1] += abs((d2[j]*10)-500)/10
    Md[2] += abs((d3[j]*10)-500)/10
    Md[3] += abs((d4[j]*10)-500)/10

iMaior = 0
iMenor = 0
i = 0
while i < len(Md):
    if Md[i] > Md[iMaior]:
        iMaior = i
    if Md[i] < Md[iMenor]:
        iMenor = i
    i += 1

count3 = 0 # contado de colisoes do metodo de aanalise de numeros
Numb =[0,0,0,0,0,0,0,0,0,0]

# Insesao
for i in range(500):
    aux3 = sum(array[i])
    if iMenor == 0:
        key3 = int(aux3/1000)
        Numb[key3] = key3
    elif iMenor == 1:
        key3 = int((aux3/100)%10)
        Numb[key3] = key3 
    elif iMenor == 2:
        key3= int((aux3/10)%10)
        Numb[key3] = key3 
    else:
        key3 = int(aux3%10)
        Numb[key3] = key3 
    
    if Vetor_hash3[key3] == None:
        Vetor_hash3[key3] = aux3
    else:
        count3 +=1
        key3 = int((aux3/10))
        if Vetor_hash3[key3] == None:
            Vetor_hash3[key3] = aux3
        else:
            count3 +=1
            key3 = int((aux3/100))
            if Vetor_hash3[key3] == None:
                Vetor_hash3[key3] = aux3
            else:
                count3 +=1
                key3 = int((aux3/1000))
                if Vetor_hash3[key3] == None:
                    Vetor_hash3[key3] = aux3
                else:
                    count3 +=1
                    for z in range(500):
                        if Vetor_hash1[z] == None:
                            Vetor_hash1[z] = aux3
                            break



print("Divisao: " + str(count_1) + " Colisoes")
print("Dobra: " + str(count_2) + " Colisoes")
print("Analise de numeros: " + str(count3) + " Colisoes, " +str(Numb))

O = open('saida.txt', 'w') #output
O.writelines("Divisao: " + str(count_1) + " Colisoes\n")
O.writelines("Dobra: " + str(count_2) + " Colisoes\n")
O.writelines("Analise de numeros: " + str(count3) + " Colisoes, " +str(Numb)+"\n")
O.close()

