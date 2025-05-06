#- Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada.

# Entrada do Dados


distancia = float(input(' A distancia percorrida em KM é: '))
tempo = float(input('o Tempo percorrido é: '))

# Processando os dados 
velo_media = distancia/tempo

#saida de dados
print(f' A media de velocidade é: {velo_media:.2f}km/h')


# Consumo de litro de gasolina
#Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l, construa um programa que determine a quantidade de combustível gasto nessa viagem

# entrada dos dados

consumo = distancia*tempo/12
print(f'O consumo por litro é de: {consumo:.2f}km/l')