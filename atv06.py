#ler 5 valores, calcular e escrever a média aritmética desses valores lidos
soma = 0
for x in range (1,5+1,1):
    valor = int(input("digite os valores: "))
    soma = soma + valor
    media = soma/5
print(f" a média é {media}")