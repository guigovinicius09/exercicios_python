# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
# quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

LATA_TINTA = 18  # litros 108m²
VALOR_LATA = 80  # reais
GALAO_TINTA = 3.6  # litros 21.6m²
VALOR_GALAO = 25  # reais

area_pintar = float(input("Digite a area total da loja: "))
litros_tinta = area_pintar / 6

acrescimo_tinta = litros_tinta * 0.10
litros_total = litros_tinta + acrescimo_tinta
print(f"Utilizará cerca de {litros_tinta} litros de tinta mais um total de {acrescimo_tinta} que correponde 10% a mais.")

# APENAS LATAS DE 18 LITROS
numero_latas = litros_total / LATA_TINTA
valor_total_latas = math.ceil(numero_latas) * VALOR_LATA
print(f"Será necessário a compra de {math.ceil(numero_latas)} latas de tintas, o que lhe custará R$ {valor_total_latas}.")

# APENAS GALÕES DE 3.6 LITROS
numero_galoes = litros_total / GALAO_TINTA
valor_total_galoes = math.ceil(numero_galoes) * VALOR_GALAO
print(f"Será necessário a compra de {math.ceil(numero_galoes)} galões de tintas, o que lhe custará R$ {valor_total_galoes}.")

# MISTURANDO LATAS E GALÕES
