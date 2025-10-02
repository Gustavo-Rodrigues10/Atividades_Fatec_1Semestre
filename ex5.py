# Receba os coeficientes A, B, C de uma equação do 2° grau. Calcule e mostre suas raízes reais.
coeficiente_A = float(input("Digite o coeficiente A: "))
coeficiente_B = float(input("Digite o coeficiente B: "))
coeficiente_C = float(input("Digite o coeficiente C: "))

delta = coeficiente_B ** 2 - 4 * coeficiente_C * coeficiente_A

raiz_1 = (- coeficiente_B + delta ** 0.5) / 2 * coeficiente_A
raiz_2 = (- coeficiente_B - delta ** 0.5) / 2 * coeficiente_A

print(f"A raíz 1 é :{raiz_1} e a raíz 2 é :{raiz_2}.")

