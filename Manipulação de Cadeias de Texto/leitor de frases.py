frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece na posição {} pela primeira vez.'.format(frase.find('A')+1))
print('A letra A aparece na posição {} pela última vez.'.format(frase.rfind('A')+1))
