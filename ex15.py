# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

soma_quadrados = (cateto1 ** 2) + (cateto2 ** 2)
hipotenusa = soma_quadrados ** 0.5

print(f"O valor da hipotenusa é: {hipotenusa}")