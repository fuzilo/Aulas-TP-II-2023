#Faça um programa para corrigir uma prova com 10 questões de
#multipla escolha ( ´ a, b, c, d ou e), em uma turma com 3 alunos.
#Cada questão vale 1 ponto.
#Leia o gabarito, e para cada aluno leia sua matricula (número inteiro) e
#suas respostas.
#Calcule e escreva: Para cada aluno, escreva sua matrícula, suas
#respostas, e sua nota. O percentual de aprovação, média 7.0.*/

tamanho = int(input("Digite q quantidade de alunos a serem avaliados\n"))

gabarito=[]
matriz=[]
#fazer iteração pra criar gabarito


for r in range(10):
    gaba= str(input(f"Digite o Gabarito da {r+1}ª Questão\n"))
    gabarito.append(gaba)


for i in range (tamanho):
    aluno=[]
    matricula = int(input(f"Insira a matricula do Aluno\n")) 
    aluno.append(matricula)
    resposta_aluno=[]
    for j in range(10):
        resp = str(input(f"Insira a resposta da {j+1}ª questão\n"))
        resposta_aluno.append(resp)
    aluno.extend(resposta_aluno)
    matriz.append(aluno)


for aluno in matriz:
    resposta_aluno=aluno[1:]
    nota=0
    for i, resposta in enumerate(resposta_aluno):
        if resposta==gabarito[i]:
            nota +=1

    aluno.append(nota)


# for i, aluno in enumerate(matriz):
#     print(f"Aluno {i+1}:")
#     for j, resposta in enumerate(aluno[1:-1]):  
#           print(f"Resposta {j+1}: {resposta}")
#     print(f"Matrícula: {aluno[0]}")
#     print(f"Nota: {aluno[-1]}")
alunos_aprovados = []

for aluno in matriz:
    matricula = aluno[0]
    respostas = aluno[1:11]  
    nota = aluno[-1]
    passou = nota >= 7  
    alunos_aprovados.append([matricula, respostas, nota, passou])


for aluno in alunos_aprovados:
    print(f"Matrícula: {aluno[0]}")
    print(f"Respostas: {aluno[1]}")
    print(f"Nota: {aluno[2]}")
    if aluno[3]:
        print("Status: Aprovado")
    else:
        print("Status: Reprovado")
    print()










