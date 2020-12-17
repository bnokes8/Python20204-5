# Brady Nokes
# 12/20
# cards starting module
#imports
import random


class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♥", "♦", "♣", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
        +----------+
        | {0:<2}{1}      |
        |          |
        |          |
        |          |
        |       {1}{0:>2}|
        +----------+
        
        """,self.rank,self.suit)
        return rep


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card)
        else:
            rep = "< EMPTY >"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,handsList,per_hand=1):
        for rounds in range(per_hand):
            for hand in handsList:
                if self.cards:
                    topcard = self.cards[0]
                    self.give(topcard, hand)
                else:
                    print("Out of cards")
                    for hands in handsList:
                        hand.clear()
                    self.clear()
                    self.populate()
                    self.shuffle()
                    self.deal(handsList,per_hand)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

my_hand = Hand()
yourhand = Hand()
handslist = [my_hand,yourhand]

deck = Deck()
deck.populate()
deck.shuffle()
deck.deal(handslist,5)
for hand in handslist:
    print(hand)

my_hand.give(my_hand.cards[0],yourhand)
print("your hand")
print(yourhand)
#print(deck)
#print(len(deck.cards))
input()
for i in range(5):
    rank = random.choice(Card.RANKS)
    suit = random.choice(Card.SUITS)

    card = Card(rank,suit)
    my_hand.add(card)


print(my_hand)

