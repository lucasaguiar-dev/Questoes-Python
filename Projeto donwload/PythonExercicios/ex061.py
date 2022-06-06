primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
contador = 0

while contador < 10:
    termo = primeirotermo + razao * contador
    print(termo, '→', end=' ')
    contador += 1
print('Fim!')

