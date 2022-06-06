a = float(input('Digite o comprimento da primeira linha: '))
b = float(input('Digite o comprimento da segunda linha: '))
c = float(input('Digite o comprimento da terceira linha: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo com essas três linhas!')
else:
    print('Não é possível formar um triângulo com essas três linhas!')
