import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_score(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards or sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
  if user_score == computer_score:   
    return "Draw"
  elif computer_score == 0:
    return "You lose. Opponent has a Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif computer_score < user_score:
    return "You Win"
  elif user_score > 21:
    return "You went over. you lose"
  if computer_score > 21:
    return "Opponent wen over. You win"
  else:
    return "You lose"    
def play_again():
    
  user_cards = []  
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print("   Your cards: {}, current score: {}".format(user_cards, user_score))
    print("   Computer's first card: {}".format(computer_cards[0]))

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True 

    else:
      continue_game = input("Type 'Y' to get another card or type 'N' to pass: ").lower()
      if continue_game == 'y':
        user_cards.append(deal_card()) 
      else:
        is_game_over = True


  while computer_score != 0 and computer_score < 17:
    computer_score.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print("   user card: {} user score: {}".format(user_cards, user_score))
  print("   computer card: {} computer score: {}".format(computer_cards, computer_score))
  compare(user_score, computer_score)

while input("Do you want to play again? enter 'y' or 'n'! ").lower() == 'y':
  play_again()