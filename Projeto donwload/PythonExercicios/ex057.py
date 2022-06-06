s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
        s = str(input('Dados invalidos, por favor informe seu sexo [M/F]: ')).strip().upper()[0]
print('Valores corretos!')



