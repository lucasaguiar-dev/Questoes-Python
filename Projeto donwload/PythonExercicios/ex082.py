numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar [S/N] ? '))
    if resposta in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
