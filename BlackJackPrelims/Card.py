class Card:
    def __init__(self, value, suit, face):
        self.value = value
        self.suit = suit
        self.face = face

    def get_card_value(self):
        return self.value

    def get_card_suit(self):
        suit_names = {'D': 'Diamond', 'H': 'Heart', 'S': 'Spade', 'C': 'Clubs'}
        return suit_names.get(self.suit, 'Unknown')

    def get_card_face(self):
        face_names = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
        return face_names.get(self.face, self.face)

    def __str__(self):
        return f"{self.get_card_face()} of {self.get_card_suit()} (Value: {self.value})"