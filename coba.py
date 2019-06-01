# 
# -*- coding: utf-8 -*-

import fileinput
import os
import sys
import time
from time import sleep

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0/90)

ask = G + '[' + W + '?' + G + '] ' + W
done = G + '[' + W + '√' + G + '] ' + W
salah = R + '[' + W + '!' + R + ']' + W
xerxez = G + '|' + W + '-' + G + '|' + W
xerxez2 = G + '[' + W + ':' + G + '] ' + W
slowprints("welcom!")
slowprints("SPESIAL Thank To Oficiql -2e3h-Buft-GblgCrew-BogorBlackHat")
os.system("pkg update")
os.system("sh sg2.sh")
print " PILIH 1/2";
slowprints("NANTI HASIL KAMU BISA TEMUI DI DIREKTORI AKU")
def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "-$ " + W)
       output = raw_input(ask + W + "Output " + G + "-$ " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (done + "^_^TER ENCEIFT GAN")
       print(xerxez2 + "SILAHKAN KAMU KETIK ls DAN CARI YANG ADI KAMU ENCRIPT")
   except KeyboardInterrupt:
       print (salah + " Jeda!")
   except IOError:
       print (salah + " Ngga ada file ya cuk!")


ngentot = raw_input(W + "InYourXerXez7-" + G + " $ " + W)

if ngentot == "1" or ngentot == "01":
   enkrip()
elif ngentot == "2" or ngentot == "02":
   exit()
else:
   print (eror + " Yang bener")
