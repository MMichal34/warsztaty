import sys
import math
win = False
tab = []
for i in range(3):
    tab.append(list(input()))
for a in range(3):
    counter = 0
    for b in range(3):
        if tab[a][b] == "O":
            counter+=1
        elif tab[a][b] == "X":
            counter-=1
    if counter == 2:
        win = True
        for b in range(3):
            if tab[a][b] ==".":
                tab[a][b] = "O"
if win:
    for x in range(len(tab)):
        print("".join(tab[x]))
else:
    for a in range(3):
        counter = 0
        for b in range(3):
            if tab[b][a] == "O":
                counter+=1
            elif tab[b][a] == "X":
                counter-=1
        if counter == 2:
            win = True
            for b in range(3):
                if tab[b][a] ==".":
                    tab[b][a] = "O"
    if win:
        for x in range(len(tab)):
            print("".join(tab[x]))
    else:
        counter = 0
        for a in range(3):
            if tab[a][a] == "O":
                counter+=1
            elif tab[a][a] == "X":
                counter-=1
        if counter == 2:
            win = True
            for a in range(3):
                if tab[a][a] ==".":
                    tab[a][a] = "O"
        if win:
            for x in range(len(tab)):
                print("".join(tab[x]))
        else:
            counter = 0
            for a in range(3):
                if tab[a][2-a] == "O":
                    counter+=1
                elif tab[a][2-a] == "X":
                    counter-=1
            if counter == 2:
                win = True
                for a in range(3):
                    if tab[a][2-a] ==".":
                        tab[a][2-a] = "O"
            if win:
                for x in range(len(tab)):
                    print("".join(tab[x]))
            else: print("false")


