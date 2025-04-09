#ler 10 valores e escrever quantos desses valores lidos estão no intervalo{10,20}
# (incluindo os valores 1o e 20 no intervalo) e quantos deles estão fora desse intervalo

dentro=0
fora = 0
for x in range(10, 21, 1):
    num = int(input("digite os valores: "))
    if num >=10 and num <=20:
          dentro = dentro+1
    else:
        fora = fora+1

print(f"{dentro1} dentro do intervalo")
print(f"{fora} fora do intevalo")




