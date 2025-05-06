# Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7


# Entrada dos Dados 
nome = input('informe o seu nome: ')
Altura  = float(input('informe a sua altura em metros: '))
sexo = input('informe seu sexo M para masculino f para feminino: ')

# Processamento dos Dados
if sexo == 'M' or sexo == 'm':
    h = (72.7*Altura) - 58
    print(f'Sr(a) {nome}, seu peso ideal é {h:.0f}')
elif sexo == 'F' or sexo == 'f':
    m = (62.1*Altura) - 44.7
    print(f'Sr(a) {nome}, seu peso ideal é {m:.0f}')
else:
    print('Verifique o sexo informado')



# Saída do Dados



#Contrução de estruturas de controle


