import pydealer

#create deck
#randomize deck
#separate to two decks
#both players open first card. Higher value wins
#winner puts the cards at the end of the deck
# if value of cards are equal, both players open second card face down and another card face up.
#repeat value check


def main():
    first_player, second_player = get_player_names()
    player_one_cards, player_two_cards = prepare_cards()

def prepare_cards():
    deck = pydealer.Deck()
    deck.shuffle()
    player_one_cards = list(deck.deal(26))
    player_two_cards = list(deck.deal(26))
    return player_one_cards, player_two_cards

def get_player_names():
    first_player = input("First Player: ").strip().title()
    second_player = input("Second Player: ").strip().title()
    return first_player, second_player

def play_game():
    pass

def play_war():
    pass
    
    
#first_player_card.value > second_player_card.value:
    

if __name__ == "__main__":
    main()