#!/usr/bin/python
import sys
sys.path.append("/home_nfs/moulin/Desktop/home/outils/bin/PIL/lib/python2.5/site-packages/PIL")
import Image

if len(sys.argv)==1:
    print "Usage: python sys.argv[0] capture.png adetecter.png"
    sys.exit(0)
nomCapture=sys.argv[1]
nomADetecter=sys.argv[2]

capture=Image.open(nomCapture)
aDetecter=Image.open(nomADetecter)

widthC, heightC = capture.size
widthD, heightD = aDetecter.size

cont = False
jC = 0
while (jC < (heightC-heightD) and (not cont)):
  iC = 0
  while (iC < (widthC-widthD) and (not cont)):
    jD = 0
    cont = True
    while ((jD < heightD) and (cont)):
      iD = 0
      while ((iD < widthD) and (cont)):
        pixC=capture.getpixel((iC+iD,jC+jD))
        pixD=aDetecter.getpixel((iD,jD))
        if (pixC != pixD):
          cont = False
        iD+=1
      jD+=1
#    if (cont):
#      print ("x : %d y : %d" % (iC,jC))
    iC+=1
  jC+=1

iC+=widthD-1
jC+=heightD-1
#print "crop:",iC,jC,iC+300,jC+320
print str(iC)+":"+str(jC)

