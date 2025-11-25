import random


def deck():
    deck = []
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♥", "♦", "♣", "♠"]
    for value in values:
        for suit in suits:
            deck.append("%s%s" % (value, suit))
    return deck


def shuffle_deck():
    cards = deck()
    random.shuffle(cards)
    return cards


def deal_cards(cards):
    player_cards = []
    dealer_cards = []
    print("Dealing cards...\n")
    player_cards.append(cards.pop(0))
    player_cards.append(cards.pop(0))
    dealer_cards.append(cards.pop(0))
    dealer_cards.append(cards.pop(0))
    return player_cards, dealer_cards, cards


def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        value = card[:-1]
        if value == "A":
            ace_count += 1
            score += 11
        elif value == "J" or value == "Q" or value == "K":
            score += 10
        else:
            score += int(value)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score


def player_turn(player_cards, cards):
    while True:
        player_score = calculate_score(player_cards)
        print("Player cards:", player_cards)
        print("Player score:", player_score)
        if player_score > 21:
            return "bust", player_cards, cards
        choice = input("Hit or Stand? (H/S): ").upper()
        if choice == "H":
            player_cards.append(cards.pop(0))
        elif choice == "S":
            print("Stand...")
            return "stand", player_cards, cards
        else:
            print("Invalid choice, enter H or S.")


def dealer_turn(dealer_cards, cards):
    dealer_score = calculate_score(dealer_cards)
    print("Dealer cards:", dealer_cards)
    print("Dealer score:", dealer_score)
    while dealer_score < 17:
        print("Dealer takes one card...")
        dealer_cards.append(cards.pop(0))
        dealer_score = calculate_score(dealer_cards)
        print("Dealer cards:", dealer_cards)
        print("Dealer score:", dealer_score)
    if dealer_score > 21:
        return "bust", dealer_cards, cards
    else:
        return "stand", dealer_cards, cards


def determine_winner(player_status, player_cards, dealer_status, dealer_cards):
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    if player_status == "bust":
        return "Dealer wins!"
    elif dealer_status == "bust":
        return "You win!"
    elif player_score > dealer_score:
        return "You win!"
    elif dealer_score > player_score:
        return "Dealer wins!"
    else:
        return "Draw"


def play_blackjack():
    cards = shuffle_deck()
    player_cards, dealer_cards, cards = deal_cards(cards)
    player_status, player_cards, cards = player_turn(player_cards, cards)
    if player_status == "bust":
        print("Dealer wins!")
        return
    dealer_status, dealer_cards, cards = dealer_turn(dealer_cards, cards)
    result = determine_winner(player_status, player_cards, dealer_status, dealer_cards)
    print(result)


play_blackjack()
