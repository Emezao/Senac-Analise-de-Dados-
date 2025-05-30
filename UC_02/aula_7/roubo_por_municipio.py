# base da dados de roubo de cargas por municipio

import pandas as pd 
import numpy as np 

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' 
df_ipsrj = pd.read_csv(endereco_dados)  
# Criando as colunas de roubo de cargas
df_ipsrj = pd.read_csv(endereco_dados,sep=';',encoding='cp1252')
df_ipsrj_roubo = df_ipsrj[['ano','roubo_carga']]
df_ipsrj_roubo = df_ipsrj_roubo[df_ipsrj_roubo['ano'].between(2003,2025)]
df_ipsrj_roubo = df_ipsrj_roubo.groupby(['ano']).sum(['roubo_carga']).reset_index()

# Obtendo os valores de media, mediana e amplitude
media = df_ipsrj_roubo['roubo_carga'].mean()
mediana = df_ipsrj_roubo['roubo_carga'].median()
amplitude = max(df_ipsrj_roubo['roubo_carga']) - min(df_ipsrj_roubo['roubo_carga'])
desvio_padrao = np.std(df_ipsrj_roubo['roubo_carga'])




# obetendo outliers do numeros de roubos
q1 = np.quantile(df_ipsrj_roubo['roubo_carga'], 0.25,method='weibull')
q2 = np.quantile(df_ipsrj_roubo['roubo_carga'], 0.50,method='weibull')
q3 = np.quantile(df_ipsrj_roubo['roubo_carga'], 0.75,method='weibull')
iqr = q3 - q1
# Anos com maior e menos numero de roubos   
ano_maior = df_ipsrj_roubo[df_ipsrj_roubo['roubo_carga'] == max(df_ipsrj_roubo['roubo_carga'])]['ano'].values[0]
ano_menor = df_ipsrj_roubo[df_ipsrj_roubo['roubo_carga'] == min(df_ipsrj_roubo['roubo_carga'])]['ano'].values[0]

# Mostrandos os Dados    
print(df_ipsrj_roubo)
print('\n-------------- Roubo de Cargas --------------')
print(f' O total de roubo de cargas foi de entre os anos de 2003 e 2025: {df_ipsrj_roubo["roubo_carga"].sum()}')
print(f' A media de roubo de cargas foi de: {media:.0f}')
print(f' A mediana de roubo de cargas foi de: {mediana}')
print(f' A amplitude de roubo de cargas foi de: {amplitude}')
print(f' O desvio padrão de roubo de cargas foi de: {desvio_padrao:.0f}')
print(f' O maior numero de roubo de cargas foi de: {max(df_ipsrj_roubo["roubo_carga"])} no ano de {ano_maior}')    
print(f' O menor numero de roubo de cargas foi de: {min(df_ipsrj_roubo["roubo_carga"])} no ano de {ano_menor}')
print('\n-------------- Valores de Outliers --------------')
print(f' O primeiro quartil de roubo de cargas foi de: {q1:.00f}')  
print(f' O segundo quartil de roubo de cargas foi de: {q2:.00f}')  
print(f' O terceiro quartil de roubo de cargas foi de: {q3:.00f}')  
print(f' O intervalo interquartil de roubo de cargas foi de: {iqr}')
print('\n-------------- Grafico de Roubo de Cargas por Ano --------------')

