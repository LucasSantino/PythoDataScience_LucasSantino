'''
10) Uma empresa deseja analisar o desempenho mensal de seus 
vendedores.Desenvolva um programa que solicite o nome de um 
vendedor, sua meta mensal e o valor total vendido.
'''


print("Olá, seja bem-vindo!!")

nome_vendedor = input("Digite o nome do vendedor: ")
meta = float(input("Digite a meta mensal: R$ "))
valor_vendido = float(input("Digite o valor total vendido: R$ "))

if meta <= 0 or valor_vendido < 0:
    print("Erro: A meta deve ser maior que zero e as vendas não podem ser negativas!")

else:
    percentual = (valor_vendido / meta) * 100

    if percentual < 80:
        resultado = "Abaixo da meta"

    elif percentual < 100:
        resultado = "Próximo da meta"

    elif percentual < 120:
        resultado = "Meta atingida"

    else:
        resultado = "Meta superada"

    print("\n===== RESULTADO =====")
    print(f"Vendedor: {nome_vendedor}")
    print(f"Meta mensal: R$ {meta:.2f}")
    print(f"Total vendido: R$ {valor_vendido:.2f}")
    print(f"Atingimento da meta: {percentual:.2f}%")
    print(f"Situação: {resultado}")

    
        
