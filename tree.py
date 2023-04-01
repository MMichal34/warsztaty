import sys
import math

n = int(input())
v = int(input())
m = int(input())
dic = {}
root = -1
def finding(tor,szuk,cur):
    if tor=="" and szuk==cur:
        return " Root"
    elif szuk == cur:
        return tor
    if cur not in dic:
        return ""
    z = finding(tor+" Left",szuk,dic[cur][0])
    x =  finding(tor+" Right",szuk,dic[cur][1])
    if z!="": return z
    if x!="": return x
    return ""
for i in range(m):
    p, l, r = [int(j) for j in input().split()]
    if root==-1:
        root = p
    dic[p] = [l,r]
print(finding("",v, root)[1:])
