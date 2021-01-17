"""Quartett"""
__author__ = "5641727, Redelin, 6544078, Kervella"


import time, os, sys, random
random.seed(1234)

def setup():
    players = []

    while True:
        try:
            number_of_players = int(input("How many players do you want to play with?"))
            restart_exit()
            break
        except ValueError:
            continue

    while isinstance(number_of_players, int) == False or number_of_players < 2 or number_of_players > 8:
        number_of_players = int(input("How many players do you want to play with?"))
        restart_exit()

    for x in range(0, number_of_players):
        name = input("What is the name of player "+str(x+1)+"?\n")
        restart_exit()
        player_or_pc = input("Who is the player played by? [me/pc]\n")
        restart_exit()
        while player_or_pc != "me" and player_or_pc != "pc":
            player_or_pc = input("Try again! Who is the player played by? [me/pc]\n")
            restart_exit()

        if player_or_pc == "me":
            player_or_pc = True
        elif player_or_pc == "pc":
            player_or_pc = False

        player_dict = {"name" : name, "player_or_pc": player_or_pc, "counter" : 0}

        players.append(player_dict)
    
    return number_of_players, players

def card_setup(number_of_players, players):
    """setup of the cards with shuffle and the dealing of the cards to all the players
    number_of_players: amount of players playing the game
    players: dictionary with all the information of all the players
    >>> card_setup(2,({"name":'John',"cards":[]},{"name":'Elie',"cards":[]}))
    shuffling the cards ...
    Player 1 has the following cards:
    ['9♥', '10♣', '8♥', 'K♥', '8♣', 'J♥', '8♦', '10♠', 'K♠', 'Q♠']
    Player 2 has the following cards:
    ['10♥', '10♦', 'J♠', '9♦', '9♣', 'Q♥', 'J♦', 'K♣', 'A♦', '8♠']
    Deck of cards:  ['9♠', 'A♣', 'A♠', 'Q♣', 'Q♦', '7♦', 'J♣', 'K♦', '7♣', '7♥', '7♠', 'A♥']
    ({'name': 'John', 'cards': ['9♥', '10♣', '8♥', 'K♥', '8♣', 'J♥', '8♦', '10♠', 'K♠', 'Q♠']}, {'name': 'Elie', 'cards': ['10♥', '10♦', 'J♠', '9♦', '9♣', 'Q♥', 'J♦', 'K♣', 'A♦', '8♠']})
    >>> card_setup(3,({"name":'John',"cards":[]},{"name":'Elie',"cards":[]},{"name":'Lisa',"cards":[]}))
    shuffling the cards ...
    Player 1 has the following cards:
    ['8♣', '8♥', '8♦', '10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥']
    Player 2 has the following cards:
    ['10♣', 'K♣', 'K♦', '7♠', '9♣', '8♠', 'Q♠', '9♠', '10♠', '9♦']
    Player 3 has the following cards:
    ['Q♥', 'K♠', 'J♦', '9♥', '7♦', 'J♣', 'J♥', 'A♣', 'Q♦', 'J♠']
    Deck of cards: ['7♣', 'A♦']
    ({'name': 'John', 'cards': ['8♣', '8♥', '8♦', '10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥']}, {'name': 'Elie', 'cards': ['10♣', 'K♣', 'K♦', '7♠', '9♣', '8♠', 'Q♠', '9♠', '10♠', '9♦']}, {'name': 'Lisa', 'cards': ['Q♥', 'K♠', 'J♦', '9♥', '7♦', 'J♣', 'J♥', 'A♣', 'Q♦', 'J♠']})
    >>> card_setup(4,({"name":'John',"cards":[]},{"name":'Elie',"cards":[]},{"name":'Lisa',"cards":[]},{"name":'Marc',"cards":[]}))
    shuffling the cards ...
    Player 1 has the following cards:
    ['9♥', 'K♣', '10♦', 'Q♥', 'J♠', 'A♣', '8♠', 'A♥']
    Player 2 has the following cards:
    ['10♥', 'K♦', 'K♠', 'A♠', 'K♥', 'Q♠', 'Q♦', '10♣']
    Player 3 has the following cards:
    ['9♦', 'Q♣', 'J♥', '7♠', '9♠', '7♥', '8♥', '8♣']
    Player 4 has the following cards:
    ['J♦', 'A♦', '8♦', '10♠', 'J♣', '7♣', '7♦', '9♣']
    Deck of cards: []
    ({'name': 'John', 'cards': ['9♥', 'K♣', '10♦', 'Q♥', 'J♠', 'A♣', '8♠', 'A♥']}, {'name': 'Elie', 'cards': ['10♥', 'K♦', 'K♠', 'A♠', 'K♥', 'Q♠', 'Q♦', '10♣']}, {'name': 'Lisa', 'cards': ['9♦', 'Q♣', 'J♥', '7♠', '9♠', '7♥', '8♥', '8♣']}, {'name': 'Marc', 'cards': ['J♦', 'A♦', '8♦', '10♠', 'J♣', '7♣', '7♦', '9♣']})
    >>> card_setup(1,{"name": 'John',"cards":[]})
    shuffling the cards ...
    Error in the previous section of the Program.
    {'name': 'John', 'cards': []}
    >>>
    """
    cards = ['7\u2665', '7\u2666', '7\u2663', '7\u2660',
    '8\u2665', '8\u2666', '8\u2663', '8\u2660',
    '9\u2665', '9\u2666', '9\u2663', '9\u2660',
    '10\u2665', '10\u2666', '10\u2663', '10\u2660',
    'J\u2665', 'J\u2666', 'J\u2663', 'J\u2660',
    'Q\u2665', 'Q\u2666', 'Q\u2663', 'Q\u2660',
    'K\u2665', 'K\u2666', 'K\u2663', 'K\u2660',
    'A\u2665', 'A\u2666', 'A\u2663', 'A\u2660'] 

    random.shuffle(cards)
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
        print("Deck of cards: ", cards[20:32])
        deck_of_cards = cards[20:32]
        
    elif number_of_players < 2:
        print("Error in the previous section of the Program.")
        
    else:
        cards_per_player = int(amount_of_cards/number_of_players)
        rest = amount_of_cards % number_of_players  #Deck of cards

        for i in range(0,number_of_players):
            time.sleep(1)
            print("Player",i+1,"has the following cards:")
            print(cards[i*cards_per_player:(i+1)*cards_per_player])
            players[i]["cards"] = cards[i*cards_per_player:(i+1)*cards_per_player]
        print("Deck of cards:",cards[len(cards)-rest:len(cards)])
        deck_of_cards = cards[len(cards)-rest:len(cards)]

    return players, deck_of_cards

