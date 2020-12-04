# ED2

COMPARAÇÃO ABB E AVL
    array.py
        Cria e embaralha vetor com 10k posições e separa a saída em 4 arquivos txt: 'arrayFull.txt'(vetor completo), 'arrayConjMenor.txt', 'arrayConjMaior.txt' e 'arrayConjInterno.txt'.
    AVL.py e ABB.py
        Recebem como entrada os arquivos de saída de 'array.py', em ordem:
            1. Recebem 'arrayFull.txt' para inserção dos 10k números;
            2. Recebem 'arrayConjInterno.txt', pesquisa seus números e grava a saída(número de vezes que a função de busca foi acionada para cada valor) no arquivo 'AVLConjInterno.txt' ou 'ABBConjInterno.txt';
            3. Recebem 'arrayConjMenor.txt', pesquisa seus números e grava a saída(número de vezes que a função de busca foi acionada para cada valor) no arquivo 'AVLConjMenor.txt' ou 'ABBConjMenor.txt';
            4. Recebem 'arrayConjMaior.txt', pesquisa seus números e grava a saída(número de vezes que a função de busca foi acionada para cada valor) no arquivo 'AVLConjMaior.txt' ou 'ABBConjMaior.txt';
    Os arquivos de entrada que são gerados pelo script array.py já têm valores, com a necessidade de um novo arranjo basta rodar o script novamente, como a escrita é interna não precisamos apontar arquivos no terminal, basta rodar com o nome do arquivo 'array.py'. 
    A geração dos dados finais se dá rodando os scripts AVL.py e ABB.py, que também fazem gravação interna e retornam 3 arquivos txt com os conjuntos de busca.
