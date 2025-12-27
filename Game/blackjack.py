import random

# declaring and initializing global playing variable
playing = True

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,'Jack': 10, 'Queen': 10, 'King': 10, 'Ace':11}

class Card: 
    """
    Represents a single playing card
    """

    def __init__(self, suit, rank):
        """ 
        Initiates a Card object with a suit, rank, and calculated value
        """
        
        self.suit = suit
        self.rank = rank    
        self.value = values[rank]   

    def __str__(self):
        """ 
        Returns a user-friendly string representaion of the card
        """
        
        return f"{self.rank} of {self.suit}"

class Deck:
    """
    Represents a deck of 52 cards.
    """

    def __init__(self):
        """
        Initializes a brand new, ordered deck of 52 Card objects.
        """

        # initializes a new deck
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffles the card in the deck in-place
        """

        random.shuffle(self.deck)

    def deal(self):
        """
        Deals a single card from the top (end) of the block 
        """
        
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None


    def __str__(self):
        """
        Returns a string showing number of cards remaining in the deck
        """

        return f"Deck of {len(self.deck)} cards."


class Hand:
    """
    Represents the hand of a player
    """

    def __init__(self):
        self.cards = [] 
        self.value = 0  
        self.aces = 0   


    def adjust_for_ace(self):
        """
        Controls the ace value logic
        """

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -=1
    
    def add_card(self, card):
        """
        Adds a new card and updates the value of hand
        """

        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()


class Chips():
    """
    Represent the chips held by the player
    """

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        """
        Adds to total chips
        """
        
        self.total += self.bet

    def lose_bet(self):
        """
        Subtracts from total chips
        """
        
        self.total -= self.bet


def take_bet(chips):
    """
    Takes a valid bet amount from the user
    """
    
    while True:
        try:
            chips.bet = int(input("Enter the amount you would like to bet: "))
        except ValueError:
            print("Please enter a valid amount in digits!")
            continue
        else:
            if chips.bet > chips.total:
                print(f"Not enough balance! You have {chips.total}")
                continue
            elif chips.bet < 0:
                print("Please enter a positive amount!")
                continue
            else:
                break


def hit(deck, hand):
    """
    Adds one card to player's hand
    """

    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    """
    Ask the user for Hit or Stand and acts accordingly
    """

    global playing

    while True:
            choice = input("Do you wanna 'h' (Hit) or 's' (Stand): ").lower()

            if choice == 'h':
                hit(deck, hand)
                break
            elif choice == 's':
                print("Player stand! Dealer is playing")
                playing = False
                break
            else:
                print("Please enter a valid value! 'h' or 's'")
                continue


def show_some(player, dealer):
    """
    Display one dealer card and all player cards
    """

    print("\nDealer's Hand:")
    print("<card hidden>")
    print(dealer.cards[1])
    print(f"Dealer's value: {dealer.cards[1].value}")

    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    print(f"Player's value: {player1.value}")

def show_all(player, dealer):

    """
    Display all cards and values of both dealer and the player
    """
    
    print("\nDealer's Hand:")
    for card in dealer.cards:
        print(card)
    print(f"Dealer's value: {dealer.value}")


    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    print(f"Player's value: {player.value}")


# Functions to control the game and chips flow
def player_busts(chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("\nDealer busts!")
    chips.win_bet()

def dealer_wins(chips):
    print("\nDealer wins!")
    chips.lose_bet()

def push():
    print("\nDealer and Player tie! It's a push.")

# Initializing player chips at the start to account for multiple rounds
player_chips = Chips()



# Final Game loop
while True:
    print("\nWelcome to the BlackJack game by codergallery!")

    # creating a new deck and shuffling
    deck1 = Deck()  
    deck1.shuffle() 

    # creating player and dealer
    player1 = Hand()
    dealer1 = Hand()

    # dealing two cards to both player and dealer at start
    for i in range(2):
        player1.add_card(deck1.deal())
        dealer1.add_card(deck1.deal())

    # take bet
    print(f"\nPlayer you have {player_chips.total} chips!")
    take_bet(player_chips)

    # show the cards to start the game
    show_some(player1, dealer1)


    # player's turn 
    while playing:

        hit_or_stand(deck1, player1)

        show_some(player1, dealer1)

        if player1.value > 21:
            player_busts(player_chips)
            break

    # Dealer's turn
    if player1.value <= 21:
        while dealer1.value < 17:
            hit(deck1, dealer1)
        
        show_all(player1, dealer1)

        if dealer1.value > 21:
            dealer_busts(player_chips)

        elif dealer1.value > player1.value:
            dealer_wins(player_chips)

        elif dealer1.value < player1.value:
            player_wins(player_chips)

        else:
            push()

    # Replay logic
    while True: 
        play = input("Play again? (y/n): ").lower()

        if play == 'y':
            playing = True
            print("\n\n\n\n")
            break
        elif play == 'n':
            print("\nThanks for playing!")
            playing = False
            break
        else:
            print("Provide a valid input! (y/n)")
            continue
    
    if playing == False:
        break