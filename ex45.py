# 45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
numerador = 1
denominador = 1
soma = 0
contador_sinal = 1

while numerador <= 15:
    termo = numerador / (denominador * denominador)
    if contador_sinal % 2 != 0:
        print(f"{soma:.2f} += {numerador} / {denominador**2}")
        soma += termo
    else:
        print(f"{soma:.2f} -= {numerador} / {denominador**2}")
        soma -= termo

    numerador += 1
    denominador += 1
    contador_sinal += 1

print("O resultado da série é:", soma)
