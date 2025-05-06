#2- Escreva um programa que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula: 

#valorfinal = prestacao+(prestacao*(taxa/100)*tempo)


# Entrada do Dados
prestacao = float(input('informe o valor da prestaçao: '))
taxa = float(input('informe a porcentagem da taxa: '))
tempo = int(input('informe o atraso em dias: '))

# Processamento dos Dados
juros = prestacao*(taxa/100)*tempo
valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

# Saida dos Dados
print(f'As prestaçoes se encontra {tempo} dias atrasada, gerando juros de {juros:.2f}, portando o valor final a ser pago será de R$ {valorfinal:,.2f}')