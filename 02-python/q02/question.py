##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
lista = []
count = []
with open('data.csv','r') as file:
    x = csv.reader(file, delimiter='\t')
    for data in x:
        lista.append(data[0])
        
letters = sorted(list(set(lista)))
for e in letters:
    count.append(lista.count(e) )
for x in range(len(letters)):
    print(str(letters[x])+","+str(count[x])) 