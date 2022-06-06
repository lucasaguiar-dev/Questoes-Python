def area(larg, comp):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


print('Controle de terrenos'.center(25))
print('-' * 26)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
