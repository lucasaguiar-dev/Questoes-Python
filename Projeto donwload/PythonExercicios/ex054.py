from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento: '))
    idade = atual-n
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'O número de maiores é {maior} e o número de menores é {menor}')
