'''
Exercícios - Estrutura de repetição 
3) solicitar 10 números e calcular a soma total. 
'''


print("Olá, seja bem-vindo!")

soma = 0

for i in range(1, 11):
    numero = float(input(f"Insira o {i}º número: "))
    soma += numero

print(f"\nA soma total dos números é: {soma:.2f}")
