n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = (n1+n2)
print('A soma entre {} e {} equivale a {}.'.format(n1, n2, s))
# poderia funcionar tbm o print('A soma entre n1, 'e', n2, 'equivale a', s, '.')
# poderia funcionar tbm o print(f'A soma entre {n1} e {n2} vale {s}.')
# eu não preciso necessáriamente fazer uma variável para somar os dois, posso colocar a conta dentro do .format(n1 + n2)
# sem o int na frente, seria uma string e não um número
