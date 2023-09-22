print("Vamos executar alguns cálculos")
numero1 = float(input("Digite um número positivo"))
print()
numero2 = float(input("Digite outro numero positivo"))


print("Digite uma opção")
print("1 - Média Ponderada")
print("2 - Quadrado da Soma")
print("3 - Cubo do menor numero")

escolha = int(input("Escolha:"))


if escolha ==1:

    print("O peso do 1º numero é 2, e o peso do 2º numero é 3")

    mediaP = ((numero1*2)+(numero2*3))/(2+3)
    print(mediaP)

elif escolha ==2:
    quadradoSoma = (numero1+numero2)**2
    print(quadradoSoma)
elif escolha ==3:
    if numero1>numero2:
        print((numero2)**3)
    else:
        print((numero1**3))
else:
    print("Opção inválida")       