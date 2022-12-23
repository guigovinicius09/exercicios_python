# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#     Para pessoa 01: (72.7*h) - 58
#     Para pessoa 02: (62.1*h) - 44.7


altura = float(input("Digite sua altura: "))

peso_ideal_01 = (72.7 * altura) - 58
peso_ideal_02 = (62.1 * altura) - 44.7

print(f"Pessoa 01, seu peso ideal é em torno de {peso_ideal_01:.1f}kg")
print(f"Pessoa 02, seu peso ideal é em torno de {peso_ideal_02:.1f}kg")