print(f'Sequência de Fibonacci\n{'=-='*30}')
n = int(input('Qual número deseja conferir? '))
print(f'{'=-='*30}')
p1 = 1
p2 = 2
p3 = 0
lista = [1,1,2]

# Calcula a sequência----------------------------------------------------------------------
while n+2>p3:
    if p1 == 1 and p2 == 2:
        print(f'Os primeiros termos da sequência de Fibonacci:\n1 ->', p1, end=' -> ')
        print(p2, end=' -> ')
        
    p3 = p1 + p2
    print(p3, end=' -> ')
    p1 = p2
    p2 = p3
    lista.append(p3)
print(f'\n{'=-='*30}')

# Valida se o número informado faz parte da sequência----------------------------------------
valida = False
cont = 0
while cont<len(lista):
    if lista[cont] == n:
        valida = True
    cont+=1
# Retorna a mensagem de validação ou não validação--------------------------------------------
if valida==True:
    print(f'O número {n} pertence a sequência.')
else:
    print(f'O número {n} não pertence a sequência.')

print('FIM')
