# Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela.

# importaçao a biblioteca de data e hora
import datetime 

# Entrada dos Dados
data_atual = datetime.date.today()
ano_nasc = int(input('Informe o ano de nascimento: '))
ano_atual = data_atual.year

# Processamento de dados 

idade = ano_atual - ano_nasc

#saida de dados 
print(f'A sua idade é {idade}')