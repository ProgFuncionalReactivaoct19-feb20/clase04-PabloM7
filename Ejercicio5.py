"""
Manejo de colecciones y tuplas


# Encontrar la siguiente estructura
#

[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
(16.666666666666668, 'José')
[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]

 

Dadas las siguientes estructuras
@pablom7

"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
#Obtencion de promedios
promedios = list(map(lambda x:sum(x)/len(x) , paraleloA))
#Unimos los promedios con los nombres
resultados = list(zip(promedios,nombres))
#Identificamos al alumno con el mayor promedio
notamayor = max(resultados, key=lambda x:x)
#Presentamos los promedios con los nombres
print(resultados)
#Presentamos al alumno con el mayor promedio
print(notamayor)
print(list(sorted(resultados, key=lambda x:x[1])))