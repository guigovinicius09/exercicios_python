# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

tc = float(input("Digite a temperatura em graus Celsius: "))
tf = (tc * 1.8) + 32

print(f"A temperatura é {tf:.1f}°F")
