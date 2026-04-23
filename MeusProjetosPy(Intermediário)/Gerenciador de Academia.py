print('=' * 30)
print('Gerenciador de Academia'.center(30))

alunos_cadastrados = []
plano_cadastrado = []
idade_cadastrada = []
cont_mensal = cont_trimestral = cont_anual = 0

while True:

    print('=' * 30)
    print('Menu Principal'.center(30))
    print('-' * 30)
    print('''    [1] > Cadastrar Aluno
    [2] > Alunos Cadastrados
    [3] > Buscar Aluno
    [4] > Receita Mensal
    [5] > Sair''')
    print('-' * 30)

    opcao_menu = str(input('Digite a opção desejada: ')).strip()

    if opcao_menu == '1':
        print('Opção selecionada: [1] Cadastrar Aluno')

        while True:
            print('=' * 30)
            print('Cadastro do Aluno')
            print('-' * 30)

            aluno_nome = str(input('Digite seu nome: ')).capitalize().strip()
            aluno_idade = int(input('Digite sua idade: '))

            print('=' * 30)
            print('PLANOS DISPONIVEIS:')
            print('-' * 30)
            print('''    [1] > Plano Mensal: R$100/mês
    [2] > Plano Trimestral: R$80/mês
    [3] > Plano Anual: R$60/mês''')
            print('=' * 30)

            plano_escolhido = str(input('Digite o plano desejado: '))

            while True:
                if plano_escolhido == '1':
                    plano = 'Plano Mensal'
                    plano_cadastrado.append(plano)
                    alunos_cadastrados.append(aluno_nome)
                    idade_cadastrada.append(aluno_idade)
                    print('-' * 30)
                    print('Plano Mensal selecionado.')
                    cont_mensal += 1
                    break

                elif plano_escolhido == '2':
                    plano = 'Plano Trimestral'
                    plano_cadastrado.append(plano)
                    alunos_cadastrados.append(aluno_nome)
                    idade_cadastrada.append(aluno_idade)
                    print('-' * 30)
                    print('Plano Trimestral selecionado.')
                    cont_trimestral += 1
                    break

                elif plano_escolhido == '3':
                    plano = 'Plano Anual'
                    plano_cadastrado.append(plano)
                    alunos_cadastrados.append(aluno_nome)
                    idade_cadastrada.append(aluno_idade)
                    print('-' * 30)
                    print('Plano Anual selecionado.')
                    cont_anual += 1
                    break

                else:
                    print('-' * 30)
                    print('Plano inválido. Por favor, escolha um plano válido.')
                    plano_escolhido = str(input('Digite o plano desejado: '))

            print('=' * 30)

            continuar = str(input('Deseja cadastrar outro aluno? [S/N] ')).upper().strip()[0]

            while True:
                if continuar == 'N':
                    print('Voltando para Menu...')
                    break

                elif continuar == 'S':
                    break

                else:
                    print('Opção inválida. Tente novamente!')
                    continuar = str(input('Deseja cadastrar outro aluno? [S/N] ')).upper().strip()

            if continuar == 'N':
                break

    elif opcao_menu == '2':
        print('Opção selecionada: [2] Alunos Cadastrados')
        print('=' * 30)
        print('Alunos Cadastrados:')

        if len(alunos_cadastrados) == 0:
            print('Nenhum aluno cadastrado.')
        else:
            for aluno in alunos_cadastrados:
                print(aluno)

    elif opcao_menu == '3':
        print('Opção selecionada: [3] Buscar Aluno')
        print('=' * 30)

        buscar_aluno = str(input('Digite o nome do aluno que deseja buscar: ')).capitalize().strip()

        if buscar_aluno in alunos_cadastrados:
            posicao_aluno = alunos_cadastrados.index(buscar_aluno)
            print(f'Nome: {buscar_aluno}')
            print(f'Idade: {idade_cadastrada[posicao_aluno]}')
            print(f'Plano: {plano_cadastrado[posicao_aluno]}')
        else:
            print('Aluno não encontrado.')

    elif opcao_menu == '4':
        print('Opção selecionada: [4] Receita Mensal')

        receita_mensal = 0

        for plano in plano_cadastrado:
            if plano == 'Plano Mensal':
                receita_mensal += 100
            elif plano == 'Plano Trimestral':
                receita_mensal += 80
            elif plano == 'Plano Anual':
                receita_mensal += 60

        print('=' * 30)
        print(f'Planos Mensais Cadastrados: {cont_mensal}')
        print(f'Planos Trimestrais Cadastrados: {cont_trimestral}')
        print(f'Planos Anuais Cadastrados: {cont_anual}')
        print('-' * 30)
        print(f'Valor total da receita mensal: R${receita_mensal}')
        
    elif opcao_menu == '5':
        print('Opção selecionada: [5] Sair')
        print('=' * 30)
        print('Saindo do programa...')
        print('Obrigado por usar o Gerenciador de Academia!')
        print('=' * 30)
        break

    else:
        print('Opção inválida. Tente novamente!')