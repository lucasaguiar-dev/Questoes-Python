from random import randint

v = 0
while True:
    jogador = int(input('Agora escolha um número: '))
    c = randint(0, 10)
    soma = jogador + c
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]

    if escolha == 'P':
        if soma % 2 == 0:
            print(f'A maquina escolheu {c}, o resultado {soma} é par, você ganhou!')
            v += 1
        else:
            print(f'A maquina escolheu {c}, o resultado {soma} é impar, você perdeu!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print(f'A maquina escolheu {c}, o resultado {soma} é impar, você ganhou!')
            v += 1
        else:
            print(f'A maquina escolheu {c}, o resultado {soma} é par, você perdeu!')
            break
    print('Vamos jogar novamente...')
print(F'Game OVER! Você venceu {v} vezes')
