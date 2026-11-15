'''
15)Solicite a temperatura e a umidade de um ambiente industrial. Exiba um alerta 
quando a temperatura ultrapassar 35 °C e a umidade estiver abaixo de 30%.
'''


print("Olá, seja bem-vindo!")

try:
    temperatura = float(input("\nInsira o valor da temperatura: "))
    umidade = float(input("\nInsira o valor da umidade (0 a 100%): "))

    if temperatura < 0 or umidade < 0 or umidade > 100:
        print("Os valores informados não podem ser negativos!")

    elif temperatura > 35 and umidade < 30:
        print("\nALERTA: Temperatura acima de 35°C e umidade abaixo de 30%!")

    else:
        print("\nTemperatura e umidade em estado normal.")

except ValueError:
    print("Insira valores numéricos válidos para temperatura e umidade!")

except Exception as erro:
    print("Ocorreu um erro inesperado!")


    