##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
lista = []
letters = []
with open("data.csv","r") as file:
    x = csv.reader(file,delimiter='\t')
    for data in x:
        lista.append((data[0],data[1]))
        letters.append(data[0])
    letters = sorted(list(set(letters)))
for x in letters:
    sum = 0
    for y in lista:
        if x == y[0]:
            sum+=int(y[1])
    print(str(x)+","+str(sum))




