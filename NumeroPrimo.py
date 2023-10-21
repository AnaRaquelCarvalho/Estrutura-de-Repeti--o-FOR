print('='*11, 'Número Primo' ,'='*11)
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n,tot))
if tot == 2:
    print('\033[33mE por isso ele é PRIMO!')
else:
    print('\033[31mE por isso ele NÃO É PRIMO!')
print('='*46)