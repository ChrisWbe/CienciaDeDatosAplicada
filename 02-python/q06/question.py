##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
from os import sep
col5 = []
listDicc = []
letters = []
num = []
with open("data.csv","r") as file:
    data = csv.reader(file, delimiter="\t")
    for row in data:
        col5.append(row[4].split(','))

for x in col5:
    for y in x:
        listDicc.append(y)
        letters.append(y.split(":")[0])

letters = sorted(list(set(letters)))
col5.clear()
for l in letters:
    count=[]
    for data in listDicc:
        if l == data.split(":")[0]:
            count.append(data.split(":")[1])
    col5.append(count)

for l in range(len(col5)):
    data = sorted(list(set(col5[l])))
    print(letters[l], min(data), max(data), sep=",")


