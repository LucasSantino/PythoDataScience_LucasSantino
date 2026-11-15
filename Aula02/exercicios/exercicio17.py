'''
Exercícios - Estrutura de repetição 
2) Solicitar um número e apresentar sua tabuada de 1 a 10 
utilizando for. 
'''


print("Olá, seja bem-vindo!")

numero = int(input("Insira um número: "))

for i in range(1, 11):
    multiplicacao = numero * i
    print(f"{numero} x {i} = {multiplicacao}")


