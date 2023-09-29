#Faça um programa para corrigir uma prova com 10 questões de
#multipla escolha ( ´ a, b, c, d ou e), em uma turma com 3 alunos.
#Cada questão vale 1 ponto.
#Leia o gabarito, e para cada aluno leia sua matricula (número inteiro) e
#suas respostas.
#Calcule e escreva: Para cada aluno, escreva sua matrícula, suas
#respostas, e sua nota. O percentual de aprovação, média 7.0.*/

tamanho = int(input("Digite q quantidade de alunos a serem avaliados\n"))
vetor=[]
gabarito=[]
folhaResp=[]
#fazer iteração pra criar gabarito

for i in range(10):
    gaba= str(input(f"Digite a resposta da {i+1}ª Questão"))
    gabarito.append(gaba)

for j in range

