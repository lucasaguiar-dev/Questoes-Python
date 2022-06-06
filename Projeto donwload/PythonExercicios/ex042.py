a = float(input('Digite o comprimento da primeira linha: '))
b = float(input('Digite o comprimento da segunda linha: '))
c = float(input('Digite o comprimento da terceira linha: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo com essas três linhas!')
    if a == b and b == c:
        print('Esse triangulo é Equilátero!')
    elif a == b and b != c or b == c and a != c:
        print('Esse triangulo é Isoceles!')
    else:
        print('Esse triangulo é Escaleno')
else:
    print('Não é possível formar um triângulo com essas três linhas!')