def restart_exit():
    restart = input("\nDo you want to restart the program? [y-restart/n-exit/any-continue] > ")

    if restart == "y":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    elif restart == "n":
        print("\nThe programm will me closed...")
        sys.exit(0)


def check_for_quartet(cards):
    """ Function to check if player has quartet and removing said quartet
    cards : list of cards
    """
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

def implement_turn_logic(players, deck_of_cards):
    """ Implementation of the game logic
    players: dictionary of the players and their cards/amount of quartets
    """
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
            restart_exit()

            while who not in people or who == player["name"]:
                who = input("Select another player?")
                restart_exit()

            if who in people and who != player["name"]:
                which_number = input("Which number do you want?") #blablainput und so
                restart_exit()
                while which_number not in quartet:
                    which_number = input("Select another number?")
                    restart_exit()

                if which_number in quartet:
                    which_color = input("Which color do you want?") #same blabla
                    restart_exit()
                    while which_color not in color:
                        which_color = input("Select another color?")
                        restart_exit()

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

                        check_card(who, which_card,players, player, deck_of_cards)
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

            check_card(who_pc, which_card_pc, players, player, deck_of_cards)
            check_for_quartet(players)
    

def check_card(who, which_card, players, player, deck_of_cards):
    """Checking if the asked player is in possesion of the asked card
    who: the person asked to give up a card
    which_card: the card asked for
    players: dictionary with all the data of all the players
    player: dictionary of the player receiving the potential card
    
    """
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
                print("Take a card:")
                take_a_card(deck_of_cards, players, player)
                return False

def take_a_card(deck_of_cards, players, player):
    if len(deck_of_cards) > 0:
        card = deck_of_cards[-1]
        player["cards"].append(card)
        deck_of_cards.remove(card) 
    else:
        print("Sorry, no more cards on the deck...")        

def _test():
    import doctest
    doctest.testmod()
          

if __name__ == '__main__':
    _test()
    number_of_players, players = setup()
    players_setup, deck_of_cards = card_setup(number_of_players, players)
    players_ckecked_for_quartet = check_for_quartet(players_setup)
    
    ending = True
    score = []
    while ending:
        implement_turn_logic(players_ckecked_for_quartet, deck_of_cards)
        for i, player in enumerate(players_ckecked_for_quartet):
            if len(player["cards"]) > 0:
                continue
            else:
                for player in players_ckecked_for_quartet:
                    score.append([player["name"], player["counter"]])
            
            if i < len(players_ckecked_for_quartet) - 1:
                compare_results(score)
                ending = False
