##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
tuplas = []
numbers = []
with open("data.csv", "r") as file:
    data = csv.reader(file, delimiter="\t")
    for x in data:
        tuplas.append((x[0], x[1]))
        numbers.append(x[1])
numbers = sorted(list(set(numbers)))


for n in numbers:
    letters = []
    for t in tuplas:
        if n == t[1]:
            letters.append(t[0])
    print((n,letters))

#[print(listTupla[x]) for x in range(len(numbers))]


