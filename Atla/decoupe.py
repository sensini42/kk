
import Image
import sys

if len(sys.argv)==1:
    print "Usage: python decoupe.py fichier.jpg"
    sys.exit(0)
nom=sys.argv[1]

img=Image.open(sys.argv[1])

if len(sys.argv)>2:
    x=int(sys.argv[2])
    y=int(sys.argv[3])
else:
    x=58
    y=331
x+=3
y+=3
a=img.crop((x,y,x+300,y+300))
VIDE=0
CITROUILLE=1
SOL=2
PIERRE=3
CAISSE=4
TELEPORT=5
CIBLE=6
AUTRE=7
DEPART=8
FANTOME=9

coul=["VIDE","CITROUILLE","SOL","PIERRE","CAISSE","TELEPORT","CIBLE","AUTRE","DEPART"]

def couleur((i,j,k)):
    if(i>200>150>j>100>50>k):
        return CITROUILLE
    else:
        if (i<j<k and 100<k):
            return VIDE
        else:
            if(i<115 and j<115 and k<115):
                return PIERRE
            else:   
                if(i>220 and j>220 and k>220):
                    return TELEPORT
                else:
                    if(i>j>k):
                        return CAISSE
                    else:
                        if( 140<i<220 and 140<j<220 and 140<k<220):
                            return SOL
                        else:
                            if( 195<i<230 and  195<j<230 and  195<k<230 ):
                                return DEPART
                            else:
                                return AUTRE


for i in range(15):
    for j in range(15):
        if ( (i!=14 and i!=15) and (j!=14 and j!=15)):
            b=a.crop((20*i,20*j,20*i+20,20*j+20))
            dossier=coul[couleur(b.getpixel((10,10)))]
            if (dossier=="VIDE" and 1<i<13 and 1<j<13):
                dossier="CIBLE"
            b.save(dossier+"/"+nom+str(i)+"_"+str(j)+".jpg")

sys.exit(0)
