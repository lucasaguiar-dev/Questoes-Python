def contador():
    c = 1
    print('-=' * 20)
    print(f'Contagem de 1 até 10 de 1 em 1')
    while c <= 10:
        print(c, end=' ')
        c += 1
        if c == 11:
            print('FIM!')
    print('-=' * 20)
    c = 10
    print(f'Contagem de 10 até 0 de 2 em 2')
    while c >= 0:
        print(c, end=' ')
        c -= 2
        if c == -2:
            print('FIM!')
    print('-=' * 20)


def contador2():
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p == 0:
        p += 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p > 0:
        if f > i:
            while i <= f:
                print(i, end=' ')
                i += p
        elif f < i:
            while i >= f:
                print(i, end=' ')
                i -= p
    else:
        if f > i:
            while i <= f:
                print(i, end=' ')
                i -= p
        elif f < i:
            while i >= f:
                print(i, end=' ')
                i += p
contador()
contador2()
