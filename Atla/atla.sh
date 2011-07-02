#!/bin/bash

echo "La fenetre doit etre ouverte avec atlanteide dessus (mais faut pas lancer atlanteide hein)"


echo "Le prochain clic doit se faire sur la fenetre de atlanteide (sa position ne doit plus changer!)"

idfenetre=`xwininfo | grep "Window id:" | awk '{print $4}' `

import -window $idfenetre test-atla.jpg

x=58 #230
y=331 #420

python reglage.py test-atla.jpg $x $y
retour=$?

while [ $retour -ne 0 ]
do

  echo "valeur de x ?"
  read x
  echo "valeur de y ?"
  read y


  python reglage.py test-atla.jpg $x $y
  retour=$?

done

echo "Ok, un appui sur la touche entree, et c'est partiii"
echo "(q pr quitter...)"
read t
capture=0

while [ "$t" != "q" ]
do
capture=$(( $capture+1 ))
import -window $idfenetre atla.jpg
#cp atla.jpg atla4-$capture.jpg
python atla-lebon.py atla.jpg $x $y
echo $capture
read -n 1  t

done

echo " "
echo "si ca a pas eu le resultat attendu : tant pis =)"


unset retour
unset x
unset y
unset t
unset idfenetre
