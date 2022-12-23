# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

# Serviço 8h diárias, 40h semanais
# 5 dias por semana, 20 dias por mês

salario_hora = int(input("Quanto você ganha por horas trabalhadas?\n\n"))
horas_mes = 8 * 20
salario_mes = salario_hora * horas_mes

print(f"Número de horas trabalhadas é de {horas_mes} horas mensais com um salário mensal de R${salario_mes:.2f}")
