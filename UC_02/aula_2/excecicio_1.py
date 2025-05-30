# Excercicio series pandas
import pandas as pd

numeros1 = pd.Series([1,2,3,4,5,6,7,8,9,10])
numeros2 = pd.Series([11,12,13,14,15,16,17,18,19,20])
soma = numeros1 + numeros2
subtracao = numeros1 - numeros2
multiplicacao = numeros1*numeros2
divisao = numeros1/numeros2

print('\n-- A soma dos numeros são: --')
print(soma)
print('\n -- A subtração dos numeros: --')
print(subtracao)
print('\n-- A multiplicação dos numeros são: --')
print(multiplicacao)
print('\n -- A divisão dos numeros: --')
print(divisao)