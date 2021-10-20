from typing import TextIO

try:
    file: TextIO = open('123.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
