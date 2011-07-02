FRAISE=0
POMME=1
BANANE=2
ORANGE=3
CITRON=4
AUTRE=5
BORD=6
FIN=7

solAff=0

def afficheSolution(l,s,hg):
	global solAff
	if (solAff==0):
		solAff=1
		n=[[0]*(10-2*hg[0]) for i in range(8-2*hg[0])]
	
		for i in range(8):
			for j in range(10):
				e=[i,j]
				if (e in s):
					n[i-hg[0]][j-hg[0]]=s.index(e)+1
	
#	for i in range(hg[0],8-hg[0]):
#		for j in range(hg[0],10-hg[0]):
	
		for i in range(8-2*hg[0]):
			print n[i]	

def f2(seq):
	# order preserving
	checked = []
	for e in seq:
		if e not in checked:
			checked.append(e)
	return checked

def solution(l,m,hg,s,index,longueursolution):
	#print s	
	if (index==longueursolution):
		if (len(s)==len(f2(s))):
			#print s
			afficheSolution(l,s,hg)
	
	cur=s[index-1]
	h=cur[0]
	w=cur[1]

	#print h,w
	if (w+1<10 and l[h][w+1]==m[index]):
		s[index]=[h,w+1]
		solution(l,m,hg,s,index+1,longueursolution)

	if (h+1<8 and l[h+1][w]==m[index]):
		s[index]=[h+1,w]
		solution(l,m,hg,s,index+1,longueursolution)

	if (w-1>0 and l[h][w-1]==m[index]):
		s[index]=[h,w-1]
		solution(l,m,hg,s,index+1,longueursolution)

	if (h-1>0 and l[h-1][w]==m[index]):
		s[index]=[h-1,w]
		solution(l,m,hg,s,index+1,longueursolution)

def couleur((R,V,B)):
	if((R+V+B)>684 and V>224):
		return AUTRE
	else:
		if (R<150):
			return BORD
		else:
			if ((abs(R-150)+abs(V-150)+abs(B-150))<100):
				return FIN
			else:
				if(V>R):
					return CITRON
				else:
					if(B>V):
						return FRAISE
					else:
						if((V-B)<60):
							return POMME
						else:
							if((V-B)<150):
								return ORANGE
							else:
								return BANANE

import Image
import sys

if len(sys.argv)==1:
    print "Usage: python puzzlemanda.py fichier.jpg [x y]"
    sys.exit(0)

img=Image.open(sys.argv[1])

if len(sys.argv)>2:
    x=int(sys.argv[2])
    y=int(sys.argv[3])
else:
    x=58
    y=337


a=img.crop((x+3,y+59,x+302,y+301))

l=[[0]*10 for i in range(8)]
m=[[-1]*1 for i in range(10)]

for i in range(8):
	for j in range(10):
		l[i][j]=couleur(a.getpixel(((15+30*j),(15+30*i))))

if(l[7][5]==BORD):
	l[0]=l[7]
if(l[6][5]==BORD):
	l[1]=l[6]
if(l[5][5]==BORD):
	l[2]=l[5]

#for i in range(8):
#	print l[i]

hautgauche=[0,0]

if (l[0][0]==BORD):
	hautgauche=[1,1]
if (l[1][1]==BORD):
	hautgauche=[2,2]
if (l[2][2]==BORD):
	hautgauche=[3,3]

#print hautgauche

b=img.crop((x+3,y+28,x+302,y+29))

i=3
j=0
k=1
ok=0

while(i<299):
	coul=couleur(b.getpixel((i,0)))
	#print i,b.getpixel((i,0))
	if(ok==0 and coul==AUTRE):
		k=46
		ok=1
	else:
		if(ok==1 and i<299):
			coul=couleur(b.getpixel((i,0)))
			k=30
			if(coul!=FIN):
				m[j]=coul
				j=j+1
			else:
				k=300
	i=i+k

#print m

longueursolution=j
solAff=0

for i in range(hautgauche[0],8-hautgauche[0]):
	for j in range(hautgauche[0],10-hautgauche[0]):
		if (l[i][j]==m[0]):
			s=[[-1,-1]*1 for k in range(longueursolution)]
			s[0]=[i,j]
			solution(l,m,hautgauche,s,1,longueursolution)

print " "
print "---------------------------------"
print " "

