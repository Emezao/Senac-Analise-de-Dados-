# Importando a Biblioteca
import pandas as pd

# Criando a Tabela Vendedor
vendedores = [
    ['Maria',800,700,1000,900,1200,600,600],
    ['João',900,500,1100,1000,900,500,700],
    ['Manoel',700,600,900,1200,900,700,400]
]

# Criando as Colunas da Tabela Vendedor
colunas = ['Nome','Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']

# Criando o DataFrame Vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Exibindo o DataFrame
print(df_vendedores)

# Criando as Métricas
soma_seg = df_vendedores['Segunda'].sum()
media_seg = df_vendedores['Segunda'].mean()
menor_seg = df_vendedores['Segunda'].min()
maior_seg = df_vendedores['Segunda'].max()
nome_vendedor_seg = df_vendedores[df_vendedores['Segunda'] == maior_seg]['Nome']
print(f'\nO Vendedor com Melhor Desempenho na Segunda-Feira foi {nome_vendedor_seg}')