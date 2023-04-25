
 
def gewonnen(liste):
    gew = 0
    for i in range(6):
        for j in range(4):
            w = "".join(liste[i])
            wertx = w.count("X",j,j+4)
            werto = w.count("O",j,j+4) 
            if wertx == 4 or werto == 4:
                gew=1
    for k in range(3):
        for h in range(7):
            if liste[k][h] == "X" and liste[k+1][h] == "X" and liste[k+2][h] == "X" and liste[k+3][h] == "X":
                gew = 1
            elif liste[k][h] == "O" and liste[k+1][h] == "O" and liste[k+2][h] == "O" and liste[k+3][h] == "O":
                gew = 1
    for l in range(3):
        for m in range(4):
            if liste[l][m] == "X" and liste[l+1][m+1] == "X" and liste[l+2][m+2] == "X" and liste[l+3][m+3] == "X":
                gew = 1
            elif liste[l][m] == "O" and liste[l+1][m+1] == "O" and liste[l+2][m+2] == "O" and liste[l+3][m+3] == "O":
                gew = 1
    for n in range(3):
        for o in range(4):
            if liste[n+3][o] == "X" and liste[n+2][o+1] == "X" and liste[n+1][o+2] == "X" and liste[n][o+3] == "X":
                gew = 1
            elif liste[n+3][o] == "O" and liste[n+2][o+1] == "O" and liste[n+1][o+2] == "O" and liste[n][o+3] == "O":
                gew = 1
    return gew
             
def feldvoll(liste):
    voll = False
    w1 = liste[0].count("~")
    if w1 == 0:
        voll = True
    return voll
       