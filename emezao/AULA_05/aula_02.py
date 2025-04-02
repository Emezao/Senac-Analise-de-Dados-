# Conntrua um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares e monstre o vetor principal na ordem inversa e depois na ordem crescente.

# Entrada dos Dados
n = 1
qtd_par = 0
qtd_impar = 0 
num = []

 




# Processamento dos Dados
for i in range(10):
    num.append(int(input(f"Informe o {n}º. valor: ")))
    n += 1 

    if n % 2 == 0:
        qtd_par += 1
    else:
        qtd_impar += 1 
     



# Saída do Dados
print(f"A quantiddade de números pares é {qtd_par}")
print(f"A quantiddade de números ímpares é {qtd_impar}")
num.reverse()
print('\nLista em ordem reversa')
print(num)
num.sort()
print('\nLista em ordem crescente')
print(num)