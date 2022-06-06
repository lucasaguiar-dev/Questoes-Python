primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
contador = 0

while contador < 10:
    termo = primeirotermo + razao * contador
    print(termo)
    contador += 1

termo2 = termo
escolha = int(input('Deseja mostrar mais quantos termos: '))
if escolha > 0:
    contador = 1
    while contador <= escolha:
        termo2 = termo + razao * contador
        contador += 1
        print(termo2)
else:
    print('Fim!')