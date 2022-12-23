# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# # sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# Serviço 8h diárias, 40h semanais
# 5 dias por semana, 20 dias por mês

salario_hora = int(input("Quanto você ganha por horas trabalhadas?\n\n"))
horas_mes = 8 * 20
salario_bruto = salario_hora * horas_mes

print(f"Número de horas trabalhadas é de {horas_mes} horas mensais com um salário mensal de R${salario_bruto:.2f}")

imposto_de_renda = salario_bruto  * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_de_renda + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f"Salário bruto mensal no valor de R$ {salario_bruto:.2f}, com descontos de:\nR$ {imposto_de_renda:.2f} de imposto de renda\nR$ {inss:.2f} de INSS e\nR$ {sindicato:.2f} de sindicato.")
print(f"\nO salário liquido é de R$ {salario_liquido:.2f}")
