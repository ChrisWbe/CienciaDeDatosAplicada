##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas personas nacieron en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
csvcut -c birthdate person | grep -e -01- -e -02- -e -03- | wc -l