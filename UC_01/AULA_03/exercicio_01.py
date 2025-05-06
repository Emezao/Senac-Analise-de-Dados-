# Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
#• Ter entre 16 e 69 anos.
#• Pesar mais de 50 kg.
#• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)
#Escreva um programa que, dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior

# Entrada dos Dados 
nome = input('informe o seu nome: ')
idade  = float(input('informe a sua idade: '))
peso = float(input('informe seu peso em kg: ')) 
descanso = float(input('informe o tempo de descando em horas: '))

# Processando os dados

if (idade >= 16 and idade <=69) and peso>= 50 and descanso>=6:
 print('voce esta apto a doar')
   
else:
 
 print(f'infelizmente {nome}, você não pode doar.')


