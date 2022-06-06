pessoas = {'nome': str(input('Nome: ')), 'media': float(input(f'Média: '))}
if pessoas['media'] >= 7:
    pessoas['situação'] = 'aprovado'
else:
    pessoas['situação'] = 'reprovado'
print(f'O Nome é igual a {pessoas["nome"]}\nMédia é igual a {pessoas["media"]}\nSituação igual a {pessoas["situação"]}')

