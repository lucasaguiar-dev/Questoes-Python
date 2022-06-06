import random
from time import sleep

pessoa = input('Digite Pedra, Papel ou Tesoura: ').lower()


if pessoa != 'pedra' and pessoa != 'papel' and pessoa != 'tesoura':
    print('Palavra inválida, digite apenas (pedra, papel ou tesoura)!')
else:
    print(f'Você escolheu {pessoa}!')

print('Aguardando a máquina..')
sleep(2)

lista = ['pedra', 'papel', 'tesoura']
maquina = random.choice(lista)
print(f'A máquina escolheu {maquina}!')

print('Analisando..')
sleep(2)

if pessoa == 'pedra' and maquina == 'tesoura' or pessoa == 'papel' and maquina == 'pedra' or pessoa == 'tesoura' and maquina == 'papel':
    print('VocÊ venceu!')
elif pessoa == maquina:
    print('Empate!')
else:
    print('A máquina venceu!')
