"""
Manejo de colecciones y tuplas


# Encontrar la siguiente estructura
#

[(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]

Dadas las siguientes estructuras
@pablom7
"""

paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]
#Obtenemos el promedio de cada tupla
promedio = list(map(lambda x: sum(x)/len(x), paraleloA))
#Obtenemos la suma de cada tupla
notatotal = list(map(lambda x: sum(x), paraleloA))
#Unimos las listas
lista = list(zip(promedio, notatotal, nombres))
#Presentacion de resultados
print(list(filter(lambda x: x[0]<=5, lista)))