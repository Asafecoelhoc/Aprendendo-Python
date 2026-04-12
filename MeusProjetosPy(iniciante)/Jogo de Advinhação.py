from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
jogador = int(input('Qual é o seu palpite? '))
tentativas = 0
while jogador != computador:
    if jogador != computador:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
print('Parabéns você acertou!')
print(f'O número de tentativas para acertar foi {tentativas + 1}')
