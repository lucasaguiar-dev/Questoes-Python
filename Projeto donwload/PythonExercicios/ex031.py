distancia = int(input('Digite a distância da viagem em Km: '))
if distancia<=200:
    print(f'O preço da passagem será {distancia*0.5}R$')
else:
    print(f'O preço da passagem será {distancia*0.45}R$')

