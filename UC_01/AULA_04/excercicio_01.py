#- Escreva um programa que, dado 5 números inteiros calcule a soma deles e identifique o maior deles.


# Entrada dos dados
soma = 0
maior = 0
# Processamento de Dados - Estrutura de Repetição
for i in range(5):
    n = int(input('Informe um valor inteiro: '))
    if n > maior :
        maior = n 
    soma = soma + n 


# Saida de dados 
    print(f'A soma é {soma}')
    print(f'O maior valor encontrado foi {maior}')

