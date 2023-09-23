pessoa1 = float(input("Digite a altura de uma pessoa\n"))
pessoa2 = float(input("Digite a altura de outra pessoa\n"))
pessoa3 = float(input("Digite a altura de mais uma pessoa\n"))

## alto, medio, baixo

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

if pessoa1==pessoa2 and pessoa1==pessoa3:
    print(pessoa1)
    print(pessoa2)
    print(pessoa3)
else: 
    print(alto)
    print(medio)
    print(baixo)


    
            



