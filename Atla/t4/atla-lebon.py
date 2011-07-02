
VIDE=0
CITROUILLE=1
SOL=2
PIERRE=3
CAISSE=4
TELEPORT=5
CIBLE=6
## AUTRE=7
DEPART=CITROUILLE
## FANTOME=9

coul=["vide","citrouille","sol","pierre","caisse","teleport","cible"]

def couleur(imagette,i,j):
    img=imagette
    h1=0
    h5=0
    for i in range(3,18):
        h1+=sum(img.getpixel((i,1)))/3
        h5+=sum(img.getpixel((i,5)))/3
    if ((2050<=h1<=2300) and (2050<=h5<=2300)):
        return CAISSE
    ##################################################
    r,v,b=0,0,0
    for i in range(5,16):
        r+=img.getpixel((i,3))[0]
        v+=img.getpixel((i,3))[1]
        b+=img.getpixel((i,3))[2]
    if ((2500<=r<=2800) and   (1100<=v<=1500) and (b<=300)      ):
       return CITROUILLE
    
    ##################################################
    r,v,b=0,0,0
    for i in range(5,16):
        r+=img.getpixel((i,10))[0]
        v+=img.getpixel((i,10))[1]
        b+=img.getpixel((i,10))[2]
    if  ((800<=r<=1300) and   (1400<=v<=1700) and (1300<=b<=1700) ):
        return VIDE
    ##################################################
    r,v,b=0,0,0
    for i in range(5,16):
        r+=img.getpixel((i,12))[0]
        v+=img.getpixel((i,12))[1]
        b+=img.getpixel((i,12))[2]
    if ((850<=r<=1100) and   (1300<=v<=1500) and   (1450<=b<=1630) ):
       return CIBLE
    ##################################################
    h10=0
    for i in range(5,16):
        h10+=sum(img.getpixel((i,8)))/3
    if ((h10<=1200) ):
        return PIERRE
    ##################################################
    h10=0
    h10+=sum(img.getpixel((10,10)))/3
    if (h10>240):
        last=sum(img.getpixel((2,10)))/3
        last2=sum(img.getpixel((18,10)))/3
        add=0
        for i in range(3,10):
            current=sum(img.getpixel((i,10)))/3
            current2=sum(img.getpixel((20-i,10)))/3
            if abs(current-current2)>35:
                return SOL
            add=add+abs(current-current2)
            last=current
            last2=current2
        if add>100:
            return SOL
        add=0
        last=sum(img.getpixel((10,5)))/3
        last2=sum(img.getpixel((10,15)))/3
        for i in range(5,10):
            current=sum(img.getpixel((10,i)))/3
            current2=sum(img.getpixel((10,20-i)))/3
            if abs(current-current2)>35 and current2>12:
                return SOL
            if current2>12:
                add=add+abs(current-current2)
            last=current
            last2=current2
        if add>100:
            return SOL
        return TELEPORT
    return SOL
 


    

##################################################



import Image
import sys

if len(sys.argv)==1:
    print "Usage: python sys.argv[0] fichier.jpg"
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

larg,haut=15,15
l=[[0]*15 for i in range(15)]


for i in range(15):
    for j in range(15):
        b=a.crop((20*i,20*j,20*i+20,20*j+20))
        cc=couleur(b,i,j)
        l[j][i]=cc

#Probleme de l'affichage du temps
l[13][13]=SOL
l[14][13]=VIDE
l[13][14]=VIDE
l[14][14]=VIDE


##################################################
for k in l:
    print k


## def affpix(i,j):
##     d=(a.getpixel((20*j+10, 20*i+10 )))
##     e=(a.getpixel((20*j+8, 20*i+8 )))
##     f=(a.getpixel((20*j+8, 20*i+12 )))
##     g=(a.getpixel((20*j+12, 20*i+8 )))
##     h=(a.getpixel((20*j+12, 20*i+12 )))
##     print i,j,(d,e,f,g,h),(couleur(d),couleur(e),couleur(f),couleur(g),couleur(h))

