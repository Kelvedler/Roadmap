import random


class Deck():

    def __init__(self, suites, ranks):
        self.suites = suites
        self.ranks = ranks
        self.deck = []
        for suite in suites:
            for rank in ranks:
                self.deck.append((suite, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def split(self):
        length = len(self.deck)
        deck1 = self.deck[:length//2]
        deck2 = self.deck[length//2:]
        return [deck1, deck2]


class Hand():

    def __init__(self, hand):
        self.hand = hand

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self):
        return self.hand.pop(0)

    def count_cards(self):
        return len(self.hand)


class Player(Hand):

    def __init__(self, name, hand):
        super().__init__(hand=hand)
        self.name = name

    def check_cards(self):
        if not self.hand:
            return False
        else:
            return True


def compare_cards(card1_rank, card2_rank):
    for rank in ranks[::-1]:
        if rank == card1_rank == card2_rank:
            return 3
        elif rank == card1_rank:
            return 1
        elif rank == card2_rank:
            return 2


suites = 'Hearts', 'Diamonds', 'Spades', 'Clubs'
ranks = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'

name1 = input('Player one, enter your name: ')
name2 = input('Player two enter your name: ')
deck = Deck(suites, ranks)
deck.shuffle()
deck1, deck2 = deck.split()
player1 = Player(name1, deck1)
player2 = Player(name2, deck2)
war = False
active_cards = []
war_chest = []

while player1.check_cards() and player2.check_cards():
    if not war:
        active_cards.extend([player1.remove_card(), player2.remove_card()])
    else:
        if player1.count_cards() > 3 and player2.count_cards() > 3:
            for i in range(3):
                war_chest.extend([player1.remove_card(), player2.remove_card()])
        active_cards.extend([player1.remove_card(), player2.remove_card()])

    if compare_cards(active_cards[0][1], active_cards[1][1]) == 1:
        for card in war_chest:
            player1.add_card(card)
        for card in active_cards:
            player1.add_card(card)
        if war:
            print(name1 + ' won the war!')
        else:
            print(name1 + ' won the round')
        war = False
        war_chest.clear()
    elif compare_cards(active_cards[0][1], active_cards[1][1]) == 2:
        for card in war_chest:
            player2.add_card(card)
        for card in active_cards:
            player2.add_card(card)
        if war:
            print(name2 + ' won the war!')
        else:
            print(name2 + ' won the round')
        war = False
        war_chest.clear()
    else:
        print('The war is on!')
        war = True
        war_chest.extend(active_cards)
    active_cards.clear()
    print('-' * 40)


if player1.check_cards():
    print(name1 + ' won the game!')
else:
    print(name2 + ' won the game!')