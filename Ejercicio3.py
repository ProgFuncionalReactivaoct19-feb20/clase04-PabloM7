"""
	Manejo de colecciones y Tuplas
	Encontrar la siguiente estructura, dadas las siguientes listas
	[((20, 4), "c"), ((30, 1), "b"), ((100, 2), "a")]
	@pablom7
"""


lista = [(100, 2), (20,4), (30, 1)]
lista2 = ["b", "a", "c"]
#Unimos las listas organizadas con zip y organizamos la segunda de manera inversa con reverse 
print(list(zip(sorted(lista), sorted(lista2, reverse=True))))