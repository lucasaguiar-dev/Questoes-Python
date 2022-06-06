n = int(input('Quantos elementos: '))
contador = 0
a = 0
b = 1
print(a)
print(b)
while contador < n:
    c = a + b
    a = b
    b = c
    print(c)
    contador += 1
