


print("é pra somar os dois maiores?\n")
vetor=[]
for i in range(3):
    numero=int(input(f"Digite o {i+1} numero"))
    vetor.append(numero)
vetor.sort(reverse=True)
print(vetor)

soma=vetor[0]+vetor[1]
print(soma)