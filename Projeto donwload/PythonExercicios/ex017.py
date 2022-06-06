import math
cO = float(input('Digite o cateto oposto: '))
cA = float(input('Digite o cateto adjacente: '))
h = math.hypot(cO,cA)
print(f'O comprimento da hipotenusa é {h}')
