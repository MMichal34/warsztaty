import sys
import math

tab = []
for j in range(9):
    tab.append(list(map(int,input().split())))
tak = True
for j in range(9):
    spr = []
    for i in range(9):
        if tab[j][i] in spr:
            tak = False
        else:
            spr.append(tab[j][i])

for i in range(9):
    spr = []
    for j in range(9):
        if tab[j][i] in spr:
            tak = False
        else:
            spr.append(tab[j][i])

for i in range(3):
    for j in range(3):
        spr = []
        for x in range(3):
            for y in range(3):
                if tab[3*i+x][3*j+y] in spr:
                    tak = False
                else:
                    spr.append(tab[3*i+x][3*j+y])        

if tak:
    print("true")
else:
    print("false")
