from datetime import datetime

menu = """
________Bem-vindo ao RodriBank________

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

______________________________________
Que operação deseja fazer?
=>"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        depositando = True
        while depositando:
            deposito = float(input("\nQuanto você deseja depositar?"))
            data_hora_deposito = datetime.now()
            extrato.append(f"{data_hora_deposito.strftime('%d/%m/%Y %H:%M')} - Depósito de R${deposito}")
            saldo += deposito
            print("\nDepósito efetuado!")
            resposta = input("\nDeseja fazer mais algum depósito? (S/N)")
            if resposta == "S":
                depositando = True
            elif resposta == "N":
                depositando = False
            else:
                print("\nValor não reconhecido, você será redirecionado ao menu de opções.")
                depositando = False

    elif opcao == "s":
        sacando = True
        while sacando:
            saque = float(input("\nQuanto você deseja sacar?"))
            if saldo < saque:
                print("\nSaldo insuficiente!")
                sacando = False
            elif numero_saques > limite_saques:
                print("\nLimite de saques excedido.")
                sacando = False
            elif saque > limite:
                print("\nValor de saque maior que o seu limite.")
                sacando = False
            else:
                saldo -= saque
                numero_saques += 1
                print("\nSaque efetuado.")
                data_hora_saque = datetime.now()
                extrato.append(f"{data_hora_saque.strftime('%d/%m/%Y %H:%M')} - Saque de R${saque}")
                resposta = input("\nDeseja realizar outro saque?")
                if resposta == "S":
                    sacando = True
                elif resposta == "N":
                    sacando = False
                else:
                    print("Valor não reconhecido, você será redirecionado ao menu de opções.")
                    sacando = False

                


    elif opcao == "e":
        print(f"__________________Extrato__________________")
        for n in range(len(extrato)):
            print(extrato[n])
        print(f"____________Saldo Final: {saldo}___________")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, favor retornar uma das opções informadas.")