numeros = (int(input('Digite o primeiro valor: ')), int(input('Digite o primeiro valor: ')),
         int(input('Digite o primeiro valor: ')), int(input('Digite o primeiro valor: ')))
print(f'Você digitou os valores {numeros}')
repetidos = 0
print(f'O número nove apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'A posição que foi digitado o primeiro valor 3 foi {numeros.index(3)+1}')
else:
    print('O número 3 não foi digitado')

print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'[{n}', end=']')
