import os
import time 
import sys
yellow = "\x1b[33m"
red="\x1b[31m"
reset = "\x1b[0m"
green = "\x1b[32m"
hide = "\x1b[?25l" 
show = "\x1b[?25h"
s = [(yellow+"  o  "+reset),
     (yellow+" /|\\ "+reset),
     (yellow+"  ^  "+reset)]
l = [(red+"  o  "+reset),
     (red+" /|\\  "+reset),
     (red+"  |  "+reset),]
l1 = [(green+"  o  "+reset),
     (green+" /|\\  "+reset),
     (green+"  ^  "+reset),]
sys.stdout.write(hide)
for c in range(6):

    os.system("cls")
    for i in range(len(s)):
        print(s[i])
    time.sleep(0.4)
    os.system("cls")
    for j in range(len(l)):
        print(l[j])
    time.sleep(0.4)
    os.system("cls")
    for z in range(len(l1)):
        print(l1[z])
    time.sleep(0.4)
    os.system("cls")
    for j in range(len(l)):
        print(l[j])
    time.sleep(0.4)
sys.stdout.write(show) 
    



