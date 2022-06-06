valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite em quantos anos vai pagar: '))
prestacaoMensal = valorCasa/(anos*12)

if prestacaoMensal <= salario * 0.3:
    print(f'Empréstimo aprovado!, o valor da parcela será {prestacaoMensal}R$')
else:
    print('Empréstimo negado!')
