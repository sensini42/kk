#!/bin/bash

echo "La fenetre doit etre ouverte avec cooking lili dessus (mais faut pas lancer cooking lili hein)"


echo "Le prochain clic doit se faire sur la fenetre de cooking lili (sa position ne doit plus changer!)"

idfenetre=`xwininfo | grep "Window id:" | awk '{print $4}' `

import -silent -window $idfenetre test-puzzle.png
a=$(python detect.py test-puzzle.png adetecter.png)

x=${a%:*}
y=${a#*:}

echo "Ok, un appui sur la touche entree, et c'est partiii"
echo "(q pr quitter...)"
read t
capture=0

while [ "$t" != "q" ]
do
    capture=$(( $capture+1 ))
    import -silent -window $idfenetre puzzle.png
    python cooking.py puzzle.png $x $y
    read -n 1 t
    
done


unset retour
unset x
unset y
unset t
unset idfenetre
