# Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.

# Entrada de Dados

tinta_18l = 130,00
tinta_1l = 3
n = 1


# Processamento de Dados
metros = int(input('Informe em metros a área a ser pintada: ')) 
Latas_tinta = metros + (tinta_18l*tinta_1l)

print(f"compra ficou em R$: {Latas_tinta}")