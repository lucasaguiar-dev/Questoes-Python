times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza',
         'Bragantino', 'Fluminense', 'Internacional', 'Ceará', 'América-MG',
         'Cuiabá', 'Athletico-PR', 'Santos', 'São Paulo', 'Atlético-GO',
         'Juventude', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense',)
timesOrdem = sorted(times)

print(f'{times}')

print('-'*15)

print(f'{times[-4:]}')

print('-'*15)

print(f'{timesOrdem}')

print('-'*15)

print(times.index('Chapecoense'))
