#Exemplo com lista 1 break
localizar= "banana"
frutas = ["maçã", "banana", "laranja"]
for lista in frutas:
    if lista == localizar:
        print(f"Encontrado:{localizar}")
        break
    else:
        print(f"{localizar} não encontrado")
#break para parada do algoritmo

#exemplo com lista 2 continue

numero =[1,2,3,4,5,6,7,8,10]
for numero in numero:
    if numero %2 ==0:
        #pula os numeros pares
        continue
    print(f"Numero ímpar:{numero}")

#exemplo lista 3 criado pelo usuario
#lista
numeros_lista = []
for i in range(1,5):
    numero = float(input(f"Digite o {i} numero"))
    numeros_lista.append(numero)

    ##append usado para mostrar que a lista recebe valores da variável

    print("numeros digitados: ")
    for numero in numeros_lista:
        print(numero)