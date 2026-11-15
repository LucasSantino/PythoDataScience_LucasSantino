'''
Exercícios - Estrutura de repetição
5) solicitar a temperatura de 10 máquinas, contar quantas 
ultrapassaram 80 °C e calcular a temperatura média. 
'''


print("Olá, seja bem-vindo!")

soma = 0
contador_alertas = 0

for i in range(10):
    temperatura = float(input(f"Insira a temperatura da máquina {i + 1}: "))

    soma += temperatura

    if temperatura > 80:
        contador_alertas += 1

media = soma / 10

print("\n--- Resultado do monitoramento ---")
print(f"Quantidade de máquinas acima de 80°C: {contador_alertas}")
print(f"Temperatura média das máquinas: {media:.2f}°C")
