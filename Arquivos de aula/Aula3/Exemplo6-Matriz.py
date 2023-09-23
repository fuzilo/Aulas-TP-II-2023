#Exemplo Matriz

matriz=[
    [1,2,3],
    [4,5,6],
    [6,5,4]
]

#leitura de uma coluna especifica
print("Mostre a primeira linha e primeira coluna", matriz[0][0])
print("Mostre a segunda linha e terceira coluna", matriz[1][2])
print("Mostre a terceira linha e segunda coluna", matriz[2][1])

print("matriz")
for linha in matriz:
    print(linha)