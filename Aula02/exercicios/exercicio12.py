'''
12) Um sistema monitora a temperatura e a vibração de uma máquina industrial.
Criar um programa para permitir que o usuário digite a temperatura e o sistema emita 
um alerta quando
a temperatura ultrapassar 80 °C ou a vibração ultrapassar 15 mm/s
'''


print("Olá, seja bem-vindo!!")

try:
    temperatura = float(input("Digite o valor da temperatura: "))
    vibracao = float(input("Digite o valor da vibração mm/s: "))

    if temperatura < 0 or vibracao < 0:
        print("Erro: Os valores não podem ser negativos!")

    elif temperatura > 80 or vibracao > 15:
        print("\nALERTA!! Limites de temperatura ou vibração ultrapassados!")

        if temperatura > 80:
            print("\nAlerta! Aumento da temperatura ultrapassando 80°C!")

        if vibracao > 15:
            print("\nAlerta! Aumento no nível de vibração ultrapassando 15 mm/s!")

    else:
        print("\nMáquina em estado normal!")

except ValueError:
    print("Digite valores numéricos válidos para temperatura e vibração!")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")






