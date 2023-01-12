#!/usr/bin/env zsh

# modèle du travail
xinput set-button-map "Kensington Slimblade Trackball" 3 2 1 5 4
# modèle de la maison
xinput set-button-map "Kensington Kensington Slimblade Trackball" 3 2 1 5 4

# pour le moonlander, il y a 2 périphériques dans Virtual core pointer,
# on les modifie tous les 2 (pas vu de différence entre les 2)
for id in $(xinput list|head -6|grep -E "Moonlander"|grep -oP "id=\K[[:digit:]]+"); do
	xinput set-button-map $id 3 2 1 5 4 7 6
done

