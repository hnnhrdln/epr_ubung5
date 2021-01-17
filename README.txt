__author__ = "5641727, Redelin, 6544078, Kervella"

1. Eine generelle Beschreibung des Projektes.

Dieses Programm implementiert die Logik eines Quartet-Kartenspiels.
Das User Interface ist die Console. Hier wird auch das Spiel gesteuert durch Eingaben des Nutzers.
Es kann zwischen 2 und 8 Spieler geben, die entweder durch den Nutzer oder den PC gesteuert werden. Diese Parameter
sowie die Namen der einzelnen Spieler werden zu Anfang des Spiels in der Funktion "setup" abgefragt. 

Nachdem die Eingaben auf Plausibilität gecheckt wurden, fährt das Spiel fort, indem das Kartendeck gemischt und an 
die Spieler verteilt wird. Im Falle von 2 Spielern erhält jeder Spieler 10 Karten, wobei 12 auf dem Kartenstapel verdeckt 
liegen bleiben. Bei mehr als 2 Spielern werden die Karten gleichmäßig an alle Spieler verteilt.

Bevor das tatsächliche Spiel beginnt wird in der Funktion "check_for_quartet" nach bereits vorhandenen Qartetten in den Händen 
der Spieler geprüft. Falls ein oder mehrere Qartette gefunden werden, wird ein einsprechender Counter im Profil der 
Spieler erhöht und die Karten abgelegt.

Das Herzstück des Programms ist die Funktion "implement_turn_logic". Hier werden die Spieler nacheinander dazu aufgefordert
einen anderen Mitspieler auszuwählen und nach einer bestimmten Karte zu fragen. In der Funktion "check_card" wird dann 
überprüft, ob diese Karte auf seiner Hand ist. Falls der Mitspieler über diese Karte verfügt, wird sie aus seiner Hand
entfernt und der Hand des derzeitigen Mitspielers gegeben. Danach wird erneut geprüft, ob sich neue Quartette gebildet haben.
Ist der Mitspieler nicht im Besitz der gewünschten Karte muss der Spieler in der Funktion "take_a_card" eine weitere Karte vom Stapel ziehen.
Bei einem menschlich gesteuerten Spieler geschiet dies wieder über Consoleneingaben. Im Falle eines durch den Computer 
gesteuerten Spielers werden zufällige Parameter gewählt.

Dieser Schritt wird so lange wiederholt bis mindestens ein Spieler keine Karten mehr auf der Hand hat. In diesem Fall
werden die Zahl der abgelegten Quartette aller Spieler verglichen. Der Spieler mit der größten Zahl an Quartetten 
gewinnt und das Programm wird beendet.

Während des Programmablaufs ist es dem Spieler aber immer möglich nach einer Eingabe das Spiel neu zu starten, zu beenden 
oder fortzusetzen. Falls das Spiel ausschließlich durch den Computer gespielt wird, ist das Spiel nach dem Setup nicht mehr
durch normale Eingaben zu beenden. Das Programm wird so lange durchlaufen, bis ein Spieler keine Karten mehr hat.


2. Eine Anleitung für die Installation und Bedienung.

Das Spiel verwendet ausschließlich Pythonbasismodule, daher müssen keine Installationen stattfinden.
Zum Start den Spiels muss das Kommando "python3 script.py" ausgeführt werden.

3. Weitere Annahmen.

-Wir nehmen an, dass bei einem Spiel mit jeder Spielerzahl ein Stapel vorhandne ist.
-Die Möglichkeit das Spiel neu zu starten oder zu beenden wird nach jeder Nutzereingabe durch einen Prompt ermöglicht.
-Doctests sind bei allen Funktionen gegeben, bei denen wir es für sinnvoll erachten. Z.B wäre der Input für die Funktion 
"implement_turn_logic" nicht reproduzierbar,weswegen wir uns hier dagegen entschieden haben.

4. Bekannte Bugs und eventuelle Fehlerbehebungen.

-Spieler mit dem gleichen Namen können für Probleme sorgen, kein Mitspieler mit dem gleichen Namen gewählt
werden kann. Im schlimmsten Fall auch zum Aufängen des Programms.
