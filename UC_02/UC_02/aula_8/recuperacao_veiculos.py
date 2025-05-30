import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'


# Criando o DataFrame ocorrencias
recuperacao_veiculo = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
recuperacao_veiculo = recuperacao_veiculo[['cisp','recuperacao_veiculos']]
recuperacao_veiculo = recuperacao_veiculo.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()
recuperacao_veiculo = recuperacao_veiculo[recuperacao_veiculo['cisp'].between(2003,2024)]



# criando um array de recuperacao de veiculo
array_recuperacao_veiculo = np.array(recuperacao_veiculo['recuperacao_veiculos'])

# obtendo a media por ano de recuperacao de veiculo
media_recuperacao_veiculo = np.mean(array_recuperacao_veiculo)
# obtendo a mediana por ano de recuperacao de veiculo
mediana_recuperacao_veiculo = np.median(array_recuperacao_veiculo)
# Soma dos recuperacao de veiculo por ano
total_recuperacao_veiculo = recuperacao_veiculo['recuperacao_veiculos'].sum()
# obtendo o maior numero de recuperacao de veiculo por ano
ano_maior = recuperacao_veiculo[recuperacao_veiculo['recuperacao_veiculos'] == max(recuperacao_veiculo['recuperacao_veiculos'])]['recuperacao_veiculos'].values[0]
# obtendo o menor numero de recuperacao de veiculo por ano
ano_menor = recuperacao_veiculo[recuperacao_veiculo['recuperacao_veiculos'] == min(recuperacao_veiculo['recuperacao_veiculos'])]['recuperacao_veiculos'].values[0]

# obtendo a distancia entre a media e a mediana
distancia_recuperacao_veiculo = abs((media_recuperacao_veiculo - mediana_recuperacao_veiculo) / mediana_recuperacao_veiculo)    
# obtendo amplitude de recuperacao de veiculo 
amplitude_recuperacao_veiculo = max(recuperacao_veiculo['recuperacao_veiculos']) - min(recuperacao_veiculo['recuperacao_veiculos'])
# Obtendo os Quartis dos recuperacao de veiculo - Método weibull
q1_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.25, method='weibull')
q2_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.50, method='weibull')
q3_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.75, method='weibull')
iqr_recuperacao_veiculo = q3_recuperacao_veiculo - q1_recuperacao_veiculo
# obtendo os outliers do recuperacao de veiculo superiores
outliers_recuperacao_veiculo_inferior = recuperacao_veiculo[recuperacao_veiculo['recuperacao_veiculos'] < q1_recuperacao_veiculo - 1.5 * iqr_recuperacao_veiculo]
outliers_recuperacao_veiculo_superior = recuperacao_veiculo[recuperacao_veiculo['recuperacao_veiculos'] > q3_recuperacao_veiculo + 1.5 * iqr_recuperacao_veiculo]
# variância de recuperação de veiculo por ano
variancia_roubo_veiculo = np.var(array_recuperacao_veiculo)


# Exibindo os dados

print(recuperacao_veiculo)
print('\n ------------------------ Valores de Recuperacao de Veiculo ------------------------')
print(f'A media dos recuperacao de veiculo foi de {media_recuperacao_veiculo:.0f}')
print(f'A mediana dos recuperacao de veiculo foi de {mediana_recuperacao_veiculo:.0f}')
print(f'A soma dos recuperacao de veiculo foi de {total_recuperacao_veiculo:.0f}')

print(f'O maior numero de recuperacao de veiculo foi de {max(recuperacao_veiculo["recuperacao_veiculos"])} no ano de {ano_maior}')    
print(f'O menor numero de recuperacao de veiculo foi de {min(recuperacao_veiculo["recuperacao_veiculos"])} no ano de {ano_menor}')
print(f'A distancia entre a media e a mediana foi de {distancia_recuperacao_veiculo}')
print(f'A amplitude dos recuperacao de veiculo foi de {amplitude_recuperacao_veiculo:.0f}')
print(f'O primeiro quartil de 25% da recuperacao de veiculo foi de {q1_recuperacao_veiculo:.0f}')  
print(f'O segundo quartil de 50% da recuperacao de veiculo foi de {q2_recuperacao_veiculo:.0f}')  
print(f'O terceiro quartil de 75% da recuperacao de veiculo foi de {q3_recuperacao_veiculo:.0f}')  
print(f'O intervalo interquartil dos recuperacao de veiculo foi de {iqr_recuperacao_veiculo:.0f}')


print('\n- Verificando a existência de outliers inferiores -')
if len(outliers_recuperacao_veiculo_inferior) == 0:
    print("Não existem outliers inferiores")
else:
    print(outliers_recuperacao_veiculo_inferior)
print('\n- Verificando a existência de outliers superiores -')
if len(outliers_recuperacao_veiculo_superior) == 0:
    print("Não existem outliers superiores")
else:
    print(outliers_recuperacao_veiculo_superior.sort_values(by='recuperacao_veiculos',ascending=False).head(5))


# Visualizando os dados sobre os recuperação de veiculo
print('\n- Visualizando os dados sobre os recuperação de veiculo -')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre os recuperação de Veículos')

# posição 01: Gráfico de recuperaçao de Veículos
plt.subplot(2,2,1)
plt.title('Boxplot dos recuperação de Veículos')
plt.boxplot(array_recuperacao_veiculo,vert=False,showmeans=True)

# Posição 02: Histograma dos recuperação de Veículos
plt.subplot(2,2,2)
plt.title('Histograma de Recuperação de Veículos')
plt.hist(array_recuperacao_veiculo,bins=100,edgecolor='black')    

# Posição 03: Gráfico dos Outliers de recuperação de Veículos
outliers_recuperacao_veiculo_superior_order = outliers_recuperacao_veiculo_superior.sort_values(by='recuperacao_veiculos',ascending=True)
plt.subplot(2,2,3)
plt.title('Gráfico de Recuperação de Veículos')
plt.barh(outliers_recuperacao_veiculo_superior_order['cisp'].astype(str),outliers_recuperacao_veiculo_superior_order['recuperacao_veiculos'])

# Posição 04: Medidas Descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas de recuperação de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média de Recuperação de Veículos: {media_recuperacao_veiculo:.0f}')
plt.text(0.1,0.8,f'Mediana de Recuperação de Veículos: {mediana_recuperacao_veiculo:.0f}')
plt.text(0.1,0.7,f'Distância entre a Média e a Mediana de Recuperação de Veículos: {amplitude_recuperacao_veiculo}')
plt.text(0.1,0.6,f'Menor Valor de recuperação de Veículos: {ano_menor:.0f}')
plt.text(0.1,0.5,f'Maior Valor dos Recuperação de Veículos: {ano_maior:.0f}')
plt.text(0.1,0.4,f'O coeficiente de variação de Recuperação de veiculo é {variancia_roubo_veiculo:.2f}')
plt.text(0.1,0.3,f'A distância da variância de Recuperação de veiculos é, {distancia_recuperacao_veiculo:.2f}')

plt.show()