# Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
def verificar_multiplo():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if numero1 > numero2:
        if numero1 % numero2 == 0:
            print(f"{numero1} é múltiplo de {numero2}.")
        else:
            print(f"{numero1} não é múltiplo de {numero2}.")
    else:
        if numero2 % numero1 == 0:
            print(f"{numero2} é múltiplo de {numero1}.")
        else:
            print(f"{numero2} não é múltiplo de {numero1}.")

verificar_multiplo()
