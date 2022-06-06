numeros = []

for c in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
print(f'O maior número é {max(numeros)} e sua posição na lista é {numeros.index(max(numeros))+1}'
      f'\nO menor número é {min(numeros)} e sua posição na lista é {numeros.index(min(numeros))+1}')
