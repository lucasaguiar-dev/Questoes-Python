f = input('Digite uma frase: ').replace(' ', '')
if f == f[::-1]:
    print('A frase é igual de trás pra frente')
else:
    print('A frase é diferente de trás pra frente')
