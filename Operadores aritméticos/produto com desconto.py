a = float(input('Qual o preço do produto? R$ '))
b = (a / 100)
c = b * 5
d = a - c
print('Seu produto com desconto de 5% fica em R$ {:.2f}.'.format(d))
