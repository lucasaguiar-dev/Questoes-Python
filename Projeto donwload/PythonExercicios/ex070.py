import math

nome = maisbarato = ''
preco = total = maiorque1000 = 0
barato = math.inf

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    total += preco
    if preco > 1000:
        maiorque1000 += 1
    if preco < barato:
        barato = preco
        maisbarato = nome
    if resposta == 'N':
        break
print(f'''A) O total gasto na compra foi R$ {total}
B) {maiorque1000} produtos custam mais de R$ 1000
C) O nome do produto mais barato é {maisbarato}''')
