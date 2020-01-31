from random import shuffle

class Deck:
    '''
        club:    \u2663
        spades:  \u2660
        diamond: \u2666
        heart:   \u2665
    '''
    deck = []

    def __init__(self):
        for c in ['\u2663', '\u2660', '\u2666', '\u2665']:
            for i in range (2,15):
                if i <= 10:
                    self.deck.append(c+str(i))
                elif i == 11:
                    self.deck.append(c+'J')
                elif i == 12:
                    self.deck.append(c+'Q')
                elif i == 13:
                    self.deck.append(c+'K')
                elif i == 14:
                    self.deck.append(c+'A')

    def shuffle_deck(self):
        x = [i for i in range(52)]
        shuffle(x)

        deck_new = []
        for i in x:
            deck_new.append(self.deck[i])

        self.deck = deck_new
        deck_new = []

    def get_a_card(self):
        return(self.deck.pop())

    def __str__(self):
        str = ''
        for s in self.deck:
            str = str + s + ', '
        return str
