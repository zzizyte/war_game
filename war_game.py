import pydealer
import time


rankings = {
    "values": {
        "Ace": 13,
        "King": 12,
        "Queen": 11,
        "Jack": 10,
        "10": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "Joker": 0,
    },
    "suits": {"Spades": 1, "Hearts": 1, "Clubs": 1, "Diamonds": 1},
}


def main():
    first_player, second_player = get_player_names()
    player_one_cards, player_two_cards = prepare_cards()
    play_game(first_player, second_player, player_one_cards, player_two_cards)


def prepare_cards():
    deck = pydealer.Deck(ranks=rankings)
    deck.shuffle()
    player_one_cards = list(deck.deal(26))
    player_two_cards = list(deck.deal(26))
    return player_one_cards, player_two_cards


def get_player_names():
    first_player = input("First Player: ").strip().title()
    second_player = input("Second Player: ").strip().title()
    return first_player, second_player


def play_game(first_player, second_player, player_one_deck, player_two_deck):
    print("One to win the most cards wins!\n")
    global first_player_won_cards, second_player_won_cards
    first_player_won_cards = []
    second_player_won_cards = []

    while player_one_deck and player_two_deck:
        player_one_card = player_one_deck.pop(0)
        print(f"{first_player}: {player_one_card}")
        player_two_card = player_two_deck.pop(0)
        print(f"{second_player}: {player_two_card}\n")
        if player_one_card.eq(player_two_card, rankings):
            if (len(player_one_deck) >= 2 and len(player_two_deck) >= 2):
                war_cards = [player_one_card, player_two_card]
                play_war(
                    player_one_deck,
                    player_two_deck,
                    war_cards,
                    first_player,
                    second_player,
                )
            elif (len(player_one_deck) == 0 or len(player_two_deck) == 0):
                check_who_won(first_player, second_player)
        else:
            war_cards = [player_one_card, player_two_card]
            check_match_winner(first_player, second_player, war_cards)
    check_who_won(first_player, second_player)


def play_war(player_one_deck, player_two_deck, war_cards, first_player, second_player):
    print("War!")
    player_one_cards = [player_one_deck.pop(0), player_one_deck.pop(0)]
    print(f"{first_player}: {player_one_cards[1]}")
    player_two_cards = [player_two_deck.pop(0), player_two_deck.pop(0)]
    print(f"{second_player}: {player_two_cards[1]}")
    war_cards.extend(player_one_cards + player_two_cards)
    if len(player_one_deck) >= 2 and len(player_two_deck) >= 2:
        if player_one_cards[1].eq(player_two_cards[1], rankings):
            play_war(
                player_one_deck, player_two_deck, war_cards, first_player, second_player
            )
        else:
            check_match_winner(first_player, second_player, war_cards)
    elif len(player_one_deck) < 2 and len(player_two_deck) < 2:   
            check_who_won(first_player, second_player)



def check_who_won(first_player, second_player):
    if len(first_player_won_cards) < len(second_player_won_cards):
        print(
            f"{second_player} won with the score {len(second_player_won_cards)}:{len(first_player_won_cards)}"
        )
    elif len(first_player_won_cards) > len(second_player_won_cards): 
        print(
            f"{first_player} won with the score {len(first_player_won_cards)}:{len(second_player_won_cards)}"
        )
    else:
        print(f"It's a draw! Score {len(first_player_won_cards)}:{len(second_player_won_cards)}")


def check_match_winner(first_player, second_player, war_cards):
    if len(war_cards) == 2:
        player_one_card = war_cards[0]
        player_two_card = war_cards[1]
    else: 
        player_one_card = war_cards[-3]
        player_two_card = war_cards[-1]
    
    if player_one_card.lt(player_two_card, rankings):
        
        second_player_won_cards.extend(war_cards)
        print(
        f"{second_player} wins\n score:{first_player}-{len(first_player_won_cards)}  {second_player}-{len(second_player_won_cards)}"
        )
        input("Press Enter to continue...")
    else:
        first_player_won_cards.extend(war_cards)
        print(
        f"{first_player} wins\nscore: {first_player}-{len(first_player_won_cards)}  {second_player}-{len(second_player_won_cards)}"
        )
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
