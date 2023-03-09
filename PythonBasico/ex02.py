#Exercício 02
    
for i in range(1,11):
    print ("Aluno", i)
    nota1 = float(input("Digite a nota 1 do aluno: "))
    nota2 = float(input("Digite a nota 2 do aluno: "))
    nota3 = float(input("Digite a nota 3 do aluno: "))

    media = (nota1 + nota2 + nota3)/3

    if media >= 7.0:
        print ("\nAluno APROVADO\n")

    else: print ("\nAluno REPROVADO\n")



