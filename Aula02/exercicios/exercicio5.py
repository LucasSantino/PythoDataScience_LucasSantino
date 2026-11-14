'''
5) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a 
quantidade comprada for maior ou igual 15 litros, o desconto será de 4% por litro. Caso contrário, será 
de 3% por litro. Para o diesel, se a quantidade comprada for maior ou igual a 15 litros, o desconto 
será de 5% por litro. Caso contrário, será de 3% por litro. O preço do litro de diesel é R$ 2,00, o preço 
do litro de etanol é R$ 1,70, o preço da gasolina é R$ 4,50. Para gasolina  maior ou igual a 20 L 3 % 
de desconto. Se não, sem desconto. Escreva um programa que leia a quantidade de litros vendidos e 
o tipo de combustível (E para etanol, D para diesel, G - Gasolina) e calcule o valor a ser pago pelo 
cliente. Tenha em mente algumas dicas:

● O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor 
do desconto.
● O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela 
quantidade de litros menos o valor de desconto resultante do cálculo.
'''

print("Olá seja bem vindo:")

combustivel = input("Digite o tipo de combustível (E - Etanol, D - Diesel, G - Gasolina): ").upper()
litros = float(input("Digite a quantidade de litros:"))

if combustivel == "E":
    preco = 1.70
    if preco >= 15:
        desconto = 0.04
    else:
        desconto = 0.03

elif combustivel == "D":
    preco = 2.00
    if preco >= 15:
        desconto = 0.05
    else:
        desconto = 0.03

elif combustivel == "G":
    preco = 4.50
    if preco >= 20:
        desconto = 0.03
    else:
        desconto = 0

else:
    print("Tipo de combustivel invalido")
    exit()


valor_total = preco * litros
valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto

print("\n===== RESUMO DA COMPRA =====")
print(f"Combustível: {combustivel}")
print(f"Quantidade: {litros:.2f} litros")
print(f"Preço por litro: R$ {preco:.2f}")
print(f"Desconto: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")