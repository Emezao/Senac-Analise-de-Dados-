

import pandas as pd
# Importando a Base de Dados
endereco_dados = 'BASES\Titanic.csv'
# Carregar o arquivo CSV com delimitador ';'
df_titanic = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Criar o array com as idades, ignorando valores ausentes
idades = df_titanic['Age'].dropna().values

# Exibir o array
print(idades)

