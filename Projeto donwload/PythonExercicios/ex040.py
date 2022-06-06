nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media >= 7:
    print(f'Aluno aprovado! média {media}')
elif 5 <= media < 7:
    print(f'Aluno em recuperação! média {media}')
else:
    print(f'Aluno reprovado! média {media}')

