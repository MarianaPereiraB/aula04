#ler 10 valores e escrever quantos desses valores lidos são Negativos.
cont=0
for x in range(1, 10, 1):
    valores = int(input("digite os valores: "))
    if valores <0:
        cont =cont+ 1
print(f"{cont} valor(es) negativo(s)")