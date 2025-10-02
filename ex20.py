# Receba três coeficientes A, B, C de uma equação do 2° grau. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
coeficiente_A = int(input("Digite o coeficiente A: "))
coeficiente_B = int(input("Digite o coeficiente B: "))
coeficiente_C = int(input("Digite o coeficiente C: "))

delta = (coeficiente_B) ** 2 - 4 * coeficiente_A * coeficiente_C

if delta < 0:
    print("Equação sem raízes reais.")
else: 
    raiz_1 = (-(coeficiente_B) + delta ** 0.5) / (2 * coeficiente_A)    
    raiz_2 = (-(coeficiente_B) - delta ** 0.5) / (2 * coeficiente_A)

    print(f"A raíz 1 da equação é: {raiz_1}, e a raíz 2 da equação é: {raiz_2}.")    