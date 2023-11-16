print('='*11,' Analisando dados de uma pequena população ','='*11)
media = 0
maior = 0
menor = 0
MaiorIdade = ''
for pessoas in range (1,6):
    print('-'*12,'{}ª Pessoa'.format(pessoas),'-'*12)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    m = media/4
    if maior == idade and sexo in 'Mn':
        maior = idade
        MaiorIdade = nome
    if sexo in 'Mn' and idade > maior:
        maior = idade
        MaiorIdade = nome
    if sexo in 'Ff' and idade <= 21:
            menor += 1
print('\033[33m>>> A média de idade do grupo é de {:.1f} anos.'.format(m))
print('\033[34m>>> O homem mais velho tem {} anos e se chama {}'.format(maior, MaiorIdade))
print('\033[35m>>> Ao todo são {} mulheres com menos de 21 anos'.format(menor))
print('='*56)