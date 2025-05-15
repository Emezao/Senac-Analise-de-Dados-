# Importando a Biblioteca
import pandas as pd

# Criando as Séries
maria = pd.Series([800,700,1000,900,1200,600,600], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
joao = pd.Series([900,500,1100,1000,900,500,700], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
manoel = pd.Series([700,600,900,1200,900,700,400], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])

# Criando as Visualizações
print('\n ------ Vendedora Maria ------')
print(maria)
print(f'\nO Total Vendido foi: {maria.sum()}')
print(f'A Média Vendida foi: {maria.mean():.0f}')
print(f'O Menor Valor Vendido foi: {maria.min()}')
print(f'O Maior Valor Vendido foi: {maria.max()}')

print('\n ------ Vendedor João ------')
print(joao)
print(f'\nO Total Vendido foi: {joao.sum()}')
print(f'A Média Vendida foi: {joao.mean():.0f}')
print(f'O Menor Valor Vendido foi: {joao.min()}')
print(f'O Maior Valor Vendido foi: {joao.max()}')

print('\n ------ Vendedor Manoel ------')
print(manoel)
print(f'\nO Total Vendido foi: {manoel.sum()}')
print(f'A Média Vendida foi: {manoel.mean():.0f}')
print(f'O Menor Valor Vendido foi: {manoel.min()}')
print(f'O Maior Valor Vendido foi: {manoel.max()}')