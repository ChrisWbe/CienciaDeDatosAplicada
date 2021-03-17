##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
letters = []
lista = []
with open("data.csv", "r") as file:
    data = csv.reader(file, delimiter="\t")
    for row in data:
        element = row[4].split(",")
        for e in element:
            letters.append(e.split(":")[0])

lista = sorted(list(set(letters)))

for l in lista:
    print(l,letters.count(l), sep=",")



