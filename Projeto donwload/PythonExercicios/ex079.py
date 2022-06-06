numeros = []

while True:
    n = (input('Digite um número ou escreva STOP para parar: '))
    if n == 'STOP':
        break
    else:
        if n in numeros:
            print('Esse número já esta na lista')
        else:
            numeros.append(n)
print(sorted(numeros))
