lista = [0, 1]

for i in range(10):
	pos = len(lista)-1
	lista.append(lista[pos-1] + lista[pos])

print(lista)