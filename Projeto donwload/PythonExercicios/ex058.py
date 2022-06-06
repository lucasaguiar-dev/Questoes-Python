from random import randint
from time import sleep
contador = 0
pessoa = 0
computador = (randint(1, 10))
while pessoa != computador:
    pessoa = int(input('Tente adivinhar o número que a máquina está pensando: '))
    print('Processando..')
    sleep(1)
    contador += 1
    if pessoa != computador:
        print(f'Você errou! Tente novamente!')
    else:
        print(f'A máquina pensou em {computador}! Você acertou!')
        print(f'Você acertou o número pensado pela máquina, depois de {contador} tentativas!')


