contador = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    contador += 1
    soma = soma + n
print(f'Foram digitados {contador} números e a soma entre eles é {soma-999}')