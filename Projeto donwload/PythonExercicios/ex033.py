a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando qual o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando qual o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número é {maior} e o menor número é {menor}')
