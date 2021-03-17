##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
lista = []
letters = []
numCol1 = []
with open("data.csv","r") as file:
    x = csv.reader(file, delimiter="\t")
    for data in x:
        lista.append((data[0],data[1]))
        letters.append(data[0])
letters = sorted(list(set(letters)))

for l in letters:
    cont = []
    for d in lista:
        if l == d[0]:
            cont.append(d[1])
    numCol1.append(cont)

for l in range(len(numCol1)):
    data = sorted(list(set(numCol1[l])))
    print(letters[l], max(data), min(data), sep=",")



