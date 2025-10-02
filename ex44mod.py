# 44. Receba o número da base e do expoente. Calcule e mostre o valor da
# potência.
def calcular_potencia():
    base = float(input("Digite o número da base: "))
    expoente = float(input("Digite o número do expoente: "))

    potencia = base ** expoente

    print("O valor da potência é:", potencia)

calcular_potencia()
