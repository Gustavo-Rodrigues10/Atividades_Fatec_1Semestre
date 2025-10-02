# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
projecao_anos = 17

idade_atual = ano_atual - ano_nascimento
idade_futura = idade_atual + projecao_anos

print(f"Sua idade atual é: {idade_atual} anos")
print(f"Sua idade daqui a {projecao_anos} anos será: {idade_futura} anos")