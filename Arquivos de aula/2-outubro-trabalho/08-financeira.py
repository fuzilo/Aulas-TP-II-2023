##renda mensal
##valor total solicitado do empréstimo
##numero de prestações
print('Programa de cáculo de empréstimo\n')

renda= float(input("Digite o valor do seu salário\n"))
empre= float(input("Digite o valor do empréstimo que deseja solicitar\n"))
parcela=int(input("Digite o numero de parcelas que deseja pagar:\n"))

if(empre<=(renda*10) and empre>0 ):

    parcelas =int( empre/(renda*.3))
    presta=float(renda*.3)
    if(parcela>parcelas):
        print("Empréstimo concedido\n")
        print(f"Você pagará valor de {round(empre/parcela,2)} em {parcela} prestações")
        print("\n")
    else:
        print(f"Empréstimo recusado, o valor máximo das parcelas é de {presta}")
elif(empre>(renda*10)):
    print("Empréstimo recusado, o valor máximo de empréstimo foi ultrapassado")