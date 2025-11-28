import os
from time import sleep

#Variáveis
saldo_caixa = 0

#Estrutura + Lógica
while True:
    os.system('cls' if os.name == 'nt' else 'clear') #Limpa tela
    print('-' * 20)
    print('-' * 8 + 'CAIXA' + '-' * 7)
    print('-' * 5 + 'ELETRÔNICO' + '-' * 5)
    print('-' * 20)
    print('1 - Depositar:')
    print('2 - Sacar:')
    print('3 - Saldo:')
    print('4 - Sair:')
    try: 
        opcao = int(input('Escolhe uma Opção:'))
    except ValueError:
        print('Digite um número Válido:')
        input('Pressione "ENTER" para continuar...!')
        continue


    #Deposito
    if opcao == 1:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') #Limpa tela
            print('-' * 20)
            print('-' * 6 + 'DEPOSITO' + '-' * 6)
            try:
                print('Digite o Valor do Deposito')
                deposito_cliente = float(input('R$: '))
            except ValueError:
                print('Digite Apenas Números!')
                input('Pressione "ENTER" para voltar ao Menu!') 
                continue 
            if deposito_cliente > 0:
                saldo_caixa += deposito_cliente
                print('Aguarde seu Depósito...')
                sleep(3)
                print('Depósito Concluido!')
                break
            else:
                print('Digite um Valor maior que R$ 0.00 Reais')
        input('Pressione "ENTER" para voltar ao Menu!')


    #Sacar
    elif opcao == 2:
        if saldo_caixa > 0:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') #Limpa tela
                print('-' * 20)
                print('-' * 8 + 'SAQUE' + '-' * 7)
                print(f'Saldo: {saldo_caixa:.2f}')
                print('Digite o valor do Saque:')
                try:
                    saque = float(input('R$: '))
                except ValueError:
                    print('Digite Apenas Números!')
                    input('Pressione "ENTER" e Tente Novamente !') 
                    continue

                if saque <= 0:
                    print('Aguarde...')
                    sleep(2)
                    print('Digite um Valor maior que R$0.00 Reais')
                    break
                
                elif saque > saldo_caixa:
                    print('Aguarde...')
                    sleep(2)
                    print('Valor Maior que o Saldo!')
                    break
                                
                else:
                    saldo_caixa -= saque
                    print('Aguarde...')
                    sleep(3)
                    print('Saque Concluido')
                    break             
        else:
            print('Saldo insuficiente!')
        input('Pressione "ENTER" para voltar ao Menu!')


    #Sair
    elif opcao == 3:
        while True:
            if saldo_caixa > 0:
                os.system('cls' if os.name == 'nt' else 'clear') #Limpa tela
                print('-' * 20)
                print('-' * 8 + 'SALDO' + '-' * 7)
                print('-' * 20)
                print(f'Seu Saldo: R${saldo_caixa:.2f}')
                print('-' * 20)
                input('Pressione "ENTER" para voltar ao Menu!')
                break

            else:
                print('-' * 20)
                print('-' * 8 + 'SALDO' + '-' * 7)
                print('-' * 20)
                print(f'Seu Saldo: R${saldo_caixa:.2f}')
                print('Para sacar, precisa fazer um depósito!')
                print('-' * 20)
                input('Pressione "ENTER" para voltar ao Menu!')
                break
    elif opcao == 4:
        print('Saindo...')
        sleep(1)
        print('-' * 20)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Limpa tela
        break

    
    #Opção Inválida
    else:
        print('Opcção Inválida!')
        input('Pressione "ENTER" para voltar ao Menu!')
