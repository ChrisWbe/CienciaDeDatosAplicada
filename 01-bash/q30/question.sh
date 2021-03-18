##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas tienen el pin entre 980 y 990?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cat *.txt | 
csvcut -c pin | 
grep -e [9][8][0-9] -e 990 | 
wc -l