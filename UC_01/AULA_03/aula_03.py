#Contrução de estruturas de controle

#ENTRADA DE DADOS

idade = int(input('Digite sua idade :'))
print(idade)

if idade < 18:
    print ('você é menor de idade')
elif idade == 18:
    print('Você tem exatos 18 anos - Acesso Liberado') 
elif idade >= 65:
    print('Você tem mais de 65 anos - Acesso Liberato com cautela veio')
else: 
    print('Acesso liberado')

    
