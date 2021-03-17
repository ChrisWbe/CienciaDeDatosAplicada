##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
suma = 0
with open ('data.csv', 'r') as File:
    reader = csv.reader(File, delimiter='\t')
    for row in reader:
        suma += int(row[1])
print(suma)