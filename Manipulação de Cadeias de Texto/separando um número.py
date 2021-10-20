x = int(input('Digite um número: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print(f'Milhar  {m}.')
print(f'Centena {c}.')
print(f'Dezena  {d}.')
print(f'Unidade {u}.')

# eu fiz:
# x = input('Digite um número: ')
# a = x[0]
# b = x[1]
# c = x[2]
# d = x[3]
# print('Milhar  {}.'.format(a))
# print('Centena {}.'.format(b))
# print('Dezena  {}.'.format(c))
# print('Unidade {}.'.format(d))