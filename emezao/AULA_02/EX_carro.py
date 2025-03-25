#Entrada dos dados  
cm = 12    
d = int(input('Informe a distancia percorrida (km): '))
t = float(input("Informe o tempo de viagem (Horas): "))

# Processamento de Dados 

vm = d / t 
l = d / cm

# Saida dos Dados

print(f'A velociade média do veiculo foi {vm:.1f} km/h')
print(f'A quantidade gasta de combustivel foi {1:.1f} litros')

