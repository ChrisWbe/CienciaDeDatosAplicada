##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'key' del archivo 'data.csv' para el 
##  registro 3?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
head -n 4 data.csv | tail -n 1 | cut -d "," -f 3 | sed 's/"//g'