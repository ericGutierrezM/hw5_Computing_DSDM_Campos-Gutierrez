from hw5 import Card, Deck

def test_deck_init():
    deck = Deck()
    assert len(deck.english_deck) == 52
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    all_cards = [(c.suit, c.value) for c in deck.english_deck]
    for s in suits:
        for v in values:
            assert (s, v) in all_cards

def test_shuffle():
    deck = Deck()
    original_order = [(c.suit, c.value) for c in deck.english_deck]
    deck.shuffle()
    shuffled_order = [(c.suit, c.value) for c in deck.english_deck]
    assert original_order != shuffled_order

def test_draw():
    deck = Deck()
    initial_len = len(deck.english_deck)
    card_drawn = deck.draw()
    assert isinstance(card_drawn, Card)
    assert len(deck.english_deck) == initial_len - 1

def test_draw_all_cards_and_empty_message():
    deck = Deck()
    for k in range(52):
        deck.draw()
    result = deck.draw()
    assert result is None