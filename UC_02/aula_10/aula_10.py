# Praticando
# O Governador do Estado do Rio de Janeiro, necessita apresentar para a mídia números relativos aos
# crimes de Homicídio Doloso(hom_doloso) e Cuposo(hom_culposo) por Delegacias de Polícia(cisp), por isso
# entrou em contato com você e solicitou que fosse realizado uma série de análises.
# Tais como:
# - Um Ranking separado para as DPs com valores discrepantes de Homicídios Dolosos e Culposos.
# - A verificação da Hipótese de uma correlação positiva ou negativa entre os tipos de Homicídios.
# - A obtenção dos indicadores de coeficiente angular, intercepto e R².
# - Elaborar o gráfico de dispersão entre os tipos de Homicídios.
# - Visualização da Reta de Regressão, através do Gráfico de Regressão.



import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1') 

# criando o Dataframe homicidio doloso
df_hom_doloso = df_ocorrencias[['cisp','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['cisp']).sum(['hom_doloso']).reset_index()
# criando o Dataframe homicidio culposo
df_hom_culposo = df_ocorrencias[['cisp','hom_culposo']]
df_hom_culposo = df_hom_culposo.groupby(['cisp']).sum(['hom_culposo']).reset_index()
# Criando array de homicidios dolosos
array_hom_doloso = np.array(df_hom_doloso['hom_doloso'])
# Criando array de homicidios culposos
array_hom_culposo = np.array(df_hom_culposo['hom_culposo'])

# Obtendo uma media de homicidios dolosos 
media_hom_doloso = np.mean(array_hom_doloso)
# Obtendo uma media de homicidios culposos 
media_hom_culposo = np.mean(array_hom_culposo)
# obtendo a soma dos homicidios dolosos
soma_hom_doloso = np.sum(array_hom_doloso)
# obtendo a soma dos homicidios culposos
soma_hom_culposo = np.sum(array_hom_culposo)
# mediana dos homicidios dolosos
mediana_hom_doloso = np.median(array_hom_doloso)
# mediana dos homicidios culposos
mediana_hom_culposo = np.median(array_hom_culposo)
# distancia entre a media e mediana
distancia_hom_doloso = media_hom_doloso - mediana_hom_doloso
distancia_hom_culposo = media_hom_culposo - mediana_hom_culposo

# obtendo quartis de homicidio doloso
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

# obtendo quartis de homicidio culposo
q1_hom_culposo = np.quantile(array_hom_culposo, 0.25, method='weibull')
q2_hom_culposo = np.quantile(array_hom_culposo, 0.50, method='weibull')
q3_hom_culposo = np.quantile(array_hom_culposo, 0.75, method='weibull')
iqr_hom_culposo = q3_hom_culposo - q1_hom_culposo

# identificando os outliers do homicidio doloso
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)

# identificando os outliers do homicidio culposo
limite_superior_hom_culposo = q3_hom_culposo + (1.5 * iqr_hom_culposo)
limite_inferior_hom_culposo = q1_hom_culposo - (1.5 * iqr_hom_culposo)

# filtrando os dataframes dos outliers
df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]
df_hom_doloso_outliers_inferior = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]

df_hom_culposo_outliers_superiores = df_hom_culposo[df_hom_culposo['hom_culposo'] > limite_superior_hom_culposo]
df_hom_culposo_outliers_inferior = df_hom_culposo[df_hom_culposo['hom_culposo'] < limite_inferior_hom_culposo]

# verificandos a existencia de outliers inferiores para homicidio culposo
if len(df_hom_culposo_outliers_inferior) == 0:
    print("Nao existem outliers inferiores para homicidio culposo")
else:
    print(df_hom_culposo_outliers_inferior)

# verificandos a existencia de outliers inferiores para homicidio doloso
if len(df_hom_doloso_outliers_inferior) == 0:
    print("Nao existem outliers inferiores para homicidio doloso")
else:
    print(df_hom_doloso_outliers_inferior)

# verificandos a existencia de outliers superiores para homicidio culposo
if len(df_hom_culposo_outliers_superiores) == 0:
    print("Nao existem outliers superiores para homicidio culposo")
else:
    print(df_hom_culposo_outliers_superiores)

# verificandos a existencia de outliers superiores para homicidio doloso
if len(df_hom_doloso_outliers_superiores) == 0:
    print("Nao existem outliers superiores para homicidio doloso")
else:
    print(df_hom_doloso_outliers_superiores)

# Correlação entre Homicidio culposo e Doloso
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação
    
corr_hom_culposo_hom_doloso = np.corrcoef(df_hom_culposo['hom_culposo'], df_hom_doloso['hom_doloso'])[0,1]
corr_hom_doloso_hom_culposo = np.corrcoef(df_hom_doloso['hom_doloso'], df_hom_culposo['hom_culposo'])[0,1]

# medidas de disperção
variancia_hom_culposo = np.var(array_hom_culposo)
variancia_hom_doloso = np.var(array_hom_doloso)
desvio_padrao_hom_culposo = np.sqrt(variancia_hom_culposo)
desvio_padrao_hom_doloso = np.sqrt(variancia_hom_doloso)
coeficiente_variacao_hom_culposo = (desvio_padrao_hom_culposo / media_hom_culposo) * 100
coeficiente_variacao_hom_doloso = (desvio_padrao_hom_doloso / media_hom_doloso) * 100


# Visualizando os Dados Analisados
print('\n- Visualizando os Dados Analisados -')
plt.subplots(2,3,figsize=(16,7))
plt.suptitle('Análise dos Dados - Homicidios culposos e dolosos',fontsize=16)

# Posição 01: Gráfico dos Outliers dos Homicidios Dolosos
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso',ascending=True)
plt.subplot(2,3,1)
plt.title('Gráfico dos Outliers dos Homicidios dolosos')
plt.barh(df_hom_doloso_outliers_superiores_order['cisp'].astype(str),df_hom_doloso_outliers_superiores_order['hom_doloso'])

# Posição 02: Gráfico dos Outliers dos Homicidios Culposos
df_hom_culposo_outliers_superiores_order = df_hom_culposo_outliers_superiores.sort_values(by='hom_culposo',ascending=True)
plt.subplot(2,3,2)
plt.title('Gráfico dos Outliers dos Homicidios culposos')
plt.barh(df_hom_culposo_outliers_superiores_order['cisp'].astype(str),df_hom_culposo_outliers_superiores_order['hom_culposo'])

# Posição 03: histograma dos Homicidios Dolosos
plt.subplot(2,3,3)
plt.title('Histograma dos Homicidios Dolosos')
plt.hist(array_hom_doloso,bins=100,edgecolor='black')

# Posição 04: histograma dos Homicidios Culposos
plt.subplot(2,3,4)
plt.title('Histograma dos Homicidios Culposos')
plt.hist(array_hom_culposo,bins=100,edgecolor='black')



plt.savefig("relatório_hom_culposo_hom_doloso.png")
plt.show()