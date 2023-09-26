# Escrever um programa para gerar 50 valores aleatórios de 0 a 20 dentro de um vetor:
#depois encontrar a soma dos valores
#O número de ocorrências do valor 9
#O maior valor armazenado
import random

vetor =[]
noves=[]
tamanho = 50

for i in range(tamanho):
    elemento = random.randint(0,20)

    vetor.append(elemento)

soma = sum(vetor)

noves = vetor.count(9)

maior_valor = max(vetor)


print("A soma destes elementos é igual a :",soma)
print(f"O número nove aparece {noves} vezes")
print("O maior valor deste vetor é: ",maior_valor)

