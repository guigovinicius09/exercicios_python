# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

PESO_LIMITE = 50
peso_peixe = float(input("Digite o valor dos pescados conforme mostra na balança: "))

if peso_peixe > 50:
    excedente = peso_peixe - PESO_LIMITE
    multa = excedente * 4
    print("Você excedeu a quantidade limite estabelecida pelo regulamento.")
    print(f"O valor excedente é de {excedente:.2f} kg e deverá pagar um total de R$ {multa:.2f} de multa.")

else:
    print("A quantidade de pescados está de acordo com o regulamento.")
