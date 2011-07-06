#!/usr/bin/python
import sys
sys.path.append("/home_nfs/moulin/Desktop/home/outils/bin/PIL/lib/python2.5/site-packages/PIL")
import Image
import ImageDraw
import math
import os
import shutil

def RGBtoHSV(R,G,B):
    # min, max, delta;
    min_rgb = min( R, G, B )
    max_rgb = max( R, G, B )
    V = max_rgb
    delta = max_rgb - min_rgb
    if not delta:
        H = 0
        S = 0
        V = R # RGB are all the same.
        return H,S,V
    elif max_rgb: # != 0
        S = delta / max_rgb
    else:
        R = G = B = 0 # s = 0, v is undefined
        S = 0
        H = 0 # -1
        return H,S,V
    if R == max_rgb:
        H = ( G - B ) / delta # between yellow & magenta
    elif G == max_rgb:
        H = 2 + ( B - R ) / delta # between cyan & yellow
    else:
        H = 4 + ( R - G ) / delta # between magenta & cyan
    H *= 60 # degrees
    if H < 0:
        H += 360
    return H,S,V




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

h,s,v = RGBtoHSV(RN,GN,BN)

print("%f %f %f" % (h,s,v))












