'''
7) Desenvolva um programa que solicite dois números e uma operação 
matemática (+, -, * ou /). Utilize estruturas condicionais para identificar 
a operação e apresentar o resultado. Caso o usuário escolha uma 
divisão por zero, exiba uma mensagem de erro.
'''

print("Olá, seja bem vindo!!")

numero1 = float(input("Digite o primeiro valor:"))
numero2 = float(input("Digite o seundo valor: "))

operacao = input("Escolha umas das operaçoes (+, -, * ou /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"resultado da adição: {resultado}")

elif operacao == "-":
    resultado = numero2 - numero1
    print(f"Resultado da subtração: {resultado}")

elif operacao == "*":
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado}")

elif operacao == "/":
    if numero2 == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado}")

else:
    print("Operação invalida!")
    



    