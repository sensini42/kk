
import Image
import sys

if len(sys.argv)==1:
    print "Usage: python reglagle.py fichier.jpg [x y]"
    sys.exit(0)


img=Image.open(sys.argv[1])

if len(sys.argv)>2:
    x=int(sys.argv[2])
    y=int(sys.argv[3])
else:
    x=58
    y=331

a=img.crop((x,y,x+300,y+300))

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
