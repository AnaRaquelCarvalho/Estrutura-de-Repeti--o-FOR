print('='*14, 'Soma Pares' ,'='*14)
s = 0
cont = 0
for c in range(0,6):
    n = int(input('          Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('='*48)
print('Foram informados {} números PARES e a soma foi {}'.format(cont, s))
print('='*48)