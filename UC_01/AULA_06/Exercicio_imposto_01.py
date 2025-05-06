# 1- Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:   
# a) salário bruto. 
# b) Quanto pagou ao IRRF. 
# c) quanto pagou ao INSS. 
# d) quanto pagou ao sindicato. 
# e) o salário líquido.

# Entrada dos Dados:
horas_trabalhadas = float(input('Digite suas horas trabalhadas: '))
salario_dias = int(input('Digite o dias trabalhados: '))
salarios_horas = int(input("Digite o salario em horas trabalhadas: "))
salario_bruto = salario_dias*horas_trabalhadas*salarios_horas

INSS = []
IRRF = []
SINDICATO = []


# Processamento dos dados
IRRF = 0.11*salario_bruto
INSS = 0.08*salario_bruto
SINDICATO = 0.05*salario_bruto
imposto = salario_bruto - IRRF - INSS - SINDICATO


# Saida dos dados 

print(f'Seu salário bruto é R$: {salario_bruto:.2f}')
print(f'Seu imposto de renda é R$: {IRRF}')
print(f'Seu imposto do inss é R$: {INSS}')
print(f'Seu imposto do sindicado é R$: {SINDICATO:.01f}')
print(f'Seu salário líquido é R$: {imposto:.01f}   ')

