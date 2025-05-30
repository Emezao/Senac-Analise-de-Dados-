import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Crindo o DataFrame
roubo_veiculo   = endereco_dados   
df_roubo_veiculo = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando as variaveis de dados
df_roubo_veiculo = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_roubo_veiculo[['cisp','ano','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo[df_roubo_veiculo['ano'].between(2003,2024)]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo'])


# criando um array de roubo de veiculo
array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

# obtendo a media por ano de roubo de veiculo
media_roubo_veiculo = np.mean(array_roubo_veiculo)
# obtendo a mediana por ano de roubo de veiculo
mediana_roubo_veiculo = np.median(array_roubo_veiculo)
# Soma dos Roubo de Veiculo por ano
total_roubo_veiculo = df_roubo_veiculo['roubo_veiculo'].sum()
# obtendo o maior numero de roubo de veiculo por ano
ano_maior = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] == max(df_roubo_veiculo['roubo_veiculo'])].values[0]
# obtendo o menor numero de roubo de veiculo por ano
ano_menor = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] == min(df_roubo_veiculo['roubo_veiculo'])].values[0]
# obtendo a distancia entre a media e a mediana
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)    
# obtendo amplitude de roubo de veiculo 
amplitude_roubo_veiculo = max(df_roubo_veiculo['roubo_veiculo']) - min(df_roubo_veiculo['roubo_veiculo'])
# Obtendo os Quartis dos roubo de carga - Método weibull
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo
# obtendo os outliers do roubo de veiculo superiores
outliers_roubo_veiculo_inferior = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1_roubo_veiculo - 1.5 * iqr_roubo_veiculo]
outliers_roubo_veiculo_superior = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3_roubo_veiculo + 1.5 * iqr_roubo_veiculo]


# Exibindo os dados

print(df_roubo_veiculo)
print('\n ------------------------ Valores de Roubo de Veiculo ------------------------')
print(f'A media dos roubo de veiculo foi de {media_roubo_veiculo:.0f}')
print(f'A mediana dos roubo de veiculo foi de {mediana_roubo_veiculo:.0f}')
print(f'A soma dos roubo de veiculo foi de {total_roubo_veiculo:.0f}')
print(f'O maior numero de roubo de veiculo foi de {max(df_roubo_veiculo["roubo_veiculo"])} ')    
print(f'O menor numero de roubo de veiculo foi de {min(df_roubo_veiculo["roubo_veiculo"])} ')
print(f'A distancia entre a media e a mediana foi de {distancia_roubo_veiculo}')
print(f'A amplitude dos roubo de veiculo foi de {amplitude_roubo_veiculo:.0f}')
print(f'O primeiro quartil dos roubo de veiculo foi de {q1_roubo_veiculo:.00f}')  
print(f'O segundo quartil dos roubo de veiculo foi de {q2_roubo_veiculo:.00f}')  
print(f'O terceiro quartil dos roubo de veiculo foi de {q3_roubo_veiculo:.00f}')  
print(f'O intervalo interquartil dos roubo de veiculo foi de {iqr_roubo_veiculo:.0f}')
print(f' Outliers inferiores: {outliers_roubo_veiculo_inferior}')
print(f' Outliers superiores: {outliers_roubo_veiculo_superior}')

print('\n- Verificando a existência de outliers inferiores -')
if len(outliers_roubo_veiculo_inferior) == 0:
    print("Não existem outliers inferiores")
else:
    print(outliers_roubo_veiculo_inferior)
print('\n- Verificando a existência de outliers superiores -')
if len(outliers_roubo_veiculo_superior) == 0:
    print("Não existem outliers superiores")
else:
    print(outliers_roubo_veiculo_superior.sort_values(by='roubo_veiculo',ascending=False).head(5))