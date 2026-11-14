
print("Olá, seja bem-vindo!")

try:
    nome_maquina = input("Digite o nome da máquina: ")

    potencia = float(input("Digite o valor da potência (kW): "))
    quantidade_horas_funcio = float(input("Digite a quantidade de horas de funcionamento: "))

    if potencia <= 0 or quantidade_horas_funcio < 0:
        print("Erro: A potência deve ser maior que zero e as horas não podem ser negativas!")

    else:
        consumo = potencia * quantidade_horas_funcio

        if consumo < 100:
            classificacao = "Baixo consumo"

        elif consumo < 300:
            classificacao = "Consumo moderado"

        else:
            classificacao = "Alto consumo"

        print("\n===== RESULTADO =====")
        print(f"Máquina: {nome_maquina}")
        print(f"Potência: {potencia:.2f} kW")
        print(f"Horas de funcionamento: {quantidade_horas_funcio:.2f} horas")
        print(f"Consumo energético: {consumo:.2f} kWh")
        print(f"Classificação: {classificacao}")

except ValueError:
    print("Erro: Digite apenas valores numéricos para potência e horas!")
    
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
