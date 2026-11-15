'''
14) Solicite o valor de uma compra e informe se o cliente é VIP. O cliente receberá 10% 
de desconto quando a compra for superior a R$ 500 ou ele for VIP. 
'''


print("Olá, seja bem-vindo!")

try:
    valor_compra = float(input("\nInsira o valor da compra: "))
    cliente_vip = input("\nDigite sim/não se o cliente é VIP? ").lower()

    if valor_compra < 0:
        print("Valor da compra inválido. Insira um valor válido!")

    elif valor_compra > 500 or cliente_vip == "sim":
        desconto = valor_compra * 0.10
        valor_final = valor_compra - desconto

        print("\nDesconto de 10% aplicado com sucesso!")
        print(f"Valor do desconto R$: {desconto:.2f}")
        print(f"Valor final da compra R$: {valor_final:.2f}")

    else:
        print("\nDesconto não aplicado.")
        print(f"Valor final da compra R$: {valor_compra:.2f}")

except ValueError:
    print("\nErro. Informe um valor válido para a compra!")

except Exception as erro:
    print("\nOcorreu um erro inesperado!")


