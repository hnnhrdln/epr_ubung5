"""Quartett"""
__author__ = "5641727, Redelin, 6544078, Kervella"

from random import shuffle
import time, os, sys, random


def setup():
    players = []

    while True:
        try:
            number_of_players = int(input("How many players do you want to play with?"))
            break
        except ValueError:
            continue

    while isinstance(number_of_players, int) == False or number_of_players < 2 or number_of_players > 8:
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

        player_dict = {"name" : name, "player_or_pc": player_or_pc, "counter" : 0}

        players.append(player_dict)
    
    return number_of_players, players

def card_setup(number_of_players, players):
    cards = ['7\u2665', '7\u2666', '7\u2663', '7\u2660',
    '8\u2665', '8\u2666', '8\u2663', '8\u2660',
    '9\u2665', '9\u2666', '9\u2663', '9\u2660',
    '10\u2665', '10\u2666', '10\u2663', '10\u2660',
    'J\u2665', 'J\u2666', 'J\u2663', 'J\u2660',
    'Q\u2665', 'Q\u2666', 'Q\u2663', 'Q\u2660',
    'K\u2665', 'K\u2666', 'K\u2663', 'K\u2660',
    'A\u2665', 'A\u2666', 'A\u2663', 'A\u2660']

    #shuffle(cards)
    print("shuffling the cards ...")
    time.sleep(2)

    amount_of_cards = len(cards) 
    if number_of_players == 2:
        rest = 12
        cards_per_player = 10
        for i in range(0,number_of_players):
                time.sleep(1)
                print("Player",i+1,"has the following cards:")
                print(cards[i*cards_per_player:(i+1)*cards_per_player])
                players[i]["cards"] = cards[i*cards_per_player:(i+1)*cards_per_player]
        print("Stapel: ", cards[20:32])

    else:
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
            players[i]["cards"] = cards[i*cards_per_player:(i+1)*cards_per_player]
        print("The rest are:",cards[len(cards)-rest:len(cards)])

    return players

def restart_exit():
    restart = input("\nDo you want to restart the program? [y/n] > ")

    if restart == "y":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    else:
        print("\nThe programm will me closed...")
        sys.exit(0)

def check_for_quartet(cards):
    quartet =['7','8','9','10','J','Q','K','A']
    for player in cards:
        for x in quartet:
            result = [i for i in player["cards"] if i.startswith(x)]
            if len(result) == 4:
                player["counter"] +=1    
                for n in player["cards"][:]:
                    if n.startswith(x):
                        player["cards"].remove(n)
        print(player) #welche karten hatte der spieler danach
    
    return cards

def implement_turn_logic(players):
    people = []
    for player in players:
        people.append(player["name"])

    quartet =['7','8','9','10','J','Q','K','A']
    color = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
    
    for player in players:
        print("It's " +player["name"]+"'s turn.")
        #ckech of pc
        if player["player_or_pc"] == True: #mensch
            who = input("Who do you want to take a card from?")

            while who not in people or who == player["name"]:
                who = input("Select another player?")

            if who in people and who != player["name"]:
                which_number = input("Which number do you want?") #blablainput und so
                while which_number not in quartet:
                    which_number = input("Select another number?")

                if which_number in quartet:
                    which_color = input("Which color do you want?") #same blabla
                    while which_color not in color:
                        which_color = input("Select another color?")

                    if which_color in color:
                        if which_color == "HEARTS":
                            which_color = "\u2665"
                        elif which_color == "DIAMONDS":
                            which_color = "\u2666"
                        elif which_color == "CLUBS":
                            which_color = "\u2663"
                        elif which_color == "SPADES":
                            which_color = "\u2660"
                        which_card = which_number + which_color
                        print(which_card)

                        check_card(who, which_card,players, player)
                        check_for_quartet(players)

                    else:
                        print("falscher color inpout")
                else:
                    print("Wrong number-input")


            else:
                print("Again")     

        else: #pc  
            print("Selecting Bot Choices")        
                
            who_pc = random.choice(people)
            while who_pc == player["name"]:
                who_pc = random.choice(people)
            which_color_pc = random.choice(color)
            which_number_pc = random.choice(quartet)

            print(who_pc, which_color_pc, which_number_pc)  

            if which_color_pc == "HEARTS":
                which_color_pc = "\u2665"
            elif which_color_pc == "DIAMONDS":
                which_color_pc = "\u2666"
            elif which_color_pc == "CLUBS":
                which_color_pc = "\u2663"
            elif which_color_pc == "SPADES":
                which_color_pc = "\u2660"
            which_card_pc = which_number_pc+ which_color_pc
            print(which_card_pc)  

            check_card(who_pc, which_card_pc, players, player)
            check_for_quartet(players)
    

def check_card(who, which_card, players, player):  
    for element in players:
        if element["name"] == who:
            if which_card in element["cards"]:
                print("IS in deck")
                element["cards"].remove(which_card)
                player["cards"].append(which_card)
                print(element["cards"])
                print(player["cards"])
                return True
            else:
                print("Sorry, they dont have that card.")
                return False




if __name__ == '__main__':
    number_of_players, players = setup()
    players_setup = card_setup(number_of_players, players)
    players_ckecked_for_quartet = check_for_quartet(players_setup)
    while True:
        implement_turn_logic(players_ckecked_for_quartet)
