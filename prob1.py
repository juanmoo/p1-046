# This code serves as a simulation of to model the scenario on Problem 1-a
import itertools
import random

class Deck(object):

    initial_card_num = 52

    def __init__ (self, deck):
        self.cards = list(deck)
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

def simulate_draw( line, deck):
    #if (len(line) != len(deck.cards)):
    #print('line length:', len(line), 'deck len:', len(deck.cards))
    #print('line:', line)
    #print('deck:', deck.cards)
    assert(len(line) == len(deck.cards))

    i = 0
    while i < len(line):
        person = line[i]
        
        t = deck.next_card(person)
        while ( not t ):
            t = deck.next_card(person)
        i += 1
    return deck.reveal_count + deck.bottom_to_top_count + deck.top_to_bottom_count

if __name__ == '__main__':
    for n in range(8 * 10,8 * 10000, 80):
        card_order = ['r'] * n + ['b'] * n
        random.shuffle(card_order)
        
        # Same Order ##
        deck = Deck(n, list(card_order))
        line = list(card_order)
        res = simulate_draw(line, deck)
        print("Same Order:", res/(2*n))
        
        # Reverse Order ##
        deck = Deck(n, list(card_order))
        line = card_order[::-1]
        res = simulate_draw(line, deck)
        print("Reverse Order:", res/(2*n))
        
        # Inverted r <-> b ##
        deck = Deck(n, list(card_order))
        line = ['r' if e == 'b' else 'b' for e in card_order]
        res = simulate_draw(line, deck)
        print("Inverted order:", res/(2 * n))
      
        # Divide in 8 ##
        deck = Deck(n, list(card_order))
        line = [['r'] * (n//8) + ['b'] * (n//8)] * 8
        line = list(itertools.chain.from_iterable(line))
        res = simulate_draw(line, deck)
        print("8 chunks order:", res/(2 * n))
    
        # Rotated by n / 2 ##
        deck = Deck(n, list(card_order))
        line = card_order[n:] + card_order[:n]
        res = simulate_draw(line, deck)
        print("Rotated by half:", res/(2 * n))
    
        # Select sides w/ larger wrong concentration #
        deck = Deck(n, list(card_order))
        line = []
        half_1 = ['b'] * (3 * n // 4) + ['r'] * (n // 4)
        random.shuffle(half_1)
        half_2 = ['r'] * (3 * n // 4) + ['b'] * (n // 4)
        random.shuffle(half_2)
        if card_order.count('b') < n/2:
            line = half_1 + half_2
        else:
            line = half_2 + half_1
        res = simulate_draw(line, deck)
        print("Side selected:", res/(2 * n))
        print('\n')
