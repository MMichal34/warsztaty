import sys
import math
n = int(input())
start = [int(j) for j in input().split()]
dist = 0

curpoint=start.copy()
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
points=[]

for i in range(n-1):
    points.append([int(j) for j in input().split()])
while len(points)>0:
    t=[]
    for z in points:
        t.append([((z[0]-curpoint[0])**2+(z[1]-curpoint[1])**2)**0.5,z])
    t.sort()
    dist+=t[0][0]
    curpoint = t[0][1].copy()
    points.remove(t[0][1])
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
dist+=((start[0]-curpoint[0])**2+(start[1]-curpoint[1])**2)**0.5
dist = int(dist+0.5)
print(dist)
