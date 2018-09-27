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

    while len(line) > 0:
        person = line.pop(0)
        
        t = deck.next_card(person)
        while ( not t ):
            t = deck.next_card(person)
    return deck.reveal_count + deck.bottom_to_top_count + deck.top_to_bottom_count


num = 4

line = ['r'] * (num//2) + ['b'] * (num//2)
random.shuffle(line)

deck = Deck(num, deck=line)
res = simmulate_draw(line, deck)
print("The number of operations was", res/num)