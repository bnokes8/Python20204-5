# Brady Nokes
# 1/21
# blackjack

import random
import cards as m_cards
import gamefunctions

class BJ_Cards(m_cards.Pos_card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Cards.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(m_cards.Deck):
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS:
                self.cards.append(BJ_Cards(rank,suit))


deck = BJ_Deck()
deck.populate()
deck.shuffle()
print(deck.cards[0])
print(deck.cards[0].value)
