import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)
computer_hand = []
for i in range(2):
    card = random.choice(cards)
    if card in computer_hand:
        continue
    else:
        computer_hand.append(card)
user_hand = []
for k in range(2):
    card = random.choice(cards)
    if card in user_hand:
        continue
    else:
        user_hand.append(card)
