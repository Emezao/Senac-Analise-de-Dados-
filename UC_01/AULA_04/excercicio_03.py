# Praticando
# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule
# a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes
# condições:
# Se a média for maior igual a 70 -> ATENDIDO
# Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# Se a média for menor que 30 -> NÃO ATENDIDO


# Entrada do Dados
for i in range(3):
    aluno = input('Informe o nome do aluno: ')
    notas_1 = float(input(f'Informe a primeira nota do {aluno}: '))
    nota_2 = float(input(f' Informe a segunda nota do {aluno}: '))

    media = (notas_1 + nota_2) / 2 

# Processamento de dados 


    if media > 70:
        print(f"Antedido")
    elif media   >= 30  < 70:
     print(f'Parcialmente atendido')
    else: 
     print(f' Não atendido')

# Saida dos dados

print(f'A média do aluno {aluno} é {media}, portanto está')