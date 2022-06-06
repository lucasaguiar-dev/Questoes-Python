def aumentar(p=0, t=0, formato=False):
    res = p + (p * t / 100)
    return res if formato is False else moeda(res)


def diminuir(p=0, t=0, formato=False):
    res = p - (p * t / 100)
    return res if formato is False else moeda(res)


def dobro(p=0, formato=False):
    res = p * 2
    return res if not formato else moeda(res)


def metade(p=0, formato=False):
    res = p / 2
    return res if not formato else moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def resumo(p=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t\t{moeda(p)}')
    print(f'Dobro do preço: \t\t{dobro(p, True)}')
    print(f'Metade do preço: \t\t{metade(p, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t\t{diminuir(p, taxar, True)}')
    print('-' * 30)