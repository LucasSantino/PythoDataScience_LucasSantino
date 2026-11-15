'''
Exercícios - Estrutura de repetição 
4) solicitar as notas de 5 alunos e calcular a média da turma.
'''

print("Olá, seja bem vindo!")

soma = 0

for i in range(5):
    nota = float(input(f"insira o {i + 1} valor da nota: "))
    soma += nota

media = soma/5

print(f"Valor da média da turma: {media}")