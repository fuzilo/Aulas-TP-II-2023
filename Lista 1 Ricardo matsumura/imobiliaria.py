nome = input("Por favor, digite o seu nome")
imoveis = int(input("Quantos imóveis você vendeu?"))
vendas = float(input("Qual o valor total das vendas?"))

comissao = (imoveis*200)+(vendas*0.05)
salario = 1500+comissao

print("O seu salário final será: ", salario)