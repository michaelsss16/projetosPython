def printar(par1):
	print(par1, "\n")
lista = []
for n in range(int(input("Qual o número de iterações desejada?\n"))):
	var = input("O que deseja escrever na tela?\n")
	lista.append(var)
for n in lista:
	print(n)
printar("Fim do programa")