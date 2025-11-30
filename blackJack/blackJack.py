import random
import time


def deck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♥", "♦", "♣", "♠"]
    return [f"{v}{s}" for v in values for s in suits]


def shuffle_deck():
    cards = deck()
    random.shuffle(cards)
    print("Dealer is shuffling deck...")
    time.sleep(0.6)
    return cards


def deal_cards(cards):
    print("Dealing cards...\n")
    time.sleep(0.6)
    player_cards = [cards.pop(0), cards.pop(0)]
    dealer_cards = [cards.pop(0), cards.pop(0)]
    return player_cards, dealer_cards, cards


def format_hand(hand):
    return " ".join(hand)


def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        value = card[:-1]
        if value == "A":
            ace_count += 1
            score += 11
        elif value in ["J", "Q", "K"]:
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
        print("Player cards:", format_hand(player_cards))
        print("Player score:", player_score)

        if player_score > 21:
            return "bust", player_cards, cards

        choice = input("Hit, Stand or Quit? (H/S/Q): ").upper()

        if choice == "H":
            print("Dealing cards...")
            time.sleep(0.6)
            player_cards.append(cards.pop(0))

        elif choice == "S":
            print("Stand...")
            time.sleep(0.6)
            return "stand", player_cards, cards

        elif choice == "Q":
            return "quit", player_cards, cards

        else:
            print("Invalid choice, enter H, S or Q.")


def dealer_turn(dealer_cards, cards):
    print("Dealer reveals the hidden card:", dealer_cards[1])
    time.sleep(0.6)

    while True:
        dealer_score = calculate_score(dealer_cards)
        print("Dealer cards:", format_hand(dealer_cards))
        print("Dealer score:", dealer_score)

        if dealer_score >= 17:
            break

        print("Dealer takes one card...")
        time.sleep(0.6)
        dealer_cards.append(cards.pop(0))

    if dealer_score > 21:
        return "bust", dealer_cards, cards
    else:
        return "stand", dealer_cards, cards


def determine_winner(player_status, player_cards, dealer_status, dealer_cards):
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    if player_status == "bust":
        return "Dealer wins!"
    if dealer_status == "bust":
        return "You win!"

    if player_score > dealer_score:
        return "You win!"
    elif dealer_score > player_score:
        return "Dealer wins!"
    else:
        return "Draw"


def play_blackjack():
    while True:
        cards = shuffle_deck()
        player_cards, dealer_cards, cards = deal_cards(cards)

        print("Dealer cards:", dealer_cards[0], "??")
        time.sleep(0.6)

        player_status, player_cards, cards = player_turn(player_cards, cards)

        if player_status == "quit":
            print("Goodbye!")
            break

        if player_status == "bust":
            print("Dealer wins!")
            continue

        dealer_status, dealer_cards, cards = dealer_turn(dealer_cards, cards)

        result = determine_winner(player_status, player_cards, dealer_status, dealer_cards)
        print(result)
        print("\n--- New round starting ---\n")
        time.sleep(0.8)


play_blackjack()
