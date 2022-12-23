# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 m² quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço
# total.

# Uma lata de tinta pinta 54 m²


LATA_TINTA = 18  # litros
VALOR_LATA = 80

area_pintar = float(input("Digite a area total da loja: "))
litros_tinta = area_pintar / 3

print(f"Utilizará cerca de {int(round(litros_tinta))} litros de tinta")

numero_latas = litros_tinta / LATA_TINTA
valor_total = round(numero_latas) * VALOR_LATA

print(f"Será necessário a compra de {round(numero_latas)} latas de tintas, o que lhe custará R$ {valor_total}.")
