alunos = []
notas = []

for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    nota = int(input("Digite a nota do aluno: "))
    alunos.append(aluno)
    notas.append(nota)

    for i in range(5):
        print(f"O aluno {alunos[i]} tirou nota {notas[i]}")
        