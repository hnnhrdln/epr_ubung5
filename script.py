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
    ---------------------------------
    shuffling the cards ...
    ---------------------------------
    John has the following cards:
    ['9♥', '10♣', '8♥', 'K♥', '8♣', 'J♥', '8♦', '10♠', 'K♠', 'Q♠']
    Elie has the following cards:
    ['10♥', '10♦', 'J♠', '9♦', '9♣', 'Q♥', 'J♦', 'K♣', 'A♦', '8♠']
    Deck of cards:  ['9♠', 'A♣', 'A♠', 'Q♣', 'Q♦', '7♦', 'J♣', 'K♦', '7♣', '7♥', '7♠', 'A♥']
    (({'name': 'John', 'cards': ['9♥', '10♣', '8♥', 'K♥', '8♣', 'J♥', '8♦', '10♠', 'K♠', 'Q♠']}, {'name': 'Elie', 'cards': ['10♥', '10♦', 'J♠', '9♦', '9♣', 'Q♥', 'J♦', 'K♣', 'A♦', '8♠']}), ['9♠', 'A♣', 'A♠', 'Q♣', 'Q♦', '7♦', 'J♣', 'K♦', '7♣', '7♥', '7♠', 'A♥'])
    >>> card_setup(3,({"name":'John',"cards":[]},{"name":'Elie',"cards":[]},{"name":'Lisa',"cards":[]}))
    ---------------------------------
    shuffling the cards ...
    ---------------------------------
    John has the following cards:
    ['8♣', '8♥', '8♦', '10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥']
    Elie has the following cards:
    ['10♣', 'K♣', 'K♦', '7♠', '9♣', '8♠', 'Q♠', '9♠', '10♠', '9♦']
    Lisa has the following cards:
    ['Q♥', 'K♠', 'J♦', '9♥', '7♦', 'J♣', 'J♥', 'A♣', 'Q♦', 'J♠']
    Deck of cards: ['7♣', 'A♦']
    (({'name': 'John', 'cards': ['8♣', '8♥', '8♦', '10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥']}, {'name': 'Elie', 'cards': ['10♣', 'K♣', 'K♦', '7♠', '9♣', '8♠', 'Q♠', '9♠', '10♠', '9♦']}, {'name': 'Lisa', 'cards': ['Q♥', 'K♠', 'J♦', '9♥', '7♦', 'J♣', 'J♥', 'A♣', 'Q♦', 'J♠']}), ['7♣', 'A♦'])
    >>> card_setup(1,{"name": 'John',"cards":[]})
    ---------------------------------
    shuffling the cards ...
    ---------------------------------
    Error in the previous section of the Program.
    ({'name': 'John', 'cards': []}, [])
    >>> card_setup(a1,{"name": 'John',"cards":[]})
    Traceback (most recent call last):
      ...
    NameError: name 'a1' is not defined
    >>> card_setup(3)
    Traceback (most recent call last):
      ...
    TypeError: card_setup() missing 1 required positional argument: 'players'
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
    print("---------------------------------")
    print("shuffling the cards ...")
    print("---------------------------------")
    time.sleep(2)

    amount_of_cards = len(cards) 
    if number_of_players == 2:
        rest = 12
        cards_per_player = 10
        for i in range(0,number_of_players):
                time.sleep(1)
                print(players[i]["name"],"has the following cards:")
                print(cards[i*cards_per_player:(i+1)*cards_per_player])
                players[i]["cards"] = cards[i*cards_per_player:(i+1)*cards_per_player]
        print("Deck of cards: ", cards[20:32])
        deck_of_cards = cards[20:32]
        
    elif number_of_players < 2:                             #obsolete if program used correctly
        print("Error in the previous section of the Program.")
        deck_of_cards = []
        
    else:
        cards_per_player = int(amount_of_cards/number_of_players)
        rest = amount_of_cards % number_of_players  #Deck of cards

        for i in range(0,number_of_players):
            time.sleep(1)
            print(players[i]["name"],"has the following cards:")
            print(cards[i*cards_per_player:(i+1)*cards_per_player])
            players[i]["cards"] = cards[i*cards_per_player:(i+1)*cards_per_player]
        time.sleep(1)
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
    cards : dictionary of one player with his cards
    >>> check_for_quartet(({"name":'John',"cards":['8♣', '8♥', '8♦','8♠','10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥'],"counter": 0},{"name":'Elie',"cards":['9♣', '9♥', '9♦','9♠','Q♦', 'Q♥'],"counter": 0}))
    ({'name': 'John', 'cards': ['10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥'], 'counter': 1}, {'name': 'Elie', 'cards': ['Q♦', 'Q♥'], 'counter': 1})
    >>> check_for_quartet(({"name":'John',"cards":['10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥'],"counter":0},{"name":'Elie',"cards":['Q♦', 'Q♥'],"counter": 0}))
    ({'name': 'John', 'cards': ['10♦', '10♥', 'A♥', 'A♠', 'K♥', 'Q♣', '7♥'], 'counter': 0}, {'name': 'Elie', 'cards': ['Q♦', 'Q♥'], 'counter': 0})
    >>> check_for_quartet (({"name":'John',"cards":['8♣', '8♥', '8♦','8♠'], "counter": 1}, {"name":'Elie', "cards":[],"counter":0}))
    ({'name': 'John', 'cards': [], 'counter': 2}, {'name': 'Elie', 'cards': [], 'counter': 0})
    >>> check_for_quartet(['8♣', '8♥', '8♦','8♠'])
    Traceback (most recent call last):
      ...
    TypeError: string indices must be integers
    >>> check_for_quartet(({"name":'John'},{"name":'Elie'}))
    Traceback (most recent call last):
      ...
    KeyError: 'cards'
    >>>
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
        if player["player_or_pc"] == True: #human
            who = input("Who do you want to take a card from?")
            restart_exit()

            while who not in people or who == player["name"]:
                who = input("Select another player?")
                restart_exit()

            if who in people and who != player["name"]:
                which_number = input("Which number do you want?") 
                restart_exit()
                while which_number not in quartet:
                    which_number = input("Select another number?")
                    restart_exit()

                if which_number in quartet:
                    which_color = input("Which color do you want?") 
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
                        print("The choosen card is:",which_card)

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
            time.sleep(2)
                
            who_pc = random.choice(people)
            while who_pc == player["name"]:
                who_pc = random.choice(people)
            which_color_pc = random.choice(color)
            which_number_pc = random.choice(quartet)

            if which_color_pc == "HEARTS":
                which_color_pc = "\u2665"
            elif which_color_pc == "DIAMONDS":
                which_color_pc = "\u2666"
            elif which_color_pc == "CLUBS":
                which_color_pc = "\u2663"
            elif which_color_pc == "SPADES":
                which_color_pc = "\u2660"
            which_card_pc = which_number_pc+ which_color_pc
            time.sleep(2)
            print("The AI asked",who_pc,"for the following card:",which_card_pc)  

            check_card(who_pc, which_card_pc, players, player, deck_of_cards)
            check_for_quartet(players)
    
