numeros = []
while True:
    n = (input('Digite um número ou escreva STOP para parar: '))
    if n == 'STOP':
        break
    else:
        numeros.append(n)
if '5' in numeros:
    print('5 foi digitado')
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números'
      f'\nA lista de ordem descrescente é {numeros}')



