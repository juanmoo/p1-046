# This code serves as a simulation of to model the scenario on Problem 1-a
import random

class Deck(object):

    initial_card_num = 52

    def __init__ (self, card_num, deck=None):
        if deck is None:
            self.cards =  ['b' for i in range(card_num//2)] + ['r' for i in range(card_num//2)]
            random.shuffle(self.cards)
        else:
            self.cards = deck
        self.reveal_count = 0
        self.bottom_to_top_count = 0
        self.top_to_bottom_count = 0

    def bottom_to_top(self):
        self.cards = [self.cards[-1]] + self.cards[:-1]
        self.bottom_to_top_count += 1

    def top_to_bottom(self):
        self.cards = self.cards[1:] + [self.cards[0]]
        self.top_to_bottom_count += 1

    def next_card(self, person):
        if self.cards[0] == person:
            self.cards.pop(0)
            self.reveal_count += 1
            return True
        else:
            self.top_to_bottom()
            return False
       # elif person == 'b':
        #    self.bottom_to_top()
        #else:
        #    self.top_to_bottom()
        #return False
    
    def __repr__ (self):
        return str(self.cards)

def simmulate_draw( line, deck):
    assert(len(line) == len(deck.cards))

    i = 0
    while i < len(line):
        person = line[i]
        
        t = deck.next_card(person)
        while ( not t ):
            t = deck.next_card(person)
        i += 1
    return deck.reveal_count + deck.bottom_to_top_count + deck.top_to_bottom_count


for n in range(1,10000, 100):
    card_order = ['r'] * n + ['b'] * n
    random.shuffle(card_order)
    
    # Same Order ##
    deck = Deck(n, list(card_order))
    line = list(card_order)
    res = simmulate_draw(line, deck)
    print("Same Order:", res/(2*n))
    
    # Reverse Order ##
    deck = Deck(n, list(card_order))
    line = card_order[::-1]
    res = simmulate_draw(line, deck)
    print("Reverse Order:", res/(2*n))
    
    # Inverted r <-> b ##
    deck = Deck(n, list(card_order))
    line = ['r' if e == 'b' else 'b' for e in card_order]
    res = simmulate_draw(line, deck)
    print("Inverted order:", res/(2 * n))
  


    print('\n')
