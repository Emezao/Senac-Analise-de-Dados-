# Importando bibliotecas panda
import pandas as pd


# Criando função 

# format (valor)
#criando tabela vendedor 


df_municipios = [ 
['Rio de Janeiro',6775561,35000], 
['Niteroi',515317,2500], 
['São Gonçalo',1091737,15000], 
['Duque de Caxias',924624,12000], 
['Nova Iguaçu',821128,10000], 
['Belford Roxo',513118,9000], 
['São João de Meriti',471906,8500], 
['Petrópolis',306678,1000], 
['Volta Redonda',273988,2000], 
['Campos dos Goytacazes',507548,4000], 
]


#criandos as colunas da tabela roubos

colunas = ['Município','População','Roubos']
ocorrencias = ['Município','População','Roubos']
# criando o dataframe roubos
df_municipios = pd.DataFrame(df_municipios,columns=colunas)
#df_ocorrencia = pd.DataFrame(ocorrencias,columns=ocorrencias)

# Realizando as Métricas Solicitadas
soma_roubos = df_municipios['Roubos'].sum()
media_roubos = df_municipios['Roubos'].mean()
media_populacao = df_municipios['População'].mean()
soma_populacao = df_municipios['População'].sum()
maior_populacao = df_municipios['População'].max()
menor_populacao = df_municipios['População'].min()
maior_roubos = df_municipios['Roubos'].max()
menor_roubos = df_municipios['Roubos'].min()
melhor_municipio = df_municipios[df_municipios['Roubos'] == menor_roubos]
pior_municipio = df_municipios[df_municipios['Roubos'] == maior_roubos]
taxa_roubos = ((soma_roubos/soma_populacao)) * 100
# Exibindo o Dataframe Vendedores
print('\n -------- Tabela Municípios -----------')
print(df_municipios)
# Exibindo o Dataframe Vendedores
print('\n -------- Tabela Municípios -----------')
print(df_municipios)
print('\n ----------- Medidas Descritivas  ------------------')
print(f'A quantidade total de Roubos no Estado foi {soma_roubos}')
print(f'A quantidade média de Roubos no Estado foi {media_roubos}')
print(f'A média de roubos por município é {media_roubos}')
print(f'O maior números de roubos em municípios encontrada foi {pior_municipio}')
print(f'O menor número de roubos encontrada foi {melhor_municipio}')
print(f'A soma da população no Estado é de {soma_populacao} habitantes')
print(f'A maior população no Estado é de {maior_populacao} habitantes')
print(f'A menor população no Estado é de {menor_populacao} habitantes')
print(f'A taxa de roubos no Estado é de {taxa_roubos:0f}')