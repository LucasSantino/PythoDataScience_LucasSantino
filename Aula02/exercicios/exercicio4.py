'''
4)  Escreva um programa que pergunte o preço de três produtos e indique 
qual o produto com menor preço
'''
print("Olá seja bem vindo:")

produto1=float(input("Digite o valor do primeiro produto R$:"))
produto2=float(input("Digite o valor do segundo produto R$: "))
produto3=float(input("Digite o valor do terceiro produto R$: "))

if produto1 < produto2 and produto1 < produto3:
    menor = produto1
elif produto2 < produto1 and produto2 < produto3:
    menor = produto2
else:
    menor = produto3


print(f"\nProduto com menor preço: R$ {menor:.2f}" )