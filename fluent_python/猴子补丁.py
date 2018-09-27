from random import shuffle

l = list(range(10))
shuffle(l)
print(l)


# 猴子补丁, 在过程中修改类或模块
def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card
shuffle(deck)

