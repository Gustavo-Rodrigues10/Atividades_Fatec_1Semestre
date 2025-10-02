# 32. Receba um número inteiro. Calcule e mostre o seu fatorial.
def calcular_fatorial():
    numero = int(input("Digite um número inteiro: "))
    fatorial = 1
    contador = 1

    while contador <= numero:
        fatorial *= contador
        contador += 1

    print(f"O fatorial de {numero} é {fatorial}")

calcular_fatorial()
