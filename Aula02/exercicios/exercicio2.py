'''
2) Escreva um programa que solicite o percentual de crescimento de 
produção de uma empresa e informe se houve um crescimento 
(porcentagem positiva) ou um decrescimento (porcentagem negativa)
'''

print("Olá seja bem vindo!")
percentual_crescimento = float(input("Digite o percentual de crescimento de produção:"))

if percentual_crescimento > 0:
    print("Houve crescimento(porcentagem positiva) de produção")

elif percentual_crescimento < 0:
    print("Houve decrescimento(porcentagem negativa) de produção")

else:
    print("A produção não apresentou cresimento  ou decrecimento")


