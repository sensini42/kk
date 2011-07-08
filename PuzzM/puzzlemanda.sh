#!/bin/bash

echo "La fenetre doit etre ouverte avec puzzlemanda dessus (mais faut pas lancer puzzlemanda hein)"


echo "Le prochain clic doit se faire sur la fenetre de puzzlemanda (sa position ne doit plus changer!)"

idfenetre=`xwininfo | grep "Window id:" | awk '{print $4}' `

import -window $idfenetre test-puzzle.jpg

x=58 #230
y=337 #420

python reglage.py test-puzzle.jpg $x $y
retour=$?

while [ $retour -ne 0 ]
do

echo "valeur de x ?"
read x
echo "valeur de y ?"
read y


python reglage.py test-puzzle.jpg $x $y
retour=$?

done

echo "Ok, un appui sur la touche entree, et c'est partiii"
echo "(q pr quitter...)"
read t
capture=0

while [ "$t" != "q" ]
do
capture=$(( $capture+1 ))
import -window $idfenetre puzzle.jpg
python puzzlemanda.py puzzle.jpg $x $y
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
