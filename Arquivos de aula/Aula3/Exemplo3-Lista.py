import numpy as np
#importação de biblioteca

tamanho = int(input("Digite o tamanho do Vetor \n"))

vetor = np.empty(tamanho, dtype=int)

for i in range(tamanho):
    elemento= int(input(f"Digite o elemento {i+1} do vetor\n"))
    vetor[i]=elemento

print("Vetor", vetor)