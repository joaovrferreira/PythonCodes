dias = int(input('Quantos dias você permaneceu com o carro? '))
vdias = dias * 60
km = float(input('Quantos quilômetros você rodou com o carro?'))
vkm = km * 0.15
valortotal = vdias + vkm
print(f'O valor de sua conta é de {valortotal}.')
# nessa caso ficou pré-estabelecido que um dia vale R$ 60,00 e a cada KM R$ 0,15
