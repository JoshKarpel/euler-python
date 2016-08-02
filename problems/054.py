import time
import miscmath


card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Card:
    def __init__(self, string):
        self.suit = string[1]
        self.value = card_values[string[0]]

class Hand:
    def __init__(self, cards):
        self.cards = cards

        self.card_values = sorted([card.value for card in self.cards])
        self.suits = [card.suit for card in self.cards]

        self.card_value_set = set(self.card_values)
        self.suit_set = set(self.suits)

        self.value = 0
        self.high_card = max(self.card_value_set)

    def compute_value(self):
        # royal flush
        if self.card_value_set == {14, 13, 12, 11, 10} and len(self.suit_set) == 1:
            self.value = 10
        # straight flush
        elif len(self.suit_set) == 1 and (self.card_values[0] == self.card_values[1] - 1 == self.card_values[2] - 2 == self.card_values[3] - 3 == self.card_values[4] - 4):
            pass
        # four of a kind
        elif self.card_values[0] == self.card_values[1] == self.card_values[2] == self.card_values[3] or self.card_values[1] == self.card_values[2] == self.card_values[3] == self.card_values[4]:
            self.value = 8
        # full house
        elif (self.card_values[0] == self.card_values[1] == self.card_values[2] and self.card_values[3] == self.card_values[4]) or (self.card_values[0] == self.card_values[1] and self.card_values[2] == self.card_values[3] == self.card_values[4]):
            self.value = 7
        # flush
        elif len(self.suit_set) == 1:
            self.value = 6
        # straight
        elif self.card_values[0] == self.card_values[1] - 1 == self.card_values[2] - 2 == self.card_values[3] - 3 == self.card_values[4] - 4:
            self.value = 5
        # three of a kind





start_time = time.clock()

c = Card('KC')
print(c.value, c.suit)


end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))