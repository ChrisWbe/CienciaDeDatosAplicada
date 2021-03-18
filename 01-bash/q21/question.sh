##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2181-4994-1181?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
ssn=$(cat bank.csv | grep "3608-2181-4994-1181" | cut -d "," -f 2 | sed 's/"//g')
fullname=$(cat person | grep $ssn | cut -d "," -f 5 | sed 's/"//g')
echo $fullname