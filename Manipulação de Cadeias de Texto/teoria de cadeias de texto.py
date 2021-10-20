# toda cadeia de texto está em aspas simples ou aspas duplas
# o python salva essa frase em mini espaços que recebem um índice, um número dentro da memória do pc
# o símbolo de colchete [] é o identificador de uma estrutura de dados de uma função chamada lista

frase = 'Curso em Vídeo Python'
#        0123456789...

# Operações com uma string:

# 1 fatiamento é pegar apenas pedaços específicos da string
frase[9]
# dentro desse comando, a letra 9 é o 'V'
frase[9:13]
# pega do 9 (é o 'V') e o 13 (é o 'o'), porém exclui a última, ou seja, vai até o caracter 12 ('Vide')
# o último valor não entra na contagem
frase[9:21]
# não é a melhor forma de fatiar colocando um valor acima
# não vai considerar o 21, a variável vai até somente o 20 ('Vídeo Python')
frase[9:21:2]
# vai de 9 até 21 e vai pulando de 2 em 2 ('VdoPto')
frase[:5]
# vai de 0 até 5, continua excluindo o último valor ('Curso')
frase[15:]
# vai de 15 até o final ('Python')
frase[9::3]
# vai começar no 9 e vai até o fim pulando de 3 em 3 ('VePh')

# 2 análise: é saber informações sobre uma string
len(frase)
# comprimento da frase (21 caracteres)
frase.count('o')
# ele conta quantas vezes aparece o que está no (  ) (3 'o')
frase.count('o', 0, 13)
# é uma contagem de quantos 'o' tem do 0 ao 13 (excluindo o último valor)
frase.find('deo')
# quantas vezes ele encontrou o 'deo' e mostra que começou na posição 11
frase.find('Android')
# vai retornar o valor -1 já que a palavra não está dentro da minha variável
'Curso' in frase
# existe 'Curso' em frase? True ou False

# 3 transformação
frase.replace('Python', 'Android')
# substitui a primeira palavra pela segunda
frase.upper()
# upper é um método, o que for minúsculo vai para maiúsculo
frase.lower()
# substitui o que está em maiúsculo para minúsculo
frase.capitalize()
# só o primeiro caracter vai para maiúsculo
frase.title()
# o primeiro caracter de uma palavra vai para maiúsculo

# 4 divisão
frase.split()
# cria divisões onde tiver os espaços sem nada
# cada uma dessas palavras nova recebe um índice diferente
# cria uma 'lista' com as palavras novas

# 5 junção
'-'.join(frase)
# junta as palavras da lista numa única cadeia de caracteres
# e coloca o '-' entre as palavras

exemplo = '   Aprenda Python  '
#          0123456789...
exemplo.strip()
# remove os espaços inúteis ('Aprenda Python')
exemplo.rstrip()
# remove os espaços para a direita ('   Aprenda Python')
exemplo.lstrip()
# remove os espaços da esquerda ('Aprenda Python  ')

