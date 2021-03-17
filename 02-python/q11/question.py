##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
lista=[]
letters=[]  
with open("data.csv", "r") as file:
    data = csv.reader(file, delimiter="\t")
    for row in data:
        lista.append((row[1],row[3]))
        element = row[3].split(",")
        for e in element:
            letters.append(e)
letters = sorted(list(set(letters)))

for l in letters:
    sum = 0
    for t in lista:
        number=t[0]
        elements=t[1]
        sum+=int(number)*int(elements.count(l))
    print(l,sum,sep=",")

