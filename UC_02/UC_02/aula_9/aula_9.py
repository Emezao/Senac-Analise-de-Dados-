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



# Correlação entre Roubo de Veiculo e Furto de Veiculo
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação

corr_roubo_furto_veiculo = np.corrcoef(df_roubo_furto_veiculo['roubo_veiculo'], df_roubo_furto_veiculo['furto_veiculos'])[0,1]
corr_furto_recuperacao_veiculo = np.corrcoef(df_furto_veiculo['furto_veiculos'],df_recuperacao_veiculo['recuperacao_veiculos'])[0,1]
corr_roubo_recuperacao_veiculo = np.corrcoef(df_roubo_veiculo['roubo_veiculo'],df_recuperacao_veiculo['recuperacao_veiculos'])[0,1]



# Exibindo as correlações
print(f"A correlação entre Roubo de Veiculo e Furto de Veiculo é {corr_roubo_furto_veiculo:.3f}")
print(f"A correlação entre Furto de Veiculo e Recuperação de Veiculo é {corr_furto_recuperacao_veiculo:.3f}")
print(f"A correlação entre Roubo de Veiculo e Recuperação de Veiculo é {corr_roubo_recuperacao_veiculo:.3f}")