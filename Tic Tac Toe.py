#Tic-Tac-Toe

spielfeld=["","1","2","3","4","5","6","7","8","9"]
def spielfeldausgabe():
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])

Name1=str(input("Spieler 1 geben Sie bitte Ihren Name ein: "))
Name2=str(input("Spieler 2 eben Sie bitte Ihren Name ein: "))


while True :
    spielfeldausgabe()
    Spieler1 =input( Name1 +" " "geben Sie eine Zahl ein ") #Spieler 1 gibt eine Zahl ein, die auf dem Spielfeld noch verfügbar ist.
    for i in spielfeld: #Mit der for Schleife gehe ich die Liste Spielfeld durch und suche damit die Zahl, die der Spieler 1 eingegeben hat.
        if Name1 == i: # Wenn die Zahl von Spieler 1 gleich ist wie i, dann soll die Zahl durch den ausgewählten Buchstabe des Spielers ersetzt werden.
            spielfeld[int(Spieler1)]="X"
# Die folgenden if Abfragen prüfen, ob eine Bedingung zutrifft. Wenn es zutrifft, hat ein Spieler gewonnen.
    if spielfeld[1] == "X" and spielfeld[2] == "X" and spielfeld[3] == "X":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[1] == "X"and spielfeld[4] == "X" and spielfeld[7] == "X":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[1] == "X" and spielfeld[5] == "X" and spielfeld[9] == "X":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[2] == "X" and spielfeld[5] == "X" and spielfeld[8] == "X":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[3] == "X" and spielfeld[6] == "X" and spielfeld[9] == "X":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[4] == "X" and spielfeld[5] == "X" and spielfeld[6] == "X":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[7] == "X" and spielfeld[8] == "X" and spielfeld[9] == "X":
        print("Spieler 2 hat gewonnen")
        break
# Hier wird geprüft, ob alle Felder mit "X" oder "o" belegt sind. Wenn alle Felder belegt sind und keiner 3 gleiche Symbole in
# in einer Reihe hat, hat keiner gewonnen.
    if (spielfeld[1] == "X" or spielfeld[1] == "o") and\
        (spielfeld[2] == "X" or spielfeld[2] == "o") and\
        (spielfeld[3] == "X" or spielfeld[3] == "o") and\
        (spielfeld[4] == "X" or spielfeld[4] == "o") and\
        (spielfeld[5] == "X" or spielfeld[5] == "o") and\
        (spielfeld[6] == "X" or spielfeld[6] == "o") and\
        (spielfeld[7] == "X" or spielfeld[7] == "o") and\
        (spielfeld[8] == "X" or spielfeld[8] == "o") and\
        (spielfeld[9] == "X" or spielfeld[9] == "o"):
        print("Leider hat keiner gewonnen")
        break
# Der weitere Code ist für den Spieler 2. Hier wurde der Code des ersten Teils übernommen, da es sich um die gleichen Befehle handelt.
#Der einzige Unterschied ist, dass bestimmte Variablen und Bedingungen geändert wurden.
# Beispielsweise wird das Zeichen "X" , welches für den Spieler 1 eingesetzt wurde, durch das Zeichen "o" ausgetauscht sowie die if-Bedingungen angepasst.
    spielfeldausgabe()
    Spieler2 = input( Name2 + " ""Wähle bitte eine freie Zahl aus")
    for j in spielfeld:
        if Name2 == "o"
            spielfeld[int(Spieler2)]="o"

    if spielfeld[1] == "o" and spielfeld[2] == "o" and spielfeld[3] == "o":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[1] == "o" and spielfeld[4] == "o" and spielfeld[7] == "o":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[1] == "o" and spielfeld[5] == "o" and spielfeld[9] == "o":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[2] == "o" and spielfeld[5] == "o" and spielfeld[8] == "o":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[3] == "o" and spielfeld[6] == "o" and spielfeld[9] == "o":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[4] == "o" and spielfeld[5] == "o" and spielfeld[6] == "o":
        print("Spieler 2 hat gewonnen")
        break
    if spielfeld[7] == "o" and spielfeld[8] == "o" and spielfeld[9] == "o":
        print("Spieler 2 hat gewonnen")
        break

    if (spielfeld[1] == "X" or spielfeld[1] == "o") and \
        (spielfeld[2] == "X" or spielfeld[2] == "o") and \
        (spielfeld[3] == "X" or spielfeld[3] == "o") and \
        (spielfeld[4] == "X" or spielfeld[4] == "o") and \
        (spielfeld[5] == "X" or spielfeld[5] == "o") and \
        (spielfeld[6] == "X" or spielfeld[6] == "o") and \
        (spielfeld[7] == "X" or spielfeld[7] == "o") and \
        (spielfeld[8] == "X" or spielfeld[8] == "o") and \
        (spielfeld[9] == "X" or spielfeld[9] == "o"):
        print("Leider hat keiner gewonnen")
        break