print('='*16, 'Grupo da Maioridade' ,'='*16)
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range (0,7):
    nasc = int(input('Em que ano ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E {} pessoas menores de idade '.format(menor))
print('='*46)