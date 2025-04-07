# Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.
import math
# Entrada de Dados

area = float(input("informe o tamanho da área a ser pintada em metros quadrados: "))


# Processamento de Dados
litros_necessarios = area / 3

latas_necesasarias = math.ceil(litros_necessarios / 18)

preco_total = latas_necesasarias * 130

print(f"\nQuantidade de latas a serem compradas: {latas_necesasarias}")
print(f"Valor total a ser pago: R${preco_total:.2f}")