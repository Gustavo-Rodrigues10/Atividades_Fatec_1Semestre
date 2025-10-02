# Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m
valor_Deposito = float(input("Digite o valor do depósito em poupança: "))

valor_Rendimento = valor_Deposito * 0.013
valor_Total = valor_Deposito + valor_Rendimento

print(f"O valor após 1 mês de aplicação é: {valor_Total}")
