print("Programa de cálculo de Descontos de vendas\n")

qtd = float(input("Digite a quantidade de peças vendidas\n"))
valor = 12.5

if qtd > 0 and qtd <=5:
    print("O valor final da compra de ", qtd, "camisas é: R$ ",round(qtd*valor*.97, 2))

elif qtd >5 and qtd <=10:
    print("O valor final da compra de ", qtd, " camisas é: R$", round(qtd*valor*.95, 2))

elif qtd >10:
    print("O valor final da compra de ",qtd," camisas é: R$",round(qtd*valor*.93, 2))