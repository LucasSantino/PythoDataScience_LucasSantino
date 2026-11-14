'''
8) Uma loja oferece descontos de acordo com o valor total da compra. 
Solicite o nome do cliente e o valor da compra
'''

print("Olá, seja bem vindo!!")

nome_cliente = input("Digite o nome do cliente:")
valor_compra = float(input("Digite o valor da compra R$: "))

if valor_compra < 100:
    desconto = 0

elif valor_compra < 500:
    desconto = 0.05

elif valor_compra < 1000:
    desconto = 0.10

else:
    valor_compra > 1000
    desconto = 0.15

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print(f"\n Resumo da compra:")
print(f"Cliente: {nome_cliente}")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
