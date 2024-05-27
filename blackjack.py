import random
from art_blackjack import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)
def check_score():
    #you can modify for win/lose
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    return user_score, computer_score
def play_game():
    print(logo)
user_cards = []
computer_cards = []
blackjack = 21

start_question = (input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))

if start_question == "y":
# Pick random cards for player
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    print(user_cards)
# If ace is drawn, is counted as 11 if total goes over 21, is counted as 1
    if (sum(user_cards)) > blackjack and user_cards[0] == 11 and user_cards[1] == 11:
        user_cards[0] = 1
        print(user_cards)

# Pick random cards for computer
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

# If ace is drawn, is counted as 11 if total goes over 21, is counted as 1
    if (sum(computer_cards) > blackjack) and computer_cards[0] == 11 and computer_cards[1] == 11:
        computer_cards[0] = 1

# Check if is Blackjack
    if sum(computer_cards) == 21:
        print(f"Your cards:{user_cards}, current score:{sum(user_cards)}")
        print(f"Computer's final hand is: {computer_cards}, final score {sum(computer_cards)}")
        print("Computer wins!")
        exit()
    elif sum(user_cards) == 21:
        print(f"Your cards:{user_cards}, current score:{sum(user_cards)}")
        print(f"Computer's final hand is: {computer_cards}, final score {sum(computer_cards)}")
        print("Player wins!")
        exit()
    elif sum(computer_cards) == 21 and sum(user_cards) == 21:
        print("It's a draw!")
        exit()
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

# Check the Score
    check_score()
    should_continue = True
    while should_continue:
        continue_play = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_play == "y":
            user_cards.append(deal_card())
            print(f"Your hand is:{user_cards}, your score is: {sum(user_cards)}")
            check_score()
            if sum(user_cards) > 21:
                print("You went over. You Lose!")
                exit()
            elif sum(user_cards) == 21:
                print(f"Computer's final hand is: {computer_cards}, final score {sum(computer_cards)}")
                print("Player wins!")
                exit()
        elif continue_play == "n":
            #here works with while for computer
            if sum(computer_cards) <= 16:
                computer_cards.append(deal_card())
                check_score()
                if sum(computer_cards) <= 16:
                    computer_cards.append(deal_card())
                    check_score()
                if sum(computer_cards) == 21:
                    print(f"Computer's final hand is: {computer_cards}, final score {sum(computer_cards)}")
                    print("Computer wins!")
                    exit()
                if sum(computer_cards) == sum(user_cards):
                    print("It's a Draw!")
                elif ((sum(computer_cards) > sum(user_cards))) and sum(computer_cards) < blackjack:
                    print(f"Computer's final hand is: {computer_cards}, final score {sum(computer_cards)}")
                    print("Computer wins!")
                    exit()
                else:
                    print(f"Your final hand is: {user_cards}, current score: {sum(user_cards)}")
                    print(f"Computer's final hand is: {computer_cards}, final score {sum(computer_cards)}")
                    print("Player wins!")
                exit()
