# 30. Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a
# idade em anos, meses e dias, considerando os anos bissextos.
diaNascimento = int(input("Digite o dia de seu nascimento"))
mesNascimento = int(input("Digite o mês de seu nascimento"))
anoNascimento = int(input("Digite o ano de seu nascimento"))

diaAtual= int(input("Digite o dia de hoje"))
mesAtual= int(input("Digite o mês de atual"))
anoAtual= int(input("Digite o ano atual"))

anosTotais = anoAtual - anoNascimento
mesesTotais = 0
diasTotais = 0

if(mesAtual > mesNascimento):  
    mesesTotais = mesAtual - mesNascimento - 1
    
    if(diaAtual >= diaNascimento):
        mesesTotais += 1
        diasTotais = diaAtual - diaNascimento
        print(f"Você tem {anosTotais} anos, {mesesTotais} meses e {diasTotais} dias")
    else:
        diasTotais = 30 - diaNascimento + diaAtual
        print(f"Você tem {anosTotais} anos, {mesesTotais} meses e {diasTotais} dias")

elif(mesAtual < mesNascimento):
    mesesTotais = 12 - mesNascimento + mesAtual -1
    
    if(diaAtual >= diaNascimento):
        mesesTotais += 1
        diasTotais = diaAtual - diaNascimento
        
        print(f"Você tem {anosTotais} anos, {mesesTotais} meses e {diasTotais} dias")
    
    else:
        diasTotais = 30 - diaNascimento + diaAtual
        print(f"Você tem {anosTotais} anos, {mesesTotais} meses e {diasTotais} dias")
else:
    print(f"Você tem {anosTotais} anos, {mesesTotais} meses e {diasTotais} dias.")