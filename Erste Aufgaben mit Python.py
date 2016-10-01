#Lecture with lists

#Hier wirst du dich ein wenig mit Python vertraut machen.


#Ich erzeuge eine Liste mit Namen und speicher diese unter dem Namen listeMitNamen
listeMitNamen = ["Peter","Paul","Max"]
#Jetzt gebe ich den Namen "Paul" aus.
print(listeMitNamen[1])


#Listen koennen auch Zahlen beinhalten.
listeMitZahlen = [1,2,3,4,5]
listeMitVielenZahlen = [0:100]


#Ich moechte einen Namen der Liste hinzufuegen. Ich mache das folgendermassen:
listeMitNamen.append("Pinky")

#Wenn ich jetzt listeMitNamen ausgebe, dann ist der Name "Pinky" mit enthalten.
"""
Aufgabe: Fuege der Liste deinen Namen hinzu.
"""


#Mit listeMitNamen[0:3] werden die ersten drei Elemente der Liste ausgegeben. Python zaehlt 0,1,2 wenn du ihm [0,3] sagst.

"""
Aufgabe: Gebe die ersten beiden Namen aus.
Aufgabe: Gebe die letzten beiden Namen aus.
"""




"""
Der string "PYTHON" hat sechs Buchstaben,
numeriert mit  0 bis 5, wie unten gezeigt:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

Wenn du den Buchstaben "H" haben moechtest, dann gebe
"PYTHON"[3] ein
"""

"""
Aufgabe: Erstelle eine Liste und waehle unterschiedliche Elemente aus.
Aufgabe: Finde heraus, was die folgenden Funktionen mit Listen machen: len()
lower()
upper()
pop()
"""



# Du kannst auch mehrere Listen und Wörter miteinander mit einem + verbinden.
print("Spam " + "and " + "eggs")

"""
Aufgabe: Versuche die Woerter "Pfadfinder","sind","cool" miteinander zu verbinden.
"""



string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


#Du kannst auch Methoden schreiben, die dann wieder in anderen Programmen verwendet werden koennen. 
#Diese Methoden beginnen immer mit deinem def. Nach dem def folgt der Name der Methode und danach 
#kommen immer (): In diese Klammer schreibt man rein, was die Methode braucht. In unserem Beispiel
#brauchen wir den Radius zum berechnen der Flaeche.
def flaecheKreis(Eingabe):
	A = 3.14*Eingabe
	print(A)

#Jetzt kannst du mit flaecheKreis(4), flaecheKreis(2), flaecheKreis(100), ... die jeweiligen Flaechen berechnen lassen.

"""
Aufgabe: schreibe eine Funktion, die den Flaecheninhalt eines gleichschenkligen Dreieecks berechnet.
	Formel: 0.5*Hypothenuse + Höhe
	Mache dir Gedanken wie die Formel berechnet wird und was in die Methode eingegeben werden muss.
"""
def flaecheDreieck():
	tmp = 0
	#hier muss was hin.


	
	
#Diese Funktion ist noch nicht fertig.
"""
Aufgabe: Schreibe diese Funktion so um, dass sie funktioniert:
"""
def Listenhalbierer(liste):
	liste1=[]
	liste2=[]
	print("Die erste Haelfte ist " + liste2 + "\n")
	print("Und dies die Zweite ")
	#Tipp: Es haben sich zwei Fehler eingeschlichen.




