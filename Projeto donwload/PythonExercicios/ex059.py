a = 0
b = 0
c = 0
while c != 5:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print('''Selecione uma opção!
     [1] Somar 
     [2] Multiplicar 
     [3] Maior
     [4] Novos números
     [5] Sair do progama''')
    c = int(input('Qual a sua opção: '))
    if c == 1:
        print(f'O resultado  é {a + b}')
    elif c == 2:
        print(f'O resultado é {a * b}')
    elif c == 3:
        if a > b:
            print(a, 'É o maior')
        elif a == b:
            print('Os números são iguais')
        else:
            print(f'{b} É o maior número')
    elif c == 4:
        print('Digite novamente!')
    elif c == 5:
        print('Finalizando..')
    else:
        print('Opção inválida. Tente novamente!')
print('Programa finalizado!')