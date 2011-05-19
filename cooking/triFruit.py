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

## if(RN<120 and BN<50):
##     shutil.copy(nomImage, "Vert/")
## elif(RN>180 and GN<100 and BN<100):
##     shutil.copy(nomImage, "Rouge/")
## elif(RN>220 and GN>180 and BN<80):
##     shutil.copy(nomImage, "Jaune/")

## elif(50<RN<100 and 105<GN<170 and BN<30):
##     shutil.copy(nomImage, "Vert/")
## elif(RN>220 and GN>180 and BN<80):
##     shutil.copy(nomImage, "Jaune/")
## elif(100<RN<160 and 25<GN<100 and 110<BN<220):
##     shutil.copy(nomImage, "Bleu/")
## elif(130<RN<170 and GN>200 and 195<BN<230):
##     shutil.copy(nomImage, "Blanc/")
## else:
##     shutil.copy(nomImage, "Autre/")
#print("%f %f %f" % (RN,GN,BN))

if(  (  52 < RN <  104 ) and ( 105 < GN < 161 ) and (   0 <= BN <  39 )):
    shutil.copy(nomImage,"Vert/")
elif((  75 < RN < 110 ) and ( 156 < GN < 193 ) and (  73 < BN <  92 )):
    shutil.copy(nomImage,"Gelvert/")
elif(( 197 < RN < 228 ) and (  27 < GN <  90 ) and (  25 < BN <  90 )):
    shutil.copy(nomImage,"Rouge/")
elif(( 177 < RN < 196 ) and (  91 < GN < 125 ) and (  91.5 < BN < 123 )):
    shutil.copy(nomImage,"Gelrouge/")
elif(( 224 < RN < 248 ) and ( 178 < GN < 242 ) and (  22 < BN <  91 )):
    shutil.copy(nomImage,"Jaune/")
elif(( 194 < RN < 210 ) and ( 213 < GN < 235 ) and ( 101 < BN < 124 )):
    shutil.copy(nomImage,"Geljaune/")
elif(( 102 < RN < 160 ) and (  31 < GN <  108 ) and ( 117 < BN < 228 )):
    shutil.copy(nomImage,"Bleu/")
elif(( 105 < RN < 185 ) and (  95 < GN < 156 ) and (  94 < BN < 227 )):
    shutil.copy(nomImage,"Gelbleu/")
elif(( 139 < RN < 166 ) and ( 199 < GN < 228 ) and ( 197 < BN < 231 )):
    shutil.copy(nomImage,"Blanc/")
else:
    shutil.copy(nomImage, "Autre/")














