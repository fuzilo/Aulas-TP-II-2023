nome = input("Por favor, digite o seu nome\n")
imoveis = int(input("Quantos imóveis você vendeu?\n"))
vendas = float(input("Qual o valor total das vendas?\n"))

comissao = (imoveis*200)+(vendas*0.05)
salario = 1500+comissao

print("O seu salário final será: R$", salario)