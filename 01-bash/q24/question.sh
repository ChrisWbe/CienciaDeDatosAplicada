##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q3 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
grep -e Jul -e Aug -e Sep *.txt | wc -l