#SISTEMA BANCÁRIO - DESAFIO 1 BOOTCAMP DIO

saldo = 0
saque_limite = 500
limite_diario_saque = 3
extrato = ""
numero_saque = 0

while True:
    opcao = int(input("[1] Sacar \n[2] Depositar \n[3] Extrato \n [4] Sair\n:"))
    if opcao == 1:
        valor_saque = int(input("Informe o valor que desja sacar:\n"))
        
        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > saque_limite

        excedeu_saques = numero_saque >= limite_diario_saque

        if excedeu_saldo:
            print("Processamento falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Processamento falhou! Valor informado é maior que o limite de saque por caixa!")

        elif excedeu_saques:
            print("Processamento falhou! Você excedeu o limite de saques diários.")

        elif valor_saque > 0:
            saldo = saldo - valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saque += 1
            print("Sacando...")
        else :
            print("Numero inválido, tente novamente")

    elif opcao == 2:
        valor_deposito =int(input("Qual valor deseja fazer seu depósito?\n"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Seu deposito foi concluído!")
        else:
            print("O valor informado é inválido")
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == 4:
        break
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")