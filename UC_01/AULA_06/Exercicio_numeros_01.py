# Crie um programa que:
# 1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
# 2- Exiba a lista completa.
# 3- Exiba o maior e o menor número da lista.
# 4- Exiba a soma e a média de todos os números.

# Entrada dos Dados
num = []


# Processamento de Dados
for i in range(10):
    num.append(int(input('Informe um numero inteiro: ')))
maior = max(num)
menor = min(num)
soma = sum(num)
media = sum(num)/ len(num)


# Saida dos Dados
print(num)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(f'A soma dos números é {soma}')
print(f'A média dos números é {media}')


