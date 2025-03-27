import random
from Card import Card

class DeckOfCards:
    def __init__(self, shuffle=True):
        self.suits = ['D', 'H', 'S', 'C']
        self.faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = []
        self.generate_deck()
        if shuffle:
            self.shuffle_deck()

    def generate_deck(self):
        self.deck = [
            Card(10 if face in ["J", "Q", "K"] else (1 if face == "A" else int(face)), suit, face)
            for suit in self.suits for face in self.faces
        ]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0) if self.deck else None
