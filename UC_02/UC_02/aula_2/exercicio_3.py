#3- O Delegado responsável pela Delegacia de roubos e furtos de automóveis, entrou em contato com você e te solicitou um auxílio, para obter duas informações: - A quantidade de roubos de automóveis + furto de automóveis diária, dos últimos 7 dias. - A taxa de recuperação de automóveis diária, dos últimos 7 dias, sabendo que para se chegar a esse número, deve-se dividir a quantidade de recuperação de automóveis pela quantidade de roubo de automóveis. Ele te enviou os seguintes dados:
# ● Roubo de automóveis: 100,90,80,120,110,90,70
# ● Furto de automóveis: 80,60,70,60,100,50,30
# ● Recuperação de automóveis: 70,50,90,80,100,70,50

import pandas as pd

def formatar(valor):
        return"{:.2f}%".format(valor)

roubo = pd.Series([100,90,80,120,110,90,70], index = ['segunda', 'terça', 'quarta', 'quinta','sexta','sabado','domingo'])
furto = pd.Series([80,60,70,60,100,50,30], index = ['segunda', 'terça', 'quarta', 'quinta','sexta','sabado','domingo'])
recuperacao = pd.Series([70,50,90,80,100,70,50], index = ['segunda', 'terça', 'quarta', 'quinta','sexta','sabado','domingo'])

soma = roubo + furto
divisao = recuperacao / roubo

tx_rec = ((recuperacao / roubo) * 100).apply(formatar)

print('\n-- A Roubos e furtos dos automóveis são: --')
print(soma)
print('\n -- Relação de Recuperação e de roubos diarios dos automóveis: --')
print(tx_rec)
