#!/usr/bin/python 
import sys
sys.path.append("/home_nfs/moulin/Desktop/home/outils/bin/PIL/lib/python2.5/site-packages/PIL")
import Image


if len(sys.argv)==1:
    print "Usage: python reglagle.py fichier.jpg [x y]"
    sys.exit(0)


img=Image.open(sys.argv[1])

if len(sys.argv)>2:
    x=int(sys.argv[2])
    y=int(sys.argv[3])
else:
    print "Usage: python detec.py capture.jpg adetecter.png"
    print "Puis"
    print "python reglagle.py capture.jpg [x y]"
    sys.exit(0)

a=img.crop((x,y,x+300,y+320))

a.save("crop_"+sys.argv[1])

