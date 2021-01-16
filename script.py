"""Quartett"""
__author__ = "5641727, Redelin, 6544078, Kervella"

from random import shuffle
import time


def setup():
    players = []

    while True:
        try:
            number_of_players = int(input("How many players do you want to play with?"))
            break
        except ValueError:
            continue

    while isinstance(number_of_players, int) == False or number_of_players <= 0:
        number_of_players = int(input("How many players do you want to play with?"))

    for x in range(0, number_of_players):
        name = input("What is the name of player "+str(x+1)+"?\n")
        player_or_pc = input("Who is the player played by? [me/pc]\n")
        while player_or_pc != "me" and player_or_pc != "pc":
            player_or_pc = input("Try again! Who is the player played by? [me/pc]\n")

        if player_or_pc == "me":
            player_or_pc = True
        elif player_or_pc == "pc":
            player_or_pc = False

        player_tuple = (name, player_or_pc)

        players.append(player_tuple)

def shuffle():
    cards = ['7\u2665', '7\u2666', '7\u2663', '7\u2660',
    '8\u2665', '8\u2666', '8\u2663', '8\u2660',
    '9\u2665', '9\u2666', '9\u2663', '9\u2660',
    '10\u2665', '10\u2666', '10\u2663', '10\u2660',
    'J\u2665', 'J\u2666', 'J\u2663', 'J\u2660',
    'Q\u2665', 'Q\u2666', 'Q\u2663', 'Q\u2660',
    'K\u2665', 'K\u2666', 'K\u2663', 'K\u2660',
    'A\u2665', 'A\u2666', 'A\u2663', 'A\u2660']

    shuffle(cards)
    print("shuffling the cards ...")
    time.sleep(2)

    amount_of_cards = len(cards) 
    cards_per_player = int(amount_of_cards/number_of_players)
    rest = amount_of_cards % number_of_players  #Stapel
    print(cards)
    print("------------------")
    print("Amount of cards:",amount_of_cards)
    print("Cards per player:",cards_per_player)
    print("The rest is:",rest)
    print("------------------")

    for i in range(0,number_of_players):
        time.sleep(1)
        print("Player",i+1,"has the following cards:")
        print(cards[i*cards_per_player:(i+1)*cards_per_player])

if __name__ == '__main__':
    setup()
    shuffle()
