import random

# Card deck setup
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 for J, Q, K, 11 for Ace

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    """Return score, adjust for Ace if needed"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
    return sum(hand)

def compare(player_score, dealer_score):
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "Draw!"
    elif player_score == 0:
        return "Blackjack! You win!"
    elif dealer_score == 0:
        return "Dealer has Blackjack! You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    game_over = False
    
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            action = input("Type 'hit' to get another card, 'stand' to pass: ").lower()
            if action == "hit":
                player_hand.append(deal_card())
            else:
                game_over = True
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

# Run the game
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    play_game()