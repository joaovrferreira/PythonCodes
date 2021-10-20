cid = str(input('Digite o nome da sua cidade: ')).strip().upper()
dividido = cid.split()
print('O nome da sua cidade começa com Santo? {}.'.format('SANTO' in dividido[0]))