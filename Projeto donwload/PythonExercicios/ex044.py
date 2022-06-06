preco = float(input('Digite o preço do produto: '))
pagamento = int(input('Para pagar em dinheiro/cheque digite 1, para pagar no cartão a vista digite 2' '\nPara pagar em '
                      '2x no cartão digite 3, para pagar em 3x ou mais digite 4. '))

if pagamento == 1:
    print(f'O valor total será {preco * 0.9}R$')
elif pagamento == 2:
    print(f'O valor total será {preco * 0.95}R$')
elif pagamento == 3:
    print(f'O valor total será {preco}R$')
else:
    print(f'O valor total será {preco * 1.2}R$')
