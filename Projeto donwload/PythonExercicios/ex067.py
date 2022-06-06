n = 1
while True:
    n = int(input('Digite um número: '))
    c = 1
    if n >= 0:
        while c <= 10:
            print(f'{n} X {c} = {n * c}')
            c = c + 1
    else:
        break
print('Fim')
