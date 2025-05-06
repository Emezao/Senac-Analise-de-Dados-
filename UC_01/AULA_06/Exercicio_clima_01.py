# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.

# Entrada dos Dados

temperatura = [10,22,36,24,40,13,17,19,25,31,27]



# Processamento de Dados

maior = max(temperatura)
menor = min(temperatura)
media = sum(temperatura)/ len(temperatura)


# Saida dos Dados
print(f'A temperaturas são: {temperatura}ºc')
print(f'O maior temperatura é: {maior}ºc')
print(f'O menor temperatura é: {menor}ºc')

print(f'A média das temperaturas é {media}ºc')


