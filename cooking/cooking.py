#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
choisir le meilleur coup pour cooking lili

tabCases grille principale, 00 en haut a gauche, 01: juste à droite…
"""

import sys
sys.path.append("/home_nfs/moulin/Desktop/home/outils/bin/PIL/lib/python2.5/site-packages/PIL")
import Image
import ImageDraw
import os
import shutil

AA=0
def coulFruit(RN, GN, BN):
    if ((RN < 120)  and (90 < GN < 180) and (BN < 50)):
        return vert
    elif((50 < RN < 110) and (130 < GN < 200) and (50 < BN < 95)):
        return -vert
    elif((180 < RN) and (GN < 100) and (BN < 100)):
        return rouge
    elif((170 < RN < 200) and (80 < GN < 140) and (80 < BN < 140)):
        return -rouge
    elif((210 < RN) and (175 < GN) and (BN < 90)):
        return jaune
    elif((180 < RN < 220) and (200 < GN) and (90 < BN < 140)):
        return -jaune
    elif((90 < RN < 170) and (20 < GN < 105) and (100 < BN < 225)):
        return bleu
    elif((90 < RN < 190) and (80 < GN < 150) and (85 < BN)):
        return -bleu
    elif((125 < RN < 175) and (195 < GN) and (180 < BN)):
        return blanc
    else:
        return noir
    


## noir = 0
## rouge = 1
## vert = 2
## jaune = 3
## bleu = 4
## blanc = 5
## gelblanc = -5
## etc
## gelrouge = -1

col = ["\033[0m", "\033[1;41;31m", "\033[1;42;32m", "\033[1;43;33m",
       "\033[1;44;34m", "\033[1;47;37m"]
col2 = ["\033[0m", "\033[1;40;31m", "\033[1;40;32m", "\033[1;40;33m",
        "\033[1;40;34m", "\033[1;40;37m"]
pieces = [col[j] + "  " + col[0] for j in range(6)]
pieceswap = [col[j]  + "[]" + col[0] for j in range(6)]
piecestop = [col[j] + "!!" + col[0] for j in range(6)]
piecestop[0] = "  "
for j in range(5, 0, -1):
    pieces.append(col[j] + "##" + col[0])
    pieceswap.append(col[j] + "{}" + col[0])
    piecestop.append(col[j] + "!!" + col[0])

from random import choice



def copie(tab):
    "retourne une copie du tableau"
    tab2= [[tab[i][j] for j in range(10)] for i in range(10)]
    return tab2


def afftab(tab):
    "affichage du tableau en couleur"
    for i in tab:
        for j in i:
            sys.stdout.write(pieces[j])
        print
    print
    
def affswap(tab, coord):
    "affichage du tableau en couleur, mise en évidence d'une paire"
    for (ki, i) in enumerate(tab):
        for (kj, j) in enumerate(i):
            if((ki, kj) in coord):
                sys.stdout.write(pieceswap[j])
            else:
                sys.stdout.write(pieces[j])
        print
    print
    
    
def aff2tab(tab,tab2):
    "affichage des tableaux en couleur (avant après)"
    for (i, iii) in zip(tab, tab2):
        for j in i:
            sys.stdout.write(pieces[j])
        sys.stdout.write(" -> ")
        for j in iii:
            sys.stdout.write(pieces[j])
        print
    print


def afftabNB(tab):
    "affichage du tableau en NB en console python"
    for i in tab:
        for j in i:
            if j:
                print j,
            else:
                print " ",
        print
    print

def rotateDroite(tab):
    "tourne vers la droite"
    ntab = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            ntab[i][9 - j] = tab[j][i]
    return ntab

def rotateGauche(tab):
    "tourne à gauche"
    ntab = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            ntab[9 - i][j] = tab[j][i]
    return ntab


def tasse(tab):
    "tasse le tableau"
    #transpose, supprime les zéros, les ajoute à la fin
    ntab = rotateDroite(tab)
    for i in ntab:
        nzero = i.count(0)
        for _ in range(nzero):
            i.remove(0)
            i.append(0)
    ntab = rotateGauche(ntab)
    return ntab

def groupes(tab):
    """retourne la liste des groupes (définis par l'ensemble des
    coordonées"""
    dgrp = {}
    ngrp = 1
    dgrp[(0, 0)] = ngrp
    for i in range(1, 10):
        #1ere ligne
        if tab[i - 1][0] == tab[i][0]:
            dgrp[(i, 0)] = dgrp[(i - 1, 0)]
        else:
            ngrp += 1
            dgrp[(i, 0)] = ngrp
        
    for j in range(1, 10):
        #1ere colonne
        if tab[0][j - 1] == tab[0][j]:
            dgrp[(0, j)] = dgrp[(0, j - 1)]
        else:
            ngrp += 1
            dgrp[(0, j)] = ngrp
    
    #le reste
    for i in range(1, 10):
        for j in range(1, 10):
            if tab[i - 1][j] == tab[i][j]:
                #la case a la mm couleur que celle haut dessus
                dgrp[(i, j)] = dgrp[(i - 1, j)]
                grph = dgrp[(i - 1, j)]
                grpg = dgrp[(i, j - 1)]
                if (tab[i][j - 1] == tab[i][j]) and grph != grpg:
                    #et mm couleur que celle a gauche: fusion de groupe
                    for grp in dgrp:
                        if dgrp[grp] == grpg:
                            dgrp[grp] = grph
            elif tab[i][j - 1] == tab[i][j]:
                #la case a la mm couleur que celle a gauche
                dgrp[(i, j)] = dgrp[(i, j - 1)]
            else:
                #la case a une nouvelle couleur: nv grp
                ngrp += 1
                dgrp[(i, j)] = ngrp
                
    invDic = {}
    for key, val in dgrp.iteritems():
        if (tab[key[0]][key[1]] != 0):
            invDic[val] = invDic.get(val, [])
            invDic[val].append(key)
    return invDic

def groupesSuperieurA2(tab):
    "dico des grp de taille sup a 2"
    dicoGrp = groupes(tab)
    dico = {}
    for (i,j) in dicoGrp.items():
        if (len(j) > 2):
            dico[i] = j
    return dico


def removeGrpDegele(tab, listeCoord):
    "enleve le groupe du tab"
    ntab = copie(tab)
    for (absc, ordo) in listeCoord:
        ntab[absc][ordo] = 0
        if(0 < absc):
            ntab[absc - 1][ordo] = abs(ntab[absc - 1][ordo])
        if(absc < len(ntab) - 1):
            ntab[absc + 1][ordo] = abs(ntab[absc + 1][ordo])
        if(0 < ordo):
            ntab[absc][ordo - 1] = abs(ntab[absc][ordo - 1])
        if(ordo < len(ntab[0]) - 1):
            ntab[absc][ordo + 1] = abs(ntab[absc][ordo + 1])
            
    return ntab

def nbpoints(nbcases, nbcombo, fruit):
    "nb de points lorsque n cases sont enlevées (pas de fruit++ pour l'instant)"
    if(fruit == bleu):
        nbcombo += 1
    if(fruit == blanc):
        nbcombo += 2
    somme = 70
    for i in range(4, nbcases + 1):
        somme += 5 * ((i - 3) ** 2) + 30 * (i - 3) + 45
    return somme * nbcombo



def swappePaire2(tab, coupleCoord):
    "retourne le nb de pt après avoir swapper la paire"
    return swappePaireDebug2(tab, coupleCoord, 0)

def swappePaireDebug2(tab, coupleCoord, debug=False):
    "retourne le nb de pt après avoir swapper la paire (affiche le tableau)"
    ntab = copie(tab)
    if debug:
        affswap(ntab,coupleCoord)
    ((i1, j1), (i2, j2)) = coupleCoord
    ntab[i1][j1], ntab[i2][j2] = ntab[i2][j2], ntab[i1][j1]
    fini = 0
    iteration = 0
    nbpoint = 0
    if debug:
        affswap(ntab, coupleCoord)
    while(not fini):
        if debug:
            print iteration, nbpoint
        nntab = copie(ntab)
        grp = groupesSuperieurA2(ntab)
        if(grp != {}):
            iteration += 1
        for i, j in grp.items():
            nbpoint += nbpoints(len(j), iteration, ntab[j[0][0]][j[0][1]])
            ntab = removeGrpDegele(ntab, j)
        if debug:
            aff3tab(nntab, ntab, tasse(ntab))
        ntab = tasse(ntab)
        if(nntab == ntab):
            fini = 1
    return (ntab, nbpoint)

def ListePaire(tab):
    """quelle paire swapper pour faire le plus de points."""
    #print tab, dgrp, nbprevision
    listePaire = []
    for (ki, i) in enumerate(tab):
        for (kj, j) in enumerate(i):
            if(kj < len(i) - 1):
                if j and tab[ki][kj + 1]:
                    listePaire.append(((ki, kj), (ki, kj + 1)))
            if(ki < len(tab) - 1):
               if j and tab[ki + 1][kj]:
                    listePaire.append(((ki, kj), (ki + 1, kj)))
    best = []
    for coord in listePaire:
        (ntab, score) = swappePaire2(tab, coord)
        best.append((coord, score, ntab))
    best = sorted(best, key=lambda x: x[1])
    return best
    
if hasattr(sys, 'ps1'):
    aff = afftabNB
else:
    aff = afftab 

def tabApresSwap(tab, coupleCoord):
    "retourne le tab et le nombre de point si on swappe cC"
    ntab = copie(tab)
    ((i1, j1), (i2, j2)) = coupleCoord
    ntab[i1][j1], ntab[i2][j2] = ntab[i2][j2], ntab[i1][j1]
    fini = 0
    iteration = 0
    nbpoint = 0
    while(not fini):
        nntab = copie(ntab)
        grp = groupesSuperieurA2(ntab)
        if(grp != {}):
            iteration += 1
        for i,j in grp.items():
            nbpoint += nbpoints(len(j), iteration, ntab[j[0][0]][j[0][1]])
            ntab = removeGrpDegele(ntab, j)
        ntab = tasse(ntab)
        if(nntab == ntab):
            fini = 1
    return (nntab, nbpoint)

def affswapEtRes(tab, coord, nbp, res):
    "affichage du tableau avec la paire et le résultat"
    print "-" * 44
    print nbp,
    if res[0] != [0] * 10:
        print  col[1] + "perdu" + col[0],
    print
    for ((ki, i), i2) in zip(enumerate(tab), res):
        for (kj, j) in enumerate(i):
            if((ki, kj) in coord):
                sys.stdout.write(pieceswap[j])
            else:
                sys.stdout.write(pieces[j])
        if ki == 0:
            sys.stdout.write(" " + col[1] + "->" + col[0] + " ")
        else:
            sys.stdout.write(" -> ")
        for j in i2:
            if ki == 0:
                sys.stdout.write(piecestop[j])
            else:
                sys.stdout.write(pieces[j])
        print
    print
    
noir = 0
rouge = 1
vert = 2
jaune = 3
bleu = 4
blanc = 5

tabCases = [
    [-4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 1, 1, 3, 1, 3, 1, 3],
    [2, 3, 1, 3, 3, 2, 2, 1, 2, 3],
    [3, 1, 3, 2, 2, 1, 1, 3, 1, 2],
    [3, 2, 1, 3, 1, 3, 3, 1, 2, 1],
    [2, 1, 2, 2, 1, 2, 1, 3, 1, 3],
    [-4, 3, 1, 1, 3, 3, 2, 1, 2, 1],
    [-5, 1, 3, 3, 2, 1, 3, 1, 2, 3],
    [3, 1, 2, 1, 3, 1, 3, 2, 3, 2],
#    [1, 3, 1, 1, 3, 3, 2, 1, 2, 1],
#    [3, 1, 3, 3, 2, 1, 3, 1, 2, 3],
#    [3, 1, 2, 1, 3, 1, 3, 2, 3, 2],
    ]

## tabCases = [
##     [1,2,1,1,3,1,2,3,1,0],
##     [1,3,3,2,2,3,2,1,3,1],
##     [2,2,1,3,3,1,1,3,2,3],
##     [1,3,2,-1,2,3,2,1,2,1],
##     [3,2,3,-3,2,3,2,3,1,3],
##     [-3,2,1,1,3,1,1,3,2,1],
##     [2,1,2,4,-4,-4,3,5,1,2],
##     [1,2,3,2,1,1,2,1,2,1],
##     [2,1,3,2,3,2,5,-5,3,3],
##     [1,-3,1,1,3,1,1,2,1,2]
##     ]
#http://www.dailymotion.com/video/x3w81e_cooking-lili-54810_videogames

if len(sys.argv) >= 2:
    nomPlateau = sys.argv[1]
    plateau = Image.open(nomPlateau)
    cropx = int(sys.argv[2])
    cropy = int(sys.argv[3])
    width, height = 25, 25
    decx = 26
    decy = 26


    for i in range(10):
        for j in range(10):
    #       crop=plateau.crop((cropx + decx + i*width, decy + (j+1)*height, decx + (i+1)*width, decy + (j+2)*height))
            RN = 0.0
            GN = 0.0
            BN = 0.0
            decImgX=cropx + decx + i*width
            decImgY=cropy + decy + (j+1)*height
            for ii in range(width / 3, 2 * width / 3):
                for jj in range(height / 3, 2 * height / 3):
                    r, g, b = plateau.getpixel((ii + decImgX, jj + decImgY))
                    RN+=r
                    GN+=g
                    BN+=b


            RN /= (width / 3) * (height / 3)
            GN /= (width / 3) * (height / 3)
            BN /= (width / 3) * (height / 3)
            tabCases[j][i] = coulFruit(RN, GN, BN)



#afftab(tabCases)
listeComplete = ListePaire(tabCases)
listeNonPerdu = filter(lambda x: x[2][0] == [0] * 10 , listeComplete[:-1])
meilleurPuisNonPerdu = listeNonPerdu + [listeComplete[-1]]
for itemPaire in meilleurPuisNonPerdu[-3:]:
    affswapEtRes(tabCases, itemPaire[0], itemPaire[1], itemPaire[2])

(t, n)=tabApresSwap(tabCases, ((-1, -1), (-1, -1)))
    
if (t != tabCases):
    print (col[1] + "/!\ La detection contient un bug!!!" + col[0])
