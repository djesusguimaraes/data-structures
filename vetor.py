if __name__ == "__main__":
    import random

    meuvetor = list(range(10000))
    for i in meuvetor:
        meuvetor[i] = i + 1


    random.shuffle(meuvetor)
    i = 0
    j = 9999
    print('As pontas: \n')
    while i < 25 | j > 9974:
        print('i ', i,'= ', meuvetor[i], ' j ', j, '= ', meuvetor[j])
        i = i + 1
        j = j - 1

    i = 4999
    print('\n\nMeio à esquerda: \n')
    while i >= 4949:
        print(meuvetor[i])
        i = i - 1
    
    i = 5000
    print('\n\nMeio à direita: \n')
    while i <= 5050:
        print(meuvetor[i])
        i = i + 1

    print('\n\n\n\n\n')
    i = 0
    while i <= 9999:
        print(meuvetor[i])
        i = i + 1
        