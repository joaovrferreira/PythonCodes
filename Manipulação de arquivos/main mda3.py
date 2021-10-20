from typing import TextIO

#with open('aws.txt', 'w+') as file:
  #  file.write('Linha1\n')
  #  file.write('Linha2\n')
   # file.write('Linha3\n')
  #   file.seek(0)
  # print(file.read())

with open('aws.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())