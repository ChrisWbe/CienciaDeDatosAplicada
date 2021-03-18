##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2596-5551-1068?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
ssn=$(cat bank.csv | grep "3608-2596-5551-1068" | cut -d "," -f 2)
fullname=$(cat person | grep $ssn |cut -d "," -f 5 | sed 's/"//g')
echo $fullname