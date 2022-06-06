import math
from math import inf
n = 0
contador = 0
media = 0
soma = 0
r = ''
maior = 0
menor = math.inf
while r != 'N':
    n = int(input('Digite um número inteiro: '))
    contador += 1
    soma += n
    media = soma / contador
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = input(str('Deseja continuar a digitar valores? [S/N]: '))
print(f'A média entre os números digitados foi {media}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')


