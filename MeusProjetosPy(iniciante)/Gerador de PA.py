print('Gerador de PA')
print('-' * 14)
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(numero, '>', end=' ')
        c += 1
        numero += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')