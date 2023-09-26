print("programa para calcular as grandezas elétricas")

print("Podemos calcular:")

print("1 - Tensão Voltz")
print("2 - Resistência Ohm")
print("3 - Corrente Ampére")

opcao = int(input("Digite a opção desejada:\n"))

if opcao == 1:
    print("Para calcular a tensão siga os passos:")
    res = float(input("Insira a resistência em ohms\n"))
    i = float(input("insira a corrente em ampéres\n"))
    U=res*i
    print("A voltagem é: ",U, "volts")

elif opcao == 2:
    print("Para calcular a resistência siga os passos:")
    U = float(input("Insira a tensão em volts\n"))
    i = float(input("insira a corrente em ampéres\n"))
    res = U/i
    print("A voltagem é: ", res, "ohms")   

elif opcao == 3:
    print("Para calcular a corrente, siga os passos:")
    res = float(input("Insira a resistência em ohms\n"))
    U = float(input("Insira a tensão em volts\n"))
    i=U/res
    print("A voltagem é: ",i, "A")    

else:
    print("Opção inválida")