# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor
# valor. Obs.: somente valores positivos.
numero = float(input("Digite o 1º número positivo: "))
maior = numero
menor = numero
contador = 2

while contador <= 100:
    numero = float(input(f"Digite o {contador}º número positivo: "))
    if numero <= 0:
        print("Digite apenas valores positivos.")
        continue
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    contador += 1

print(f"O maior valor é {maior} e o menor valor é {menor}")
