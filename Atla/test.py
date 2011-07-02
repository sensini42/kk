
import Image
import sys

if len(sys.argv)==1:
    print "Usage: python reglagle.py fichier.jpg [x y]"
    sys.exit(0)


img=Image.open(sys.argv[1])
img2=Image.open(sys.argv[2])

if len(sys.argv)>3:
    x=int(sys.argv[3])
    y=int(sys.argv[4])
else:
    x=58
    y=331
##     x=230
##     y=420

x+=3
y+=3
a=img.crop((x,y,x+303,y+303))
b=img2.crop((x,y,x+303,y+303))

for i in range(a.size[0]):
    for j in range(a.size[1]):
        (r1,g1,b1)=a.getpixel((i,j))
        (r2,g2,b2)=b.getpixel((i,j))
#        a.putpixel((i,j),(abs(r1),abs(g2),abs(b2)))
        a.putpixel((i,j),(255-abs(r1-r2),255-abs(g1-g2),255-abs(b1-b2)))
        #a.putpixel((i,j),(255-abs(r1-r2),255-abs(g1-g2),255-abs(b1-b2)))

for i in range(15):
    for j in range(15):
        a.putpixel((20*i+10,20*j+10),( 255,0,0)  )
        a.putpixel((20*i+8,20*j+8),( 255,0,0)  )
        a.putpixel((20*i+8,20*j+12),( 255,0,0)  )
        a.putpixel((20*i+12,20*j+8),( 255,0,0)  )
        a.putpixel((20*i+12,20*j+12),( 255,0,0)  )
a.show()

print "est-ce que ca ressemble a quoi ca doit ressembler [yo/n] ?"

reponse=sys.stdin.read(1)

if (reponse!="y" and reponse!="o"):
    print "Changer la valeur de x et y (valeur courante:",x,y,")"
    sys.exit(1)

sys.exit(0)
