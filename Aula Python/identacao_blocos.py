def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca da caixa.")

    else:
        print("Saldo insuficiente.")
    
    print("Obrigado por ser nosso cliente")

sacar(1000)

def depositar(valor):
    saldo = 500
    saldo += valor