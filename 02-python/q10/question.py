##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima una tabla en formato CSV que contenga 
##  por registro, la letra de la columna 1 y la cantidad de elementos de las 
##  columnas 4 y 5. 
## 
##  Rta/
##  E,3,5
##  A,3,4
##  B,4,4
##  ...
##  C,4,3
##  E,2,3
##  E,3,3
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv

with open("data.csv", "r") as file:
    data = csv.reader(file, delimiter="\t")
    for x in data:
        col1 = x[0]
        col4 = len(x[3].split(","))
        col5 = len(x[4].split(","))
        print(col1,col4,col5, sep=",")


