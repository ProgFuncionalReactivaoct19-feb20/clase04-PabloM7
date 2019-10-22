"""
	Manejo de colecciones y tuplas
	Encontrar la siguiente estructura dadas las siguientes listas
	[("a", (30, 1)),("b", (100, 2)), ("c", (20, 4))]
	@pablom7
"""
lista = [(100, 2), (20,4), (30, 1)]
lista2 = ["b", "a", "c"]

#Usaremos zip y le enviaremos dos listas, al mismo tiempo que esas listas seran ordenadas con sorted, la segunda lista sera ordenada segun su segundo elemento
print(list(zip(sorted(lista2), sorted(lista, key=lambda x: x[1]))))