## print 13,12
## affpix(13,12)

## print 12,9
## affpix(12,9)

def voisins(i,laby,larg,haut):
    v=[]
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j-=1
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j+1,laby))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j+=1
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j-1,laby))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j+=larg
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j-larg,laby))
    j=i
    while(laby[j]==SOL or laby[j]==TELEPORT or laby[j]==CITROUILLE or laby[j]==DEPART):
        j-=larg
        if j==t1:
            j=t2
        else:
            if j==t2:
                j=t1
    if (laby[j]==CIBLE):
        v.append((j,laby))
    if (laby[j]==PIERRE or laby[j]==CAISSE):
        v.append((j+larg,laby))
    return v


def voisins_pouss(i,laby,pousse,larg,haut):
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
#    if(la.count(TELEPORT)!=2 ):
#        print "probleme teleport"
    t1=la.index(TELEPORT)
    t2=la.index(TELEPORT,t1+1)
#print "teleport:",t1,t2

BLANC=0
GRIS=1
NOIR=2

pere=[-1 for i in range(larg*haut)]

laCoul=[BLANC for i in range(larg*haut)]

depart=-1
if DEPART in la:
    depart=la.index(DEPART)

cible =la.index(CIBLE)

if CITROUILLE in la:
    depart=la.index(CITROUILLE)

if depart==-1:
    print "depart non trouve"
    sys.exit(1)


aExplorer=[(depart,la)]
voiz=[]
trouve=False

while(aExplorer!=[]):    
    (x,la2)=aExplorer.pop(0)
    voiz=voisins(x,la2,larg,haut)
    for (y,la3) in voiz:
        if laCoul[y]==BLANC and y!=x:
            laCoul[y]=GRIS
            pere[y]=x
            aExplorer.append((y,la3))
            if y==cible :
                trouve=True
                aExplorer=[]
                break
    laCoul[x]=NOIR
#print pere
#print "depart cible",depart,cible

if trouve==False:
    print "pas trouve sans pousse"
else:
    cur=cible
    ch=""
    while (cur!=-1 and cur!=pere[cur]):
        p=pere[cur]
        if p!=-1:
            if p>cur and (p/15==cur/15):
                ch="gauche "+ch
            else:
                if p<cur and (p/15==cur/15):
                    ch="droite "+ch
                else:
                    if p>cur and ((p-cur)%15==0):
                        ch="haut "+ch
                    else:
                        if p<cur and ((p-cur)%15==0):
                            ch="bas "+ch
                        else:
                            ch="TP "+ch
        cur=pere[cur]
    print ch



######################



BLANC=0
GRIS=1
NOIR=2

pere=[-1 for i in range(larg*haut)]

laCoul=[BLANC for i in range(larg*haut)]

depart=-1
if DEPART in la:
    depart=la.index(DEPART)

cible =la.index(CIBLE)

if CITROUILLE in la:
    depart=la.index(CITROUILLE)

if depart==-1:
    print "depart non trouve"
    sys.exit(1)


pousse=False
aExplorer=[(depart,la,pousse)]

#les voisins de la case exploree
voiz=[]

trouve=False

while(aExplorer!=[]):    
    (x,la2,pousse)=aExplorer.pop(0)
    voiz=voisins_pouss(x,la2,pousse,larg,haut)
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


if trouve==False:
    print "pas trouve tout court"
    sys.exit(1)

cur=cible
ch=""
while (cur!=-1 and cur!=pere[cur]):
    p=pere[cur]
    if p!=-1:
        if p>cur and (p/15==cur/15):
            ch="gauche "+ch
        else:
            if p<cur and (p/15==cur/15):
                ch="droite "+ch
            else:
                if p>cur and ((p-cur)%15==0):
                    ch="haut "+ch
                else:
                    if p<cur and ((p-cur)%15==0):
                        ch="bas "+ch
                    else:
                        ch="TP "+ch
    cur=pere[cur]
print ch
#sol= ch[fin]
#print sol






