# Entrada dos Dados 
nome = input('informe o seu nome: ')
idade  = float(input('informe a sua idade: '))
peso = float(input('informe seu peso em kg: ')) 
descanso = float(input('informe o tempo de descando em horas: '))

#outra soluçao de aplicar.

  
if idade>= 16 and idade <69:
    if peso >=50:
        if descanso>=6:
         print('voce esta apto a doar')

        else:
            print("voce nao esta apto a doar")
    else:
        print('voce nao esta apto a doar')

else:
 print("voce nao esta apto a doar")