# Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7


# Entrada dos Dados 
Altura  = float(input('informe a sua altura em metros: '))

# Processamento dos Dados
h = (72.7*Altura) - 58
m = (62.1*Altura) - 44.7

# Saída do Dados

print(f'O peso idela para homens é: {h:.0f} Kg')
print(f'O peso idela para mnulheres é: {m} Kg')