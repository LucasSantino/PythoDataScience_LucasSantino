'''
Exercícios
6) Em uma empresa de venda de imóveis você precisa criar um código que analise os 
dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa 
coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um 
cálculo de variação percentual. A partir do valor da variação, deve ser enviada às 
seguintes sugestões:
● Para variação acima de 20%: bonificação para o time de vendas.
● Para variação entre 2% e 20%: pequena bonificação para time de vendas.
● Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
● Para bonificações abaixo de -10%: corte de gastos.
'''

print("Olá seja bem vindo!!")

vendas2022 = int(input("Digite a quantidade de vendas do ano de 2022: "))
vendas2023 = int(input("Digite a quanti de vendadas do ano de 2023: "))


if vendas2022 <= 0:
    print("A quantidade de vendas precisa ser maior que 0!")

else: 
    variacao = ((vendas2023 - vendas2022)/vendas2022*100)
    print(f"\nVariação percentual: {variacao:.2f}%")

    if variacao > 20:
        print("Sugestão: bonificação para o time de vendas:")

    elif variacao >= 0.02:
        print("Pequena bonificação para o time de vendas:")

    if variacao >= -10:
        print("Planejamento de politicas de incentivo ás vendas")

    else:
        print("Sugestão: corte de gastos")
        exit()

