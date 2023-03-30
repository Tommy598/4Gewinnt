# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:13:01 2020
 
@author: Robin
"""
from random import randint
def spielfeld(liste,anzeige):
    print("")
    print("   ".join(anzeige))
    print("")
    print(liste[0])
    print(liste[1])
    print(liste[2])
    print(liste[3])
    print(liste[4])
    print(liste[5])

rdspieler = randint(1,2)
def Spieler(rdspieler):
    if rdspieler == 1:
        spieler = "X"
    elif rdspieler == 2:
        spieler = "O"
    return spieler

def spielereingabe():
    abbruch = 0
    inp = 0
    while not inp:
        eingabe = input(">>> Bitte Spalte angeben: ")
        if eingabe == "q":
            abbruch = 1
            inp = 1
            eingabe = 0
        else:
            try:
                eingabe = int(eingabe)
                if eingabe < 1 or eingabe > 7:
                    print()
                    print(">>> Überprüfe deine Eingabe.")
                else:
                    inp = 1
            except:
                print()
                print(">>> Bitte nur Zahlen angeben.")
                 
    return eingabe,abbruch
 
def spieleingabe_infeld(eingabe,spieler,liste):
    spw = 0
    b = 0
    ind1 = 5
    index = eingabe - 1
    while not b:
        if ind1 >= 0:
            if liste[ind1][index] == "X" or liste[ind1][index] == "O":
                ind1-=1
                b = 0
            else:
                liste[ind1][index] = spieler
                b = 1
                spw = 1
        else:
            print("")
            print("Diese Spalte ist voll.")
            b = 1
    return liste,spw
 
def spielerwechsel(spieler):
    if spieler == "X":
        spieler = "O"
    elif spieler =="O":
        spieler = "X"
    return spieler
 
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
       
 
def Spiel(rdspieler):
    anzeige = ["  1.","2.","3.","4.","5.","6.","7.","Spalte"]
    liste = [["~","~","~","~","~","~","~"],
             ["~","~","~","~","~","~","~"],
             ["~","~","~","~","~","~","~"],
             ["~","~","~","~","~","~","~"],
             ["~","~","~","~","~","~","~"],
             ["~","~","~","~","~","~","~"]]
    spieler = Spieler(rdspieler)
    schluss = 0
    while not schluss:
        while gewonnen(liste) == 0:
            if feldvoll(liste) == True:
                liste = [["~","~","~","~","~","~","~"],
                         ["~","~","~","~","~","~","~"],
                         ["~","~","~","~","~","~","~"],
                         ["~","~","~","~","~","~","~"],
                         ["~","~","~","~","~","~","~"],
                         ["~","~","~","~","~","~","~"]]
            else:
                spielfeld(liste,anzeige)
                print("")
                print(">>> Der Spieler",spieler,"ist am Zug.")
                wert = spielereingabe()
                eingabe = wert[0]
                if eingabe > 0:
                    wert1 = spieleingabe_infeld(eingabe, spieler,liste)
                    liste = wert1[0]
                    if wert1[1] == 1:
                        spieler = spielerwechsel(spieler)
                else:
                    schluss = 1
                 
        if gewonnen(liste) == 1:
            spielfeld(liste, anzeige)
            print("")
            print(">>> Wir Haben einen Sieger!!!")
            print(">>> Der Spieler",spielerwechsel(spieler),"hat 4-Gewinnt gewonnen.")
            schluss = 1
         
         
print()
print("Willkommen zum Spiel 4-Gewinnt !!!")
print("Der Spieler",Spieler(rdspieler),"beginnt das Spiel !!")
print()
Spiel(rdspieler)