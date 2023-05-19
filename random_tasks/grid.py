import sys
import math

map = []
new = []

width, height = [int(i) for i in input().split()]
for i in range(height):
    map.append(input())
for i in range(height):
    t = ""
    for j in range(width):
        if map[i][j]=="#":
            t+="#"
        else:
            ile = 0
            if i>0 and map[i-1][j]!="#":
                ile+=1
            if j>0 and map[i][j-1]!="#":
                ile+=1
            if i<height-1 and map[i+1][j]!="#":
                ile+=1
            if j<width-1 and map[i][j+1]!="#":
                ile+=1
            t+=str(ile)
    print(t)
