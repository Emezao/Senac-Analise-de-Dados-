#Programa Média



#Entrada de dados tudo que for uma variavel de dados. 

nome = input('Informe o nume do estudante: ')
n1 = float(input(f'informe a primeira nota do estudande {nome}: '))
n2 = float(input(f'informe a segunda nota do estudande {nome}: '))
n3 = float(input(f'informe a terceira nota do estudante {nome}: '))

# Processamento de Dados 
media = (n1+n2+n3)/3

#saida dos dados 
print(f'Sr(a) {nome} A sua média foi:{media:.1f}') #f string serve para criar mascara.