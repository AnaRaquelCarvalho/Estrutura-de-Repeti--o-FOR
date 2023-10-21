print('='*16, 'PALINDROMO' ,'='*16)
frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O INVERSO de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALINDROMO!')
else:
    print('A frase digitado NÃO É UM PALINDROMO')
print('='*46)