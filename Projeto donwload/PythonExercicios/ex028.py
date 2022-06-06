import random

num = int(input('tente adivinhar um número entre 0 e 5: '))
numSort = random.randint(0, 5)

if num==numSort:
    print('Você acertou o número')
else:
    print('Você errou o número')

print(f'O número sorteado foi {numSort} e o número adivinhado foi {num}')
