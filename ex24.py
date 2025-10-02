# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
valor = int(input("Digite um valor inteiro: "))

if valor % 2 == 0 and valor % 3 == 0:
    print(f"O valor {valor} é divisível por 2 e 3.")
elif valor % 2 == 0:
    print(f"O valor {valor} é divisível apenas por 2.")
elif valor % 3 == 0:
    print(f"O valor {valor} é divisível apenas por 3.")
else:
    print(f"O valor {valor} não é divisível por 2 nem por 3.")
