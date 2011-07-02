
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
    x=230
    y=420

a=img.crop((x,y,x+280,y+140))

a.show()

print "est-ce que ca ressemble a quoi ca doit ressembler [yo/n] ?"

reponse=sys.stdin.read(1)

if (reponse!="y" and reponse!="o"):
    print "Changer la valeur de x et y (valeur courante:",x,y,")"
    sys.exit(1)

sys.exit(0)
