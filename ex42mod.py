# 42. Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
def serie_50_99():
    soma = 0
    numerador = 1
    denominador = 1

    while numerador <= 50:
        soma += numerador / denominador
        numerador += 1
        denominador += 2

    print("O resultado da série é:", soma)

serie_50_99()
