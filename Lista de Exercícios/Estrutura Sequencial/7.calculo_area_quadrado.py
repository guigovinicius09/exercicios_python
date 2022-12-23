# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Informe o valor do lado do quadrado: "))

area = lado ** 2
area_dobro = area ** 2

print(f"O valor da área é {area} e o dobro desta área é {area_dobro}")
