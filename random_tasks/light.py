import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
tab = []
n = int(input())
l = int(input())
pola = [(x,y) for x in range(n) for y in range(n)]
def pokryj(x,y):
    for a in range(-l+1, l):
        for b in range(-l+1, l):
            if(y+a, x+b) in pola and tab[y+a][x+b]!="C":
                tab[y+a][x+b] = "O"
for i in range(n):
    tab.append(input().split())
for a in range(n):
    for b in range(n):
        if tab[a][b] == "C":
            pokryj(b, a)
#print(tab)
ile = 0
for q in range(n):
    for z in range(n):
        if tab[q][z] == "X":
            ile+=1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(ile)
