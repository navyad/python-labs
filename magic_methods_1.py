import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    french_deck = FrenchDeck()

    print(french_deck)
    print(len(french_deck))

    print(choice(french_deck))

    for card in french_deck:
        if card.suit == 'spades':
            print(card.rank, card.suit)

    print(french_deck[1:2])
    print(french_deck[0])
    card = french_deck[0]
    print(type(card))
    print(type(french_deck))
    print(Card(99, 'foo') in french_deck)

"""
Notes:
1. namedtuple has been used to create class called Card
2. __getitem__ allows to iterate, index, slicing etc.
3. french_deck consists of objects from Card, compostion applies here.
"""
