##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
with open("data.csv","r") as file:
    data = csv.reader(file,delimiter="\t")
    for row in data:
        col1 = row[0]
        col5 = row[4].split(",")
        cont = 0
        for e in col5:
            number = e.split(":")[1]
            cont+=int(number)
        print(col1,cont,sep=",")


