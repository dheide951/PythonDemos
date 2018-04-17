from random import shuffle

class Card:
    suits = ["spades","hearts","diamonds","clubs"]
    values = [None, None,"2","3","4","5","6",
              "7","8","9","10",
              "Jack","Queen","King","Ace"]

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return "{} of {}".format(self.values[self.value],self.suits[self.suit])

class Deck:

    def __init__(self, shuffled=True):
        self.cards = []
        for x in range(2,15):
            for i in range(4):
                self.cards.append(Card(x,i))
                if shuffled == True:
                    shuffle(self.cards)

    def shuffle_deck(self):
        shuffle(self.cards)
 
    def cards_remaining(self):
        return len(self.cards)
    
    def rm_card(self):
        if len(self.cards) <= 0:
            return None
        return self.cards.pop()

    def show_deck_to_console(self):
        for x in self.cards:
            print(x)
        

    def __repr__(self):
        return "Deck of {} cards".format(self.cards_remaining())

class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

    def draw(self, deck):
        self.card = deck.rm_card()

class Game:

    def __init__(self):
        name1 = input("Name of Player1: ")
        name2 = input("Name of Player2: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)
    
    def play_game(self):
        print("Beginning War")
        response = ""
        cards = self.deck.cards
        while(len(cards) >= 2):
            response = input("q to quit. Any key to play\n")
            if response == "q":
                break
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)
            print("{} drew {}".format(self.player1.name, self.player1.card))
            print("{} drew {}".format(self.player2.name, self.player2.card))
            if self.player1.card > self.player2.card:
                self.winner(self.player1)
            elif self.player1.card < self.player2.card:
                self.winner(self.player2)
            print("")
        self.stats()


    def stats(self):
        winner = None
        print("")
        print("{} won {} times".format(self.player1.name, self.player1.wins))
        print("{} won {} times".format(self.player2.name, self.player2.wins))
        if(self.player1.wins > self.player2.wins):
            winner = self.player1
        elif(self.player2.wins > self.player1.wins):
            winner = self.player2
        else:
            print("it was a tie")
        if winner != None:
            print("The Winner is {}".format(winner.name))
        

    def winner(self, player):
        print("{} wins this round".format(player.name))
        player.wins += 1


game = Game()
game.play_game()
            

            
            
        
            

            











        
