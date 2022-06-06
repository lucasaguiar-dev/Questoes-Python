cedula50 = cedula20 = cedula10 = cedula1 = int(0)
valor = 1
resto = 0
while True:
    valor = int(input('Digite o valor a ser sacado: R$ '))
    cedula50 = int(valor / 50)
    resto = valor % 50
    cedula20 = int(resto / 20)
    resto = resto % 20
    cedula10 = int(resto / 10)
    resto = resto % 10
    cedula1 = int(resto / 1)
    break
print('='*20)
print(f"{'Banco Aguiar' : ^20}")
print('='*20)
print(f'''Total de {cedula50} cédulas de R$ 50
Total de {cedula20} cédulas de R$ 20
Total de {cedula10} cédulas de R$ 10
Total de {cedula1} cédulas de R$ 1''')