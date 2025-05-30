# Criando base da dados da Segurança pública do RJ

# Importando a Biblioteca
import pandas as pd 
import numpy as np 

# Importando a Base de Dados    
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' 
df_ipsrj = pd.read_csv(endereco_dados)  

df_ipsrj = pd.read_csv(endereco_dados,sep=';',encoding='utf-8')
df_ipsrj_homicidios = df_ipsrj[['ano','hom_doloso']]
df_hom_doloso = df_ipsrj_homicidios[df_ipsrj_homicidios['ano'].between(2003,2025)]
df_hom_doloso = df_ipsrj_homicidios.groupby(['ano']).sum(['hom_doloso']).reset_index()

# Separando os dados por Município  
df_ipsrj = df_ipsrj[df_ipsrj['munic'] == 'Rio de Janeiro']

# Obetendo valores de media, mediaana e amplitude
media = df_ipsrj['hom_doloso'].mean()
mediana = df_ipsrj['hom_doloso'].median()
amplitude = max(df_ipsrj['hom_doloso']) - min(df_ipsrj['hom_doloso'])
desvio_padrao = np.std(df_ipsrj['hom_doloso'])

# Total de Homicidios Dolosos
total_hom_doloso = df_ipsrj['hom_doloso'].sum()

# percentual de homicidios por ano de 2003 a 2025 maior que zero
#percentual = (df_ipsrj[df_ipsrj['hom_doloso'] > 0]['hom_doloso'].sum() / df_ipsrj['hom_doloso'].sum()) * 100
df_ipsrj = df_ipsrj[df_ipsrj['ano'] >= 0]

#   obtendo o ano com maior e com menor numero de homicidos total por ano
ano_maior = df_ipsrj[df_ipsrj['hom_doloso'] == max(df_ipsrj['hom_doloso'])]['ano'].values[0]
ano_menor = df_ipsrj[df_ipsrj['hom_doloso'] == min(df_ipsrj['hom_doloso']>0)]['ano'].values[0]


# obetendo a amplitude dos homicidios
amplitude = max(df_ipsrj['hom_doloso']) - min(df_ipsrj['hom_doloso'])

# Obtendo valores de outliers
q1 = np.quantile(df_ipsrj['hom_doloso'], 0.25,method='weibull')
q2 = np.quantile(df_ipsrj['hom_doloso'], 0.50,method='weibull')
q3 = np.quantile(df_ipsrj['hom_doloso'], 0.75,method='weibull')
iqr = q3 - q1
 








#   Exibindo a base de dados
print(df_ipsrj)
print(df_hom_doloso)
print(f'\n-------------- Homicídios Dolosos por Ano --------------')
print(f' O total de homicídios dolosos foi de entre os anos de 2003 e 2025: {total_hom_doloso}')
print(f' A media de homicídio doloso foi de: {media:.0f}')
print(f' A mediana de homicídio doloso foi de: {mediana}')
print(f' A amplitude de homicídio doloso foi de: {amplitude}')
print(f' O desvio padrão de homicídio doloso foi de: {desvio_padrao:.0f}')
print(f'\n-------------- Valores de Outliers --------------')
print(f' O primeiro quartil de homicídio doloso foi de: {q1:f}')  
print(f' O segundo quartil de homicídio doloso foi de: {q2:f}')  
print(f' O terceiro quartil de homicídio doloso foi de: {q3:f}')  
print(f' O iqr de homicídio doloso foi de: {iqr}')
print(f' O limite superior dos quartis de homicídio doloso foi de: {q3 + (1.5 * iqr)}')
print(f' O limite inferior dos quartis de homicídio doloso foi de: {q1 - (1.5 * iqr)}')
print(f' O ano com maior numero de homicídios dolosos foi de: {max(df_ipsrj["hom_doloso"])} no ano de {ano_maior}')    
print(f' O ano com menor numero de homicídios dolosos foi de: {min(df_ipsrj["hom_doloso"])} no ano de {ano_menor}')
print(f' A amplitude dos homicídios dolosos foi de: {amplitude}')

