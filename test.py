import random
from prob1 import Deck, simulate_draw


# Need to be able to enumerate possible permutations given length of deck / line of people #

def enumerate(r, b):
    if r == 0:
        return ['b' * b]
    elif b == 0:
        return ['r' * r]
    else:
        first = ['r' + s for s in enumerate(r - 1, b)]
        second = ['b' + s for s in enumerate(r, b - 1)]
        first.extend(second)
        return first
enumerate_list = lambda r, b: [list(s) for s in enumerate(r, b)]

# Given deck size, simulate draws with all possible permutations of line and output max #
def find_max_perm(N):

    #Initialize Card Order
    card_order = ['b'] * N + ['r'] * N
    random.shuffle(card_order)

    l = list()
    for perm in enumerate_list(N, N):
        best_order = (None, -1)
    
        for line in enumerate_list(N, N):
            deck = Deck(perm)
            res = simulate_draw(line, deck)
            if res > best_order[1]:
                best_order = (line, res)
        l.append((perm, best_order[0], best_order[1]))
    l.sort(key=lambda x:-x[2])
    for card, line, score in l:
        print ('cards:\t', card)
        print ('line:\t', line)
        print ('score:\t', score)
        print()

if __name__ == '__main__':
    find_max_perm(4)

