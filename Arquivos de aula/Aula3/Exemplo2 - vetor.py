#Definir o tamanho do vetor de forma dinâmica e 
#Atribuir valores dentro do vetor

tamanho= int(input("Digite o tamanho do vetor: \n"))

vetor=[]

##Estrutura de repetição
## -For- executa de acordo com o tamanho digitado pelo ususário
# 

for i in range(tamanho):
    # variável elemento armazena o numero digitado pelo ususário
    elemento = int(input(f"Digite o elemento {i+1} do vetor: \n"))

    #append, adiciona o valor digitado pelo usuário
    vetor.append(elemento)
    #O índice do vetor começa em Zero
print("Vetor: ",vetor)