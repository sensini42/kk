#!/bin/bash

echo "La fenetre doit etre ouverte avec tubulo dessus (mais faut pas lancer tubulo hein)"


echo "Le prochain clic doit se faire sur la fenetre de tubulo (sa position ne doit plus changer!)"

idfenetre=`xwininfo | grep "Window id:" | awk '{print $4}' `

import -window $idfenetre test-tubu.jpg

x=70 #230
y=425 #420

python reglage.py test-tubu.jpg $x $y
retour=$?

while [ $retour -ne 0 ]
do

echo "valeur de x ?"
read x
echo "valeur de y ?"
read y


python reglage.py test-tubu.jpg $x $y
retour=$?

done

echo "Ok, un appui sur la touche entree, et c'est partiii"
echo "(q pr quitter...)"
read t
capture=0

while [ "$t" != "q" ]
do
capture=$(( $capture+1 ))
import -window $idfenetre tubu.jpg
python tubu.py tubu.jpg $x $y
echo $capture
read -n 1 -t 1 t

done

echo " "
echo "si ca a pas eu le resultat attendu : tant pis =)"


unset retour
unset x
unset y
unset t
unset idfenetre