def check_card(who, which_card, players, player, deck_of_cards):
    """Checking if the asked player is in possesion of the asked card
    who: the person asked to give up a card
    which_card: the card asked for
    players: dictionary with all the data of all the players
    player: dictionary of the player receiving the potential card
    deck_of_cards: cards in the deck to pick from in case 2 player
    >>> check_card('John','J♦',({"name":'John',"cards":['J♦']},{"name":'Elie',"cards":['8♦', '10♠']}),{"name":'John',"cards":['J♦']},['10♠'])
    The asked card is in the players' deck
    Your new hand is: ['J♦', 'J♦']
    True
    >>> check_card('John','J♦',({"name":'John',"cards":['Q♦']},{"name":'Elie',"cards":['8♦', '10♠']}),{"name":'John',"cards":['Q♦']},['10♠'])
    Sorry, the player is not in possesion of the card.
    Take a card from the deck:
    The card 10♠ was added to your hand!
    Your new hand is: ['Q♦', '10♠']
    False
    >>> check_card(John,5HEART,(John,Elie),John,['10♠'])
    Traceback (most recent call last):
      ...                
    SyntaxError: invalid syntax
    >>> check_card('John','J♦',({"name":'John',"cards":['Q♦']},{"name":'Elie',"cards":['8♦', '10♠']}),{"name":'John',"cards":['Q♦']})
    Traceback (most recent call last):
      ...
    TypeError: check_card() missing 1 required positional argument: 'deck_of_cards'
    >>>
    """
    for element in players:
        if element["name"] == who:
            if which_card in element["cards"]:
                print("The asked card is in the players' deck")
                element["cards"].remove(which_card)
                player["cards"].append(which_card)
                print("Your new hand is:",player["cards"])
                return True
            else:
                print("Sorry, the player is not in possesion of the card.")
                print("Take a card from the deck:")
                take_a_card(deck_of_cards, players, player)
                return False

def take_a_card(deck_of_cards, players, player):
    """function to take a card from the given deck
    only used for 2 players
    >>> take_a_card(['J♦', 'A♦', '8♦', '10♠'],({"name":'John',"cards":[]},{"name":'Elie',"cards":[]},{"name":'Lisa',"cards":[]},{"name":'Marc',"cards":[]}),{"name":'John',"cards":[]})
    The card 10♠ was added to your hand!
    Your new hand is: ['10♠']
    >>> take_a_card(['J♦', 'A♦', '8♦', '10♠'],({"name":'John',"cards":[]},{"name":'Elie',"cards":[]},{"name":'Lisa',"cards":[]},{"name":'Marc',"cards":[]}),{"name":'John',"cards":['8♥', '8♦', '10♦']})
    The card 10♠ was added to your hand!
    Your new hand is: ['8♥', '8♦', '10♦', '10♠']
    >>> take_a_card([],({"name":'John',"cards":[]},{"name":'Elie',"cards":[]},{"name":'Lisa',"cards":[]},{"name":'Marc',"cards":[]}),{"name":'John',"cards":[]})
    Sorry, no more cards on the deck...
    >>> take_a_card(1,2,3)
    Traceback (most recent call last):
        ...
    TypeError: object of type 'int' has no len()
    >>> take_a_card()
    Traceback (most recent call last):
      ...
    TypeError: take_a_card() missing 3 required positional arguments: 'deck_of_cards', 'players', and 'player'
    >>>
    """
    if len(deck_of_cards) > 0:
        card = deck_of_cards[-1]
        player["cards"].append(card)
        deck_of_cards.remove(card)
        time.sleep(1)
        print("The card",card,"was added to your hand!")
        time.sleep(1)
        print("Your new hand is:",player["cards"])
    else:
        print("Sorry, no more cards on the deck...")
        
def compare_results(score):
    """
    Quick comparaison of multiple results from all the players to return a winner
    """
    best_score = max([player[1] for player in score])
    for subarray in score:
        if best_score in subarray:
            print("#############################################")
            print("_____________________________________________")
            print("\nThe winner is " + subarray[0])
            print("_____________________________________________")
            print("#############################################")
            restart_exit()
            
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
