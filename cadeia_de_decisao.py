#Exemplo2
#Algoritmo para solicitação de empréstimo

print("Programa de empréstimos ## Responda (0 - Não, 1 - Sim)")
nomeNegativado = int(input("Possui nome negativado?"))
if nomeNegativado == 1:
    print("Não pode realizar empréstimo!")
else:
    carteiraAssinada= int(input("Possui carteira Assinada?"))
    if carteiraAssinada == 0:
        print("Não pode realizar empréstimo!")
    else:
        possuiCasaPropria=int(input("Possui Casa Própria?"))
        if possuiCasaPropria == 0:
            print("Não pode realizar empréstimo!")
        else:
            print("Conceder empréstimo")

