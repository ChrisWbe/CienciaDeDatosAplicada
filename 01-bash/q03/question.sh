##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'ccn' del archivo 'data.csv' para el primer 
##  registro?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
head -n 2 data.csv | 
tail -n 1 | 
cut -d "," -f1 | 
sed 's/"//g'