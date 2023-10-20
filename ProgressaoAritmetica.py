print('='*8, 'Prograssão Aritmética' ,'='*8)
print('        10 termos de uma P.A   ')
print('='*40)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
print('='*56)
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c),end='➞ ')
print('Acabou!!!')
print('='*56)