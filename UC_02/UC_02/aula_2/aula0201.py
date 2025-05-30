# Script Utilizandos Listas
notas = [25,78,98,56,68,75,45,39,89,87]
acima = [] 
abaixo = []

for i in range (len(notas)):
    if notas[i] >= 70:
        acima.append(notas[i])
    else:
        abaixo.append(notas[i])    

print('\n-- Notas maiores ou iguais a 70 --')
print(acima)
print('\n -- Notas menores que 70 --')
print(abaixo)