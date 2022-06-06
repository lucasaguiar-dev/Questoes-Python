def escreva(msg):
    print('~' * (len(msg)+2))
    print(msg.center((len(msg)+2)))
    print('~' * (len(msg)+2))


msg = input('Digite algo: ')
escreva(msg)


