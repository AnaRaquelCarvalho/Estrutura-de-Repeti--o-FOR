print('='*12,' Maior e Menor Seguência de Pesos ','='*12)
maior = 0
menor = 0
for pessoas in range(1,6):
    peso = float(input('Informe o Peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso
print('\033[34mO maior peso lido foi {} Kg.'.format(maior))
print('\033[31mO Menor peso lido foi {} Kg.'.format(menor))
print('\033[m='*14,' FIM ','='*14)