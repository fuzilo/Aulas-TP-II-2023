
vetor=[]

print("Neste programa, iremos calcular a média das notas que você deverá inserir\n")
tamanho=int(input("Quantas notas irá analisar?\n"))

for i in range(tamanho):
    nota=(float(input(f"Digite a {i+1}º nota\n")))
    vetor.append(nota)


media=round((sum(vetor)/tamanho),2)

print(f"A média das notas é de :", media)
