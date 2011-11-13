#!/bin/sh
old=$(pwd)
cd ~/Documents/git/kk/Flush
if [ ! -e flushee.html ];
then
  echo "Change main directory"
  exit
fi
if [ ! -e flushee.jar ];
then 
  mkdir bin
  javac -d bin flushee/Flushee.java
  javac -d bin flushee/Applet.java
  echo -ne "Manifest-Version: 1.0\nClass-Path: .\nMain-Class: flushee.Flushee\n" > bin/MANIFEST.MF
	cp flushee/*.png bin/flushee/
  cd bin
  jar -cfm ../flushee.jar MANIFEST.MF flushee
  cd -
  rm -rf bin
fi
java -jar flushee.jar
cd $old
