#Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E

# Entrada dos Dados
prova =  []
gabarito = ["A","B","B","D","E"]
acerto = 0 
erro = 0 
n = 1

# Processamento dos Dados
for i in range(5):
    prova.append(input(f'Informe a alternativa da {n}a. questao: '))
    n += 1    
for i in range(len(prova)):
      if prova[i].upper() == gabarito[i]:
        acerto += 1 
      else:
          erro += 1


# Saída dos Dados
print("\n As alternativas informadas foram")
print(prova)
print('\n As alternativas corretas são')
print(gabarito)
print(f'Portando você acertou {acerto}questões e errou {erro} questões.')