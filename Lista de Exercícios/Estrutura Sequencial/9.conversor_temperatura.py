# Faça um Programa que peça a temperatura em graus Fahrenheit
# Transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

tf = int(input("Digite a temperatura em graus Fahrenheit: "))
tc = 5 * ((tf - 32) / 9)

print(f"Temperatura Celsius é de {tc:.1f}°C")
