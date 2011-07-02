#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
choisir le meilleur coup pour kaskade 2 (le plus de points + le plus
de points pour le prochain coup

tabCases grille principale, 00 en haut a gauche, 01: juste à droite…

"""

from random import choice
import sys

def afftab(tab):
    "affichage du tableau en couleur"
    col = ["\033[0m", "\033[1;41;31m", "\033[1;42;32m", "\033[1;44;34m"]
    for i in tab:
        for j in i:
            if j:
                sys.stdout.write(col[j]+"  "+col[0])
            else:
                sys.stdout.write("  ")
        print
        
def aff2tab(tab,tab2):
    "affichage du tableau en couleur"
    col = ["\033[0m", "\033[1;41;31m", "\033[1;42;32m", "\033[1;44;34m"]
    for (i,iii) in zip(tab, tab2):
        for j in i:
            if j:
                sys.stdout.write(col[j]+"  "+col[0])
            else:
                sys.stdout.write("  ")
        sys.stdout.write(" -> ")
        for j in iii:
            if j:
                sys.stdout.write(col[j]+"  "+col[0])
            else:
                sys.stdout.write("  ")
        print
        
def afftab2(tab):
    "affichage du tableau en couleur plus aéré"
    col = ["\033[0m", "\033[1;31m", "\033[1;32m", "\033[1;34m"]
    for i in tab:
        for j in i:
            if j:
                print col[j]+"#"+col[0],
            else:
                print " ",
        print

def afftab3(tab):
    "affichage du tableau en couleur"
    col = ["\033[0m", "\033[1;41;31m", "\033[1;42;32m", "\033[1;44;34m"]
    for i in tab:
        for j in i:
            if j:
                sys.stdout.write(col[j]+"[]"+col[0])
            else:
                sys.stdout.write("[]")
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

def rotateDroite(tab):
    "tourne vers la droite"
    ntab = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            ntab[i][7-j] = tab[j][i]
    return ntab

def rotateGauche(tab):
    "tourne à gauche"
    ntab = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            ntab[7-i][j] = tab[j][i]
    return ntab


def tasse(tab):
    "tasse le tableau vers le bas puis la gauche"
    #vers le bas
    #transpose, supprime les zéros, les ajoute à la fin
    ntab = rotateDroite(tab)
    for i in ntab:
        nzero = i.count(0)
        for _ in range(nzero):
            i.remove(0)
            i.append(0)
    #vers la gauche
    ntab = rotateGauche(ntab)
    for i in ntab:
        nzero = i.count(0)
        for _ in range(nzero):
            i.remove(0)
            i.append(0)
    return ntab
    
#
#grp = set([liste coord],[liste])
#
#
def groupes(tab):
    """retourne la liste des groupes (définis par l'ensemble des
    coordonées"""
    dgrp = {}
    ngrp = 1
    dgrp[(0, 0)] = ngrp
    for i in range(1, 8):
        #1ere ligne
        if tab[i - 1][0] == tab[i][0]:
            dgrp[(i, 0)] = dgrp[(i - 1, 0)]
        else:
            ngrp += 1
            dgrp[(i, 0)] = ngrp
        
    for j in range(1, 8):
        #1ere colonne
        if tab[0][j - 1] == tab[0][j]:
            dgrp[(0, j)] = dgrp[(0, j - 1)]
        else:
            ngrp += 1
            dgrp[(0, j)] = ngrp
        

    #le reste
    for i in range(1, 8):
        for j in range(1, 8):
            if tab[i - 1][j] == tab[i][j]:
                #la case a la mm couleur que celle haut dessus
                dgrp[(i, j)] = dgrp[(i - 1, j)]
                grph = dgrp[(i - 1, j)]
                grpg = dgrp[(i, j-1)]
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

def removeGrp(tab, listeCoord):
    "enleve le groupe de la tab (debogage)"
    ntab = [[tab[i][j] for j in range(8)] for i in range(8)]
    for (abs, ord) in listeCoord:
        ntab[abs][ord] = 0
    return ntab

def nbpoints(nbcases):
    "nb de point lorsque n cases sont enlevées"
    return (50 * nbcases * (nbcases - 1))


def quelgroupe(tab, dgrp, nbprevision):
    """quel groupe enlever pour faire le plus de points possible. Si
    nbprevision = 0, correspond au plus gros groupe. Si = 1 correspond
    a la somme des points du grp et du prochain. etc.
    Un groupe doit être au moins de taille 2."""
    #print tab, dgrp, nbprevision
    if nbprevision == 0:
        #critere d'arret
        gmax = max(dgrp, key = lambda x: len(dgrp[x]))
        return  (gmax, nbpoints(len(dgrp[gmax])))
    else:
        score = {}
        for grp in dgrp:
            if len(dgrp[grp]) > 1:
                score[grp] = nbpoints(len(dgrp[grp]))
                ntab = tasse(removeGrp(tab, dgrp[grp]))
                ngrp, nscore = quelgroupe(ntab, groupes(ntab), nbprevision - 1)
                score[grp] += nscore
        gmax = max(score, key = lambda x: score[x])
        return  (gmax, score[gmax])
        

noir = 0
rouge = 1
vert = 2
bleu = 3

if hasattr(sys, 'ps1'):
    aff = afftabNB
else:
    aff = afftab 

tabCases = [[choice([1, 2, 3]) for _ in range(8)] for _ in range(8)]

###a enlever
## tabCases[3][3] = 0
## tabCases[3][4] = 0
## tabCases[3][5] = 0
## tabCases[4][3] = 0

## aff(tabCases)
## print ""
## tabCases = tasse(tabCases)
###fin a enlever
aff(tabCases)

dicGrp = groupes(tabCases)

print "2 coups sans prévision:"
(grp, score) = quelgroupe(tabCases, dicGrp, 0)
ntab2 = (removeGrp(tabCases, dicGrp[grp]))
ntab = tasse(ntab2)
aff2tab(ntab2, ntab)
score = nbpoints(len(dicGrp[grp]))
print "coup 1:", len(dicGrp[grp]), "cases", score
(grp2, score2) = quelgroupe(ntab, groupes(ntab), 0)
nntab2 = (removeGrp(ntab, groupes(ntab)[grp2]))
nntab = tasse(nntab2)
aff2tab(nntab2, nntab)
score2 = nbpoints(len(groupes(ntab)[grp2]))
print "coup 2:", len(groupes(ntab)[grp2]), "cases", score2
print "total:", score + score2

print "2 coups 1 prévision:"
(grp, score) = quelgroupe(tabCases, dicGrp, 1)
ntab2 = (removeGrp(tabCases, dicGrp[grp]))
ntab = tasse(ntab2)
aff2tab(ntab2, ntab)
score = nbpoints(len(dicGrp[grp]))
print "coup 1:", len(dicGrp[grp]), "cases", score
(grp2, score2) = quelgroupe(ntab, groupes(ntab), 0)
nntab2 = (removeGrp(ntab, groupes(ntab)[grp2]))
nntab = tasse(nntab2)
aff2tab(nntab2, nntab)
score2 = nbpoints(len(groupes(ntab)[grp2]))
print "coup 2:", len(groupes(ntab)[grp2]), "cases", score2
print "total:", score + score2
