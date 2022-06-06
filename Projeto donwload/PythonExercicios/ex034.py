salario = float(input('Digite o salário em R$: '))
if salario>1250.0:
    print(f'Com o aumento o salário ficará {salario*1.1}')
else:
    print(f'Com o aumento o salário ficará {salario*1.15}')
