import sys
import math
dic = {}
n = int(input())
for i in range(n):
    inputs = input().split()
    b = inputs[0]
    c = int(inputs[1])
    dic[b] = chr(c)
ret = ""
curindex=0
toindex = 1
s = input()
while curindex + toindex < len(s)+1:
    if s[curindex:curindex+toindex] in dic:
        ret += dic[s[curindex:curindex+toindex]]
        curindex = curindex+toindex
        toindex = 1
    else:
        toindex+=1
if curindex<len(s):
    ret = "DECODE FAIL AT INDEX "+str(curindex)

print(ret)
