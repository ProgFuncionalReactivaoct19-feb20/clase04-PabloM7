"""
Manejo de colecciones y tuplas


# Encontrar la siguiente estructura
#

[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]

Dadas las siguientes estructuras:
@pablom7
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
#Usamos map para la iteracion de elementos y la funcion anonima con sum y len para encontrar el promedio de cada tupla
promedio = list(map(lambda x: sum(x)/len(x), paraleloA))
#Unimos la lista con zip
lista = list(zip(promedio, nombres))
#Presentacion de resultados
print(list(lista))