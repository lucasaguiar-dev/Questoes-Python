num = int(input('Digite um número para ser convertido: '))
baseNum = int(input('Digite 1 para converter para binário, 2 para octal, 3 para hecadecimal. '))
if baseNum == 1:
    print(f'O número convertido para binário ficou: {bin(num)}')
elif baseNum == 2:
    print(f'O número convertido para octal ficou {oct(num)}')
else:
    print(f'O número convertido para hexadecimal ficou {hex(num)}')
