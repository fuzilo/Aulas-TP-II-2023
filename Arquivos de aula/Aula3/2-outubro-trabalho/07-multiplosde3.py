#Solicitar ao usuário um numero natural positivo#
#calcular os próximos 5 números múltiplos de 3
#guardar em um vetor
#imprimir o vetor
vetor=[]
numero = int(input("Digite um numero real positivo\n"))
if numero%3==0:
    for i in range (5):
        vetor.append(numero)
        numero +=3
elif numero%3 ==1: 
    numero +=2
    #if numero%3 ==0:#
    for i in range (5):
        vetor.append(numero)
        numero +=3
else:
    numero +=1
    for i in range (5):        
        vetor.append(numero)
        numero +=3    


print(vetor)