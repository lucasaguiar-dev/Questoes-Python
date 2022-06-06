def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número: ')
n2 = leiaFloat('Digite um número real: ')
print(f'{n1} e {n2}')
