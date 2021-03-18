##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
grep -e Jan -e Feb -e Mar *.txt | wc -l