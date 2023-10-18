print('='*16, 'TABUADA' ,'='*16)
n = int(input('Digite um número da Tabuada: '))
print('''Escolha a tabuada do número {} que deseja ver:'
[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO'''.format(n))
opcao = int(input('Opção: '))
print('='*26)
if opcao == 1:
    print('Tabuada de {} >> ADIÇÃO '.format(n))
    for c in range(1,11):
        print('       {} + {:2} = {}'.format(c, n, (c + n)))
elif opcao == 2:
    print('Tabuada de {} >> SUBTRAÇÃO '.format(n))
    for c in range(1, 11):
        print('       {} - {:2} = {}'.format(c, n, (c - n)))
elif opcao == 3:
    print('Tabuada de {} >> MULTIPLICAÇÃO '.format(n))
    for c in range(1,11):
        print('       {} * {:2} = {}'.format(c, n,(c * n)))
elif opcao == 4:
    print('Tabuada de {} >> DIVISÃO '.format(n))
    for c in range(1,11):
        print('       {} : {:2} = {:.1f}'.format(n, c,(n / c)))
else:
    opcao = 0
    print('\033[1:31m[{}]'.format(opcao),'OPÇÃO INVÁLIDA - TENTE NOVAMENTE!')
print('='*26)
