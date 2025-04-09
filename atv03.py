#ler um valor N e imprimir todos os valores inteiros entre 1(inclusive) e N (inclusive). considere que o n sera sempre maior que zero.
valor = int(input("digite um valor: "))
if valor < 0:
    print("número inválido")
for x in range(1,valor+1,1):
    print(x, end= " ")

