##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas personas tienen 'AA' como iniciales de su nombre?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
csvcut -c fullname person |
cut -d " " -f1,2 | 
grep -e " A" | 
cut -d " " -f1 | 
grep -e A | wc -l