##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantos registros quedan en el archivo 'person' si se eliminan los 
##  registros con 'city' = 'Anaheim (California)'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
csvcut -c city person | grep -v 'Anaheim (California)' | head -n -1 | wc -l