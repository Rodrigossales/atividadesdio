print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
limite = 200
conta_especial = False

saque = int(input("Digite o valor que você deseja sacar:"))
if (saque <= saldo and saque <= limite) or (conta_especial and saldo >= saque):
    print(f"Saque de {saque} efetuado!")
elif saldo < saque:
    print(f"Saldo insufieciente!")
elif limite < saque:
    print(f"Limite de saque atingido")

