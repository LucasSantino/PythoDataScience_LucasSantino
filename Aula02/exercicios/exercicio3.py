print("Olá, seja bem-vindo!")

valor1 = float(input("Digite o preço do primeiro ano: R$ "))
valor2 = float(input("Digite o preço do segundo ano: R$ "))
valor3 = float(input("Digite o preço do terceiro ano: R$ "))

if valor1 > valor2 and valor1 > valor3:
    maior = valor1
elif valor2 > valor1 and valor2 > valor3:
    maior = valor2
else:
    maior = valor3

if valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor1 and valor2 < valor3:
    menor = valor2
else:
    menor = valor3

print(f"\nMaior preço: R$ {maior:.2f}")
print(f"Menor preço: R$ {menor:.2f}")