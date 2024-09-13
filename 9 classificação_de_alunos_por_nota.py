# Programa para calcular a média da turma e classificar alunos

# Inicializa listas para armazenar nomes e notas
nomes = []
notas = []

# Coleta os dados dos alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    nomes.append(nome)
    notas.append(nota)

# Calcula a média da turma
media_turma = sum(notas) / len(notas)
print(f"\nMédia da turma: {media_turma:.2f}")

# Classifica cada aluno
print("\nClassificação dos alunos:")
for i in range(5):
    if notas[i] >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print(f"{nomes[i]} - Nota: {notas[i]} - Status: {status}")