altura = float(input('Qual a altura dessa parede? '))
largura = float(input('Qual o comprimento dessa parede? '))
area = altura * largura
qnd_tinta = area / 2
print('Serão necessárias {:.2f} latas de tinta para pintar uma parede de {}m de área.'.format(qnd_tinta, area))
