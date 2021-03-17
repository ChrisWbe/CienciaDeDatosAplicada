##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
month = []
with open("data.csv",'r') as file:
    x = csv.reader(file, delimiter="\t")
    for data in x:
        month.append(data[2].split("-")[1])
listM = sorted(list(set(month)))
for x in listM:
    print(str(x)+","+str(month.count(x)))
