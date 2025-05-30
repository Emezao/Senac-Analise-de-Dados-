import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando o DataFrame Roubo de Veiculo
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

# Criando o DataFrame Furto de Veiculo
df_furto_veiculo = df_ocorrencias[['cisp','furto_veiculos']]
df_furto_veiculo = df_furto_veiculo.groupby(['cisp']).sum(['furto_veiculos']).reset_index()

# Criando o DataFrame Recuperação de Veiculo
df_recuperacao_veiculo = df_ocorrencias[['cisp','recuperacao_veiculos']]
df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()

# Criando o DataFrame Roubo e Furto de Veiculo
df_roubo_furto_veiculo = df_ocorrencias[['cisp','roubo_veiculo','furto_veiculos']]
df_roubo_furto_veiculo = df_roubo_furto_veiculo.groupby(['cisp']).sum(['roubo_veiculo','furto_veiculos']).reset_index()

# Criando arrays para a correlação
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])
array_furto_veiculo = np.array(df_furto_veiculo["furto_veiculos"])
array_recuperacao_veiculo = np.array(df_recuperacao_veiculo["recuperacao_veiculos"])

# obtendo os quartis de roubos de veiculos e furto de veiculos
q1_roubo_veiculo = np.quantile(array_roubo_veiculo,0.25)
q2_roubo_veiculo = np.quantile(array_roubo_veiculo,0.50)
q3_roubo_veiculo = np.quantile(array_roubo_veiculo,0.75)

q1_furto_veiculo = np.quantile(array_furto_veiculo,0.25)
q2_furto_veiculo = np.quantile(array_furto_veiculo,0.50)
q3_furto_veiculo = np.quantile(array_furto_veiculo,0.75)

q1_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo,0.25)
q2_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo,0.50)
q3_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo,0.75)

iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo
iqr_furto_veiculo = q3_furto_veiculo - q1_furto_veiculo
iqr_recuperacao_veiculo = q3_recuperacao_veiculo - q1_recuperacao_veiculo

# Obtendo os outliers superiores
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_superior_furto_veiculo = q3_furto_veiculo + (1.5 * iqr_furto_veiculo)
limite_superior_recuperacao_veiculo = q3_recuperacao_veiculo + (1.5 * iqr_recuperacao_veiculo)

# Obtendo os outliers inferiores
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)
limite_inferior_furto_veiculo = q1_furto_veiculo - (1.5 * iqr_furto_veiculo)
limite_inferior_recuperacao_veiculo = q1_recuperacao_veiculo - (1.5 * iqr_recuperacao_veiculo)




# Correlação entre Roubo de Veiculo e Furto de Veiculo
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação

corr_roubo_furto_veiculo = np.corrcoef(df_roubo_furto_veiculo['roubo_veiculo'], df_roubo_furto_veiculo['furto_veiculos'])[0,1]
corr_furto_recuperacao = np.corrcoef(df_furto_veiculo['furto_veiculos'],df_recuperacao_veiculo['recuperacao_veiculos'])[0,1]
corr_roubo_recuperacao = np.corrcoef(df_roubo_veiculo['roubo_veiculo'],df_recuperacao_veiculo['recuperacao_veiculos'])[0,1]





print(f"A correlação entre Roubo de Veiculo e Furto de Veiculo é {corr_roubo_furto_veiculo:.3f}")
print(f"A correlação entre Furto de Veiculo e Recuperação de Veiculo é {corr_furto_recuperacao:.3f}")
print(f"A correlação entre Roubo de Veiculo e Recuperação de Veiculo é {corr_roubo_recuperacao:.3f}")


