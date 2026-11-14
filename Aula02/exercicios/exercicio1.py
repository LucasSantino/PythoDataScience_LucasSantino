'''
1)Escreva um programa que peça à pessoa usuária para fornecer dois 
números e exibir o número maior
'''

print("Seja Bem vindo!!!")

numero1 = float(input("Digite o Primeiro Numero:"))
numero2 = float(input("Digite o Segundo Numero: "))

if numero1 > numero2:
    print("O maior numero é: ", numero1)

elif numero2 > numero1:
    print("O maior numero é: ", numero2)

else:
    print("Os dois numeros são iguais")