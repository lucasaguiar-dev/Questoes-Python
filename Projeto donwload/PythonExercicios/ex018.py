import math
a = float(input('Digite o angulo: '))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print(f'O cosseno, seno e a tangente de {a} são respectivamente: {c:.1f}, {s:.1f} {t:.1f}')
