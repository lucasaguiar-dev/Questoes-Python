peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepreso')
elif 30 <= imc < 30:
    print('Obesidade')
else:
    print('Obesidade mórbida')
