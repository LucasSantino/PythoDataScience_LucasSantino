'''
11) Uma indústria utiliza sensores para monitorar a temperatura de suas 
máquinas. Desenvolva um programa que solicite o nome da máquina e sua 
temperatura atual em graus Celsius.Utilize estruturas condicionais para 
determinar o estado operacional:
'''

print("Olá, seja bem vindo!!")
try:
    nome_maquina = input("Digite o nome da maquina: ")
    temperatura = float(input("Digite o valor atual da temperatura: "))

    if temperatura < 40:
        estado = " Operação normal"

    elif temperatura < 60:
        estado = "Atenção"

    elif temperatura < 80:
        estado = "Alerta de aquecimento"

    else:
        estado = "temperatura critica"

    print("\n__RESULTADO__")
    print(f"Máquina: {nome_maquina}")
    print(f"Temperatura: {temperatura:.2f} °C")
    print(f"Estado operacional: {estado}")

    if temperatura > 80:
        print("ALERTA: verificar imediatamente a máquina!")

except ValueError:
    print("Erro: Digite uma temperatura numérica válida!")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")


