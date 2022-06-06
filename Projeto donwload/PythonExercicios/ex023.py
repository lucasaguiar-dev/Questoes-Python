num = input('Digite um número entre 0 e 9999: ')
numSeparado = num.replace('', ' ')
numSeparado = (numSeparado.strip().split())
for n in numSeparado:
    print(n)

