
import pandas as pd

# Lendo o arquivo CSV com separador adequado
df_enem = pd.read_csv('ENEM_2014_2023.csv', sep=';', encoding='utf-8')

# Selecionando apenas os dados de interesse
df_enem = df_enem[['Estado','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']]

# Reorganizando a tabela: anos como linhas, estados como colunas
df_enem_reorganizado = df_enem.set_index('Estado').transpose()

# Exibindo a nova tabela
print(df_enem_reorganizado)

