# Importando a Biblioteca
import pandas as pd

# Definindo a Função para Formatar
def formatar(valor):
    return "{:.2f}%".format(valor)

def visual(v):
    return "{:,.0f}".format(v)

# Criando as Séries
vacinas = pd.Series([30000000,25000000,10000000,5000000], index = ['2021','2022','2023','2024'])
populacao = pd.Series([213317639,214477744,215574303,216687971], index = ['2021','2022','2023','2024'])

tx_vacinacao = ((vacinas / populacao) * 100).apply(formatar)

total_tx_vacinacao = (vacinas.sum() / populacao.tail(1).iloc[0]) * 100

# Criando as Visualizações
print('\n-- DADOS DA POPULAÇÃO VACINADA POR ANO--')
print(vacinas.apply(visual))
print(f'O Acumulado de Pessoas Vacinadas foi: {vacinas.sum()}')
print(f'A Média de Pessoas Vacinadas foi: {vacinas.mean():.0f}')

print('\n-- DADOS DA POPULAÇÃO POR ANO --')
print(populacao.apply(visual))
print(f'O Acumulado de Pessoas é: {populacao.tail(1).iloc[0]}')
print(f'A Média de Pessoas é: {populacao.mean():.0f}')

print('\n-- PERCENTUAL DE PESSOAS VACINADAS POR ANO --')
print(tx_vacinacao)

print(f'\n O Percentual de Pessoas Vacinadas nos Últimos 4 anos foi de: {total_tx_vacinacao:.2f}%')
