# Script Utilizandos Listas
import pandas as pd
notas = pd.Series([25,78,98,56,68,75,45,39,89,87])
acima = notas[notas >= 70] 
abaixo = notas[notas < 70]
print('\n-- Notas maiores ou iguais a 70 --')
print(acima)
print('\n -- Notas menores que 70 --')
print(abaixo)