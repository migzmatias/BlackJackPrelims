class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        num_aces = 0

        for card in self.hand:
            card_value = card.get_card_value()
            value += card_value
            if card.face == "A":
                num_aces += 1

        while num_aces > 0 and value + 10 <= 21:
            value += 10
            num_aces -= 1

        return value

    def show_hand(self, hide_first=False):
        if hide_first:
            print("[Hidden Card]")
            for card in self.hand[1:]:
                print(card)
        else:
            for card in self.hand:
                print(card)
