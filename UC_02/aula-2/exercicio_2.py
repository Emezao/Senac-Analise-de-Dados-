# Script Utilizandos Listas
import pandas as pd
idade = pd.Series([5,8,12,15,18,19,25,35,22])
acima = idade[idade >= 18] 
abaixo = idade[idade < 18]
print('\n-- idades maiores ou iguais a 18 --')
print(acima.to_string(index=False))
print('\n -- idades menores que 18 --')
print(abaixo.to_string(index=False))