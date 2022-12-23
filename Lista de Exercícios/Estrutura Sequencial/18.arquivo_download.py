# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

net_speed = int(input("Digite a velocidade de sua internet: "))
arquivo = int(input("Digite o tamanho do arquivo que deseja fazer o download: "))

tempo_download = arquivo / net_speed
minutos = int(tempo_download // 60)
segundos = int(tempo_download % 60)

if minutos <= 1:
    print(f"O tempo aproximado de download será de {minutos} minuto e {segundos} segundos.")
else:
    print(f"O tempo aproximado de download será de {minutos} minutos e {segundos} segundos.")
