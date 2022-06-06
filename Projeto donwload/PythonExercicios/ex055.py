import math
from math import inf
for c in range(1, 6):
    p = int(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f'O maior peso foi {maior} e o menor foi {menor}')
