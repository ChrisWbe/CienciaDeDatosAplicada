##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q4 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
grep -e Oct -e Nov -e Dec *.txt | wc -l