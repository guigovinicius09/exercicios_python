# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

N1 = float(input("Digite a nota do primeiro bimestre: "))
N2 = float(input("Digite a nota do segundo bimestre: "))
N3 = float(input("Digite a nota do terceiro bimestre: "))
N4 = float(input("Digite a nota do quarto bimestre: "))

media = (N1 + N2 + N3 + N4) / 4
print(f"A média das notas é: {media:.1f}")
