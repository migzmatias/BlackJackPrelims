from DeckOfCards import DeckOfCards
from Player import Player

def player_turn(deck, player):
    while player.get_hand_value() < 21:
        print("\nYour Hand:")
        player.show_hand()
        print(f"Your Hand Value: {player.get_hand_value()}")

        while True:
            choice = input("Do you want to (H)it or (S)tand? ").strip().upper()
            if choice in ("H", "S"):
                break
            print("Invalid option, please enter H or S.")

        if choice == "H":
            player.add_card(deck.draw_card())

            print("\nYour Hand:")
            player.show_hand()
            print(f"Your Hand Value: {player.get_hand_value()}")

            if player.get_hand_value() > 21:
                print("\nYour Final Hand:")
                player.show_hand()
                print(f"Final Hand Value: {player.get_hand_value()}")
                return False
        elif choice == "S":
            break

    return True

def dealer_turn(deck, dealer):
    while dealer.get_hand_value() < 17:
        dealer.add_card(deck.draw_card())

def display_results(player, dealer):
    player_value = player.get_hand_value()
    dealer_value = dealer.get_hand_value()

    print("\nDealer's Hand:")
    dealer.show_hand()
    print(f"Dealer's Hand Value: {dealer_value}\n")

    if player_value > 21:
        print("You bust! Dealer wins.")
    elif dealer_value > 21:
        print("Dealer busts! You win.")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("It's a tie!")

def main():
    while True:
        deck = DeckOfCards()
        player = Player()
        dealer = Player()

        player.add_card(deck.draw_card())
        player.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())

        print("\nDealer's Hand:")
        dealer.show_hand(hide_first=True)

        player_did_not_bust = player_turn(deck, player)

        if not player_did_not_bust:
            display_results(player, dealer)
        else:
            dealer_turn(deck, dealer)
            display_results(player, dealer)

        while True:
            play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
            if play_again in ["Y", "N"]:
                break
            print("Invalid option, please enter Y or N.")

        if play_again != "Y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

