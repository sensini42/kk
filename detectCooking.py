#!/usr/bin/python
import sys
sys.path.append("/home_nfs/moulin/Desktop/home/outils/bin/PIL/lib/python2.5/site-packages/PIL")
import Image
import ImageDraw

if len(sys.argv)==1:
    print "Usage: python sys.argv[0] plateau.png"
    sys.exit(0)
nomPlateau=sys.argv[1]
plateau=Image.open(nomPlateau)

width, height = 25, 25
decx = 26
decy = 26

#draw = ImageDraw.Draw(plateau)
#for i in range(11):
# draw.line((decx+i*width,0,decx+i*width,plateau.size[1]), fill=128)
#for i in range(11):
# draw.line((0,decy+(i+1)*height,plateau.size[0],decy+(i+1)*height), fill=128)
#del draw 

for i in range(10):
 for j in range(10):
  crop=plateau.crop((decx+i*width,decy+(j+1)*height,decx+(i+1)*width,decy+(j+2)*height))
  plateauCrop=nomPlateau+"_"+str(i)+"_"+str(j)+".png"
  crop.save(plateauCrop)


