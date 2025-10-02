# Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahreinheit
temp_celsius = float(input("Digite a temperatura em celsius:"))

temp_fahreinheit = (9 * temp_celsius + 160) / 5

print("A temperatura de", temp_celsius, "graus celsius convertida para fahrenheit é", temp_fahreinheit, "graus fahrenheit")