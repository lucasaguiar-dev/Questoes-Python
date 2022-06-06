somaidade = 0
m = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('-'*10, c, 'ª', '-'*10)
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    m = m + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print(f'A média de idade é {m/4}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho} ')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
