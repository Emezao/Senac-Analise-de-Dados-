num = [10,2,3,5,6,20,50,77,4,15] # criação de lista


# Operações matemáticas com base na lista
soma = sum(num) 
maior = max(num)
menor = min(num)
media = sum(num) / len(num)

# Print e ordenação de resultados sendo o primeiro do reverso.
pos = num.index(50)
num.sort(reverse=True)
print(num)
print(f"o item encontra se na posiçao:0 {pos}")
print(maior)
print(soma)
print(menor)
print(media)

