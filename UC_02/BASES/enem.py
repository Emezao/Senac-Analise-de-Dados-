import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')    

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\ENEM_2014_2023.csv'

# Criando o DataFrame financeira
df_enem = pd.read_csv(endereco_dados,sep=';',encoding='utf-8')


# Criandos estatisticas dos participantes com media, emediana e distancia entre média e mediana
maximo_enem_participantes = max(df_enem[['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']])
minimo_enem_participantes = min(df_enem[['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']])
array_enem_participantes = np.array(df_enem[['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']])
media_enem_participantes = np.mean(array_enem_participantes)
mediana_enem_participantes = np.median(array_enem_participantes)
distancia_enem_participantes = abs((media_enem_participantes - mediana_enem_participantes) / mediana_enem_participantes)
#array_total_enem_participantes = np.array(df_enem[['Total']])

# Obtendo os quartis dos participantes
q1_enem_participantes = np.quantile(array_enem_participantes, 0.25,method='weibull')
q2_enem_participantes = np.quantile(array_enem_participantes, 0.50,method='weibull')
q3_enem_participantes = np.quantile(array_enem_participantes, 0.75,method='weibull')
iqr_enem_participantes = q3_enem_participantes - q1_enem_participantes



# Limites dos quartis
limite_superior_enem_participantes = q3_enem_participantes + (1.5 * iqr_enem_participantes)
limite_inferior_enem_participantes = q1_enem_participantes - (1.5 * iqr_enem_participantes)




# Criando o array do valor total
array_enem_total = np.array(df_enem["Total"])

# Obtendo a média do valor total
media_total = np.mean(array_enem_total)

# Obtendo a mediana do valor total
mediana_total = np.median(array_enem_total)

# Obtendo a distância entre a média e a mediana do valor total
distancia_total = abs((media_total - mediana_total) / mediana_total)

# Obtendo o menor valor total
minimo_total = np.min(array_enem_total)

# Obtendo o maior valor total
maximo_total = np.max(array_enem_total)

# Obtendo os dados sobre os estados com maiores e menores inscritos
estado_maior = df_enem[df_enem['Total'] == maximo_total]['Estado'].values[0]
estado_menor = df_enem[df_enem['Total'] == minimo_total]['Estado'].values[0]
percentual_total = ((maximo_total - minimo_total) / minimo_total) * 100

# Exibindo a base de dados financeira    
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_enem)
print(f'\n-- OBTENDO INFORMAÇÕES SOBRE O ENEM   --')
#print(f'total de participantes foi {array_enem_participantes:.0f}')
print(f"A media dos participantes foi {media_enem_participantes:.0f}")
print(f"A mediana dos participantes foi {mediana_enem_participantes:.2f}")
print(f"A distancia entre a media e a mediana dos participantes foi {distancia_enem_participantes:.0f}")
print(f"O primeiro quartil dos participantes foi {q1_enem_participantes:.0f}")
print(f"O segundo quartil dos participantes foi {q2_enem_participantes:.0f}")
print(f"O terceiro quartil dos participantes foi {q3_enem_participantes:.0f}")
print(f"O iqr dos participantes foi {iqr_enem_participantes:.0f}")
print(f"O limite superior dos quartis dos participantes foi {limite_superior_enem_participantes:.0f}")
print(f"O limite inferior dos quartis dos participantes foi {limite_inferior_enem_participantes:.0f}")
print(f"O maior valor dos participantes foi {maximo_total:.0f}")
print(f"O menor valor dos participantes foi {minimo_total:.0f}")
print(f'\nO estado com a maior quantidade de inscritos na série histórica é {estado_maior}')
print(f'O estado com a menor quantidade de inscritos na série histórica é {estado_menor}')
print(f'O percentual de inscritos no estado de {estado_maior} em relação ao estado de {estado_menor} é {percentual_total:.0f}%')