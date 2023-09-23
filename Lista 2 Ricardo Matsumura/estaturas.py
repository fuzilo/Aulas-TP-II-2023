print("Usuário, insira a medida de estatura de 3 pessoas:")

pessoa1=float(input("Estatura da primeira pessoa\n"))
pessoa2=float(input("Estatura da segunda pessoa\n"))
pessoa3=float(input("Estatura da terceira pessoa\n"))

if pessoa1 == pessoa2 and pessoa1==pessoa3:
    print("“Há, pelo menos, 2 pessoas com a mesma estatura”")
elif pessoa1==pessoa2 or pessoa1==pessoa3 or pessoa2==pessoa3:
    print("“Há, pelo menos, 2 pessoas com a mesma estatura”")

else:
    if pessoa1 > pessoa2 and pessoa1 > pessoa3:
        alto = pessoa1
        if pessoa2 > pessoa3:
            medio = pessoa2
            baixo = pessoa3
        else:
            medio=pessoa3
            baixo=pessoa2
    elif pessoa2 > pessoa1 and pessoa2 > pessoa3:
        alto=pessoa2
        if pessoa1> pessoa3:
            medio = pessoa1
            baixo = pessoa3
        else:
            medio = pessoa3
            baixo = pessoa1
    elif pessoa3> pessoa1 and pessoa3 > pessoa2:
        alto=pessoa3
    if pessoa1> pessoa2:
        medio= pessoa1
        baixo = pessoa2
    else:
        medio=pessoa2
        baixo=pessoa1
    print(alto)

