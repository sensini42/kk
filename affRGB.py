#!/usr/bin/python
import sys
sys.path.append("/home_nfs/moulin/Desktop/home/outils/bin/PIL/lib/python2.5/site-packages/PIL")
import Image
import ImageDraw
import math
import os
import shutil

def distance (a,b):
 dist=0.0
 for i in range(len(a)):
  dist+=(a[i]-b[i])*(a[i]-b[i])
 return math.sqrt(dist)

if len(sys.argv)==1:
    print "Usage: python", sys.argv[0], "image.png"
    sys.exit(0)

nomImage=sys.argv[1]
image=Image.open(nomImage)

RN = 0.0
GN = 0.0
BN = 0.0

for i in range(image.size[0]/3,2*image.size[0]/3):
 for j in range(image.size[1]/3,2*image.size[1]/3):
  r,g,b=image.getpixel((i,j))
  RN+=r
  GN+=g
  BN+=b


RN/=image.size[0]/3*image.size[1]/3
GN/=image.size[0]/3*image.size[1]/3
BN/=image.size[0]/3*image.size[1]/3

print("%f %f %f" % (RN,GN,BN))












