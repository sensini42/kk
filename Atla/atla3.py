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


import Image
import sys

if len(sys.argv)==1:
    print "Usage: python atla.py fichier.jpg [x y]"
    sys.exit(0)


img=Image.open(sys.argv[1])

if len(sys.argv)>2:
    x=int(sys.argv[2])
    y=int(sys.argv[3])
else:
    x=65
    y=335
#    x=61
#    y=329



a=img.crop((x,y,x+300,y+300))
#a.show()



## l=[[0]*15 for i in range(15)]

## for i in range(15):
##     for j in range(15):
##         a.putpixel((20*i+10,20*j+10),( 255,0,0)  )
##         a.putpixel((20*i+8,20*j+8),( 255,0,0)  )
##         a.putpixel((20*i+8,20*j+12),( 255,0,0)  )
##         a.putpixel((20*i+12,20*j+8),( 255,0,0)  )
##         a.putpixel((20*i+12,20*j+12),( 255,0,0)  )
## a.show()

## img=Image.open(sys.argv[1])



#a=img.crop((x,y,x+300,y+300))

larg,haut=15,15
l=[[0]*15 for i in range(15)]

def majo(l):
    zz={}
    for i in l:
        zz[i]=zz.get(i,0)+1
    kk=zz.keys()
    kk.sort(cmp=lambda a,b: cmp(zz[a],zz[b]))
    return kk[-1]

for i in range(15):
    for j in range(15):
        d=couleur(a.getpixel((20*j+10, 20*i+10 )))
        e=couleur(a.getpixel((20*j+8, 20*i+8 )))
        f=couleur(a.getpixel((20*j+8, 20*i+12 )))
        g=couleur(a.getpixel((20*j+12, 20*i+8 )))
        h=couleur(a.getpixel((20*j+12, 20*i+12 )))
        cc=majo([d,e,f,g,h])
        if (cc==VIDE and 1<i<13 and 1<j<13):
            cc=CIBLE
        l[i][j]=cc
        if (cc==TELEPORT):
#            d=couleur(a.getpixel((20*j+10, 20*i+10 )))
            e=couleur(a.getpixel((20*j+6, 20*i+6 )))
            f=couleur(a.getpixel((20*j+6, 20*i+14 )))
            g=couleur(a.getpixel((20*j+14, 20*i+6 )))
            h=couleur(a.getpixel((20*j+14, 20*i+14 )))
            gg=majo([e,f,g,h])
            if (gg==TELEPORT):
                l[i][j]=FANTOME

#Probleme de l'affichage du temps
l[13][13]=SOL
l[14][13]=VIDE
l[13][14]=VIDE
l[14][14]=VIDE


#for k in l:
#    print k



def affpix(i,j):
    d=(a.getpixel((20*j+10, 20*i+10 )))
    e=(a.getpixel((20*j+8, 20*i+8 )))
    f=(a.getpixel((20*j+8, 20*i+12 )))
    g=(a.getpixel((20*j+12, 20*i+8 )))
    h=(a.getpixel((20*j+12, 20*i+12 )))
    print i,j,(d,e,f,g,h),(couleur(d),couleur(e),couleur(f),couleur(g),couleur(h))
    
## for i in range(len(l)):
##     for j in range(len(l[i])):
##         if l[i][j]==7:
##             affpix(i,j)
##         if l[i][j]==1:
##             affpix(i,j)
            
## print l[8][11],
## affpix(8,11)

#for i in range(len(l[9])):
#    affpix(9,i)

def voisins(i,laby,pousse,larg,haut):
    v=[]
    j=i
    j-=1
    if ((not pousse) and laby[j]==CAISSE and laby[j-1]==SOL):
        la=laby[:]
        la[j]=SOL
        la[j-1]=CAISSE
        v.append((j,la,True))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j-=1
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby,pousse))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j+1,laby,pousse))
    j=i
    j+=1
    if ((not pousse) and laby[j]==CAISSE and laby[j+1]==SOL):
        la=laby[:]
        la[j]=SOL
        la[j+1]=CAISSE
        v.append((j,la,True))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j+=1
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby,pousse))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j-1,laby,pousse))
    j=i
    j+=larg
    if ((not pousse) and laby[j]==CAISSE and laby[j+larg]==SOL):
        la=laby[:]
        la[j]=SOL
        la[j+larg]=CAISSE
        v.append((j,la,True))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j+=larg
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby,pousse))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j-larg,laby,pousse))
    j=i
    j-=larg
    if ((not pousse) and laby[j]==CAISSE and laby[j-larg]==SOL):
        la=laby[:]
        la[j]=SOL
        la[j-larg]=CAISSE
        v.append((j,la,True))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j-=larg
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby,pousse))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j+larg,laby,pousse))
    return v


la=[]
for i in l: la.extend(i)
t1=-1
t2=-1
if (la.count(TELEPORT)!=0):
    if(la.count(TELEPORT)!=2 ):
        print "probleme teleport"
    t1=la.index(TELEPORT)
    t2=la.index(TELEPORT,t1+1)

if (la.count(FANTOME)>=1):
    print "probleme fantome?"
if (la.count(AUTRE)>=1):
    print "probleme autre?"

BLANC=0
GRIS=1
NOIR=2

pere=[-1 for i in range(larg*haut)]

laCoul=[BLANC for i in range(larg*haut)]

cible=-1
depart=-1

if DEPART in la:
    depart=la.index(DEPART)

if CIBLE in la:
    cible =la.index(CIBLE)

if CITROUILLE in la:
    depart=la.index(CITROUILLE)

if depart==-1:
    print "depart non trouve"
    sys.exit(1)

if cible==-1:
    print "cible non trouve"
    sys.exit(1)


pousse=False
aExplorer=[(depart,la,pousse)]


#stocke le chemin (par ex RDDRRRRRRUUUUURURUR)
#ch=[[""]]*(larg*haut)


#les voisins de la case exploree
voiz=[]

trouve=False

while(aExplorer!=[]):    
    (x,la2,pousse)=aExplorer.pop(0)
    voiz=voisins(x,la2,pousse,larg,haut)
    for (y,la3,pousse) in voiz:
        if laCoul[y]==BLANC and y!=x:
            laCoul[y]=GRIS
            pere[y]=x
            aExplorer.append((y,la3,pousse))
            if y==cible :
                trouve=True
                aExplorer=[]
                break
    laCoul[x]=NOIR

#print "depart cible",depart,cible
#for i in voisins(depart,la,larg,haut):
#    print i

#print pere

if trouve==False:
    print "pas trouve"
    sys.exit(1)

cur=cible
ch=""
while (cur!=-1 and cur!=pere[cur]):
    p=pere[cur]
    if p!=-1:
        if p>cur and p>=cur+15:
            ch="haut "+ch
        if p<cur and p<=cur-15:
            ch="bas "+ch
        if p>cur>p-15:
            ch="gauche "+ch
        if p<cur<p+15:
            ch="droite "+ch
    cur=pere[cur]

print ch
#sol= ch[fin]
#print sol






