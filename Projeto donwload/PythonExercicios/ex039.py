from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual-nascimento

if idade < 18:
    print(f'Ele ainda vai se alistar no serviço militar, faltam {18-idade} ano(s)')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Já passou do tempo do alistamento, passaram {idade-18} ano(s)')
