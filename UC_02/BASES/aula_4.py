# Importando a Biblioteca
import pandas as pd 
import numpy as np 

# importando a Base de Dados

endereco_dados = 'Bases\Funcionarios.csv'

# Criando o dataFrame Funcionários
df_funcionarios = pd.read_csv(endereco_dados,sep=',', encoding='iso-8859-1')



print(df_funcionarios)