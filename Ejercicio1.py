"""
	Colecciones y tuplas
	@pablom7
"""

listaA=[10, 2, 3, 4]
listaB=["a", "b", "c", "d"]
#Ordenamos las listas con la funcion sorted
lista1 = sorted(listaA)
#Ordenamos la lista de manera inversa con reverse
lista2 = sorted(listaB, reverse=True)
#Juntamos las dos listas ya ordenadas con el uso de zip
listajunta = zip(lista1, lista2)
#Presentamos la union de las dos listas
print(list(listajunta))
