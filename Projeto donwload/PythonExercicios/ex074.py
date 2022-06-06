from random import randint
numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os números gerados foram {numeros}')
ordemNumeros = sorted(numeros)
print(f'O maior número foi {ordemNumeros[4]} e o menor foi {ordemNumeros[0]}')
