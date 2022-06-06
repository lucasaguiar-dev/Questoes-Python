velocidade = float(input('Digite a velocidade do carro: '))
if velocidade>80:
    valorMulta = 7 * (velocidade - 80)
    print(f'O carro foi multado em {valorMulta}R$')
else:
    print('O carro não foi multado')
