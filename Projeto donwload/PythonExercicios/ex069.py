maiores = mulheres20 = homens = 0
while True:
    i = int(input('Digite a idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar cadastrando [S/N]? ')).strip().upper()[0]
    if i > 18:
        maiores += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        mulheres20 = + 1
    if r == 'N':
        break
print(f'''A) {maiores} pessoas tem mais de 18 anos 
B) Foram cadastrados {homens} homens
C) {mulheres20} É o número de mulheres com menos de 20 anos''')
