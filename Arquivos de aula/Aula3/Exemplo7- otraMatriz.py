linhas=(int(input("Digite o numero de Linhas da matriz")))
colunas=int(input("Digite o numero de colunas da matriz"))
matriz_numeros=[]

for i in range(linhas):
    linha=[]
    for j in range(colunas):
        numero=float(input(f"Digite o numero para posição({i},{j})"))
        linha.append(numero)
    matriz_numeros.append(linha)

print(matriz_numeros)

#Exibição da matriz (utilização função join)        

for linha in matriz_numeros:
    print(' '.join(map(str,linha)))

    #função adicionar todo conteúdo dentro de uma string
    #map parametro da função join
    