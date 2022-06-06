pessoas = []
dados = []

maiorPeso = 0
pessoaPesada = []
menorPeso = 9999
pessoaLeve = []
while True:
    dados.append(str(input('Digite o Nome: ')))
    dados.append(int(input('Digite a peso: ')))
    pergunta = str(input('Deseja continuar [S/N]? '))
    pessoas.append(dados[:])
    dados.clear()
    if pergunta in 'Nn':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
for p in pessoas:
    if p[1] >= maiorPeso:
        maiorPeso = p[1]
    if p[1] <= menorPeso:
        menorPeso = p[1]
print(f'Maior peso foi {maiorPeso}. Peso de: ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'Menor peso foi {menorPeso}. Peso de: ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')