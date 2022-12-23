# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     A. o produto do dobro do primeiro com metade do segundo .
#     B. a soma do triplo do primeiro com o terceiro.
#     C. o terceiro elevado ao cubo.

numero_1 = int(input("O primeiro número deve ser um INTEIRO:\n"))
numero_2 = int(input("O segundo  número deve ser um INTEIRO:\n"))
numero_3 = float(input("O terceiro número deve ser um número REAL:\n"))

print(f"Primeiro número é {numero_1}")
print(f"Segundo número é {numero_2}")
print(f"Terceiro número é {numero_3}")

# Resolução A
resultado_A = (numero_1 * 2) * (numero_2 / 2)
print(f"Resolução A é: {resultado_A}")

# Resolução B
resultado_B = (numero_1 * 3) + numero_3
print(f"Resolução B é: {resultado_B}")

# Resolução C
resultado_C = numero_3 ** 3
print(f"Resolução C é: {resultado_C}")