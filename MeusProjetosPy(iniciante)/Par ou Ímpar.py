from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

# Eu poderia ter usado (while par_impar not in 'PI') dentro do while true deixaria o código muito menor, porem fiz sem olhar a resolução final para poder testar meus conhecimentos

cont = 0
while True:
    valor = int(input('Diga uma valor: '))
    compu = randint(0, 10)
    soma = valor + compu
    cont += 1
    par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print('-' * 30)
    if par_impar == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {valor} e o computador {compu}. Total de {soma} DEU PAR')
            print('-' * 30)
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
        else:
            print(f'Você jogou {valor} e o computador {compu}. Total de {soma} DEU ÍMPAR')
            print('-' * 30)
            print('Você PERDEU!')
            print('=-' * 15)
            break
    elif par_impar == 'I':
        if soma % 2 != 0:
            print(f'Você jogou {valor} e o computador {compu}. Total de {soma} DEU PAR')
            print('-' * 30)
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
        else:
            print(f'Você jogou {valor} e o computador {compu}. Total de {soma} DEU ÍMPAR')
            print('-' * 30)
            print('Você PERDEU!')
            print('=-' * 15)
            break
print(f'GAME OVER! Você ganhou {cont-1} vezes')