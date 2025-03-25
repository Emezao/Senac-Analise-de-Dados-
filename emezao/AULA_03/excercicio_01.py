#Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.
#Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.


# Entrada de Dados 

n1 = int(input('Informe o Primeiro Valor: '))
n2 = int(input('Informe o Segundo Valor: '))

# Processamento de dados 
if n1 == n2:
    print(f'Eles são iguais, portando a soma vale {n1+n2}')
else:
    print(f'Eles são diferentes, portanto o produto vale {n1*n2}')

