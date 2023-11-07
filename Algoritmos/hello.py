def hello():
    name = input("Digite seu nome: ")
    print(f"Bom dia, {name}")



def example_cash_machine():
    balance = 1000
    value = int(input("""    Digite
          1 para saque
          2 para saldo
          3 para extrato: """))
    if value == 1:
        withdraw = int(input("Digite o valor que deseja sacar: "))
        if withdraw > balance:
            print('Valor de saldo insuficiente')
        else: print('Saque realizado com com sucesso!')
    elif value == 2:
        print(f"Seu saldo é R$ {balance}")
    elif value == 3:
        print("Carregando extrato atualizado. Aguarde..")
    else:
        print("Número inválido. Digite uma opção válida")
        (example_cash_machine())
    

example_cash_machine()