matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares, somaColuna, maiorValor = 0, 0, 0

for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            somaColuna += matriz[l][c]
        if l == 2:
            if matriz[l][c] > maiorValor:
                maiorValor = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {somaColuna}')
print(f'O maior valor da segunda linha é {maiorValor}')
