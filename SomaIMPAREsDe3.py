print('='*14, 'Soma dos Ímpares múltiplos de 3' ,'='*14)

soma = 0
cont = 0
for c in range(1, 500,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é igual a {}'.format(cont, soma))
print('='*28, 'FIM' ,'='*28)