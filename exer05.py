# Escreva um programa que inverta os caracteres de um string.
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = str(input('Digite uma STRING: '))

for v in range(len(string)-1, -1, -1):
    print(string[v], end='')