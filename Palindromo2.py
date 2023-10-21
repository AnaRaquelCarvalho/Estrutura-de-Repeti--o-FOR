print('='*16, 'PALINDROMO 2' ,'='*16)
frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O INVERSO de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALINDROMO!')
else:
    print('A frase digitado NÃO É UM PALINDROMO')
print('='*46)