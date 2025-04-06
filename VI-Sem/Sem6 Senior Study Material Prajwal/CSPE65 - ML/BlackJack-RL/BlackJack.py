from Deck import Deck
from Player import Player, HIT, STICK

HIT = 0
STICK = 1


class BlackJack:
    def __init__(self, players, n_decks=1):
        self.deck = Deck(n_decks)
        self.players = players
        self.player_done = []
        assert len(self.players) <= 4, "Too many players"
        assert len(self.players) != 0, "No players"

        for player in self.players:
            assert type(player) is not Player, "one of the players is not really a player"
            player.new_card_drawn(self.deck.pop_card())
            self.player_done.append(0)

        self.dealer = Player()
        self.dealer.new_card_drawn(self.deck.pop_card())

        for player in self.players:
            player.new_card_drawn(self.deck.pop_card())

        self.game_over = False

    def get_current_state(self, detailed=False):
        if detailed:
            return self.get_detailed_state()
        players_total = [self.dealer.get_current_total()]
        for player in self.players:
            players_total.append(player.get_current_total())

        return players_total

    def get_detailed_state(self):
        all_cards = [self.dealer.get_current_cards()]
        for player in self.players:
            all_cards.append(player.get_current_cards())

        return all_cards

    def step(self, players_actions, print_stuff=False):
        i = 0
        for player in self.players:
            if self.player_done[i] != 0:
                i += 1
                continue

            player_action = players_actions[i]  # player.choose_action(self.get_current_state())

            if player_action == HIT:
                player.new_card_drawn(self.deck.pop_card())
                if player.is_bust():
                    player.receive_reward(-1)
                    self.player_done[i] = 1
                else:
                    player.receive_reward(0)
            else:
                self.player_done[i] = 1

            i += 1

        if sum(self.player_done) == len(self.player_done):
            while self.dealer.current_total < 17 and not self.dealer.is_bust():
                self.dealer.new_card_drawn(self.deck.pop_card())

            if print_stuff:
                print("\nDealer's total:", self.dealer.current_total)

            if self.dealer.is_bust():
                self.dealer.current_total = -1

            max_total = self.dealer.current_total

            for player in self.players:
                if player.get_current_total() > max_total and not player.is_bust():
                    max_total = player.get_current_total()

            for player in self.players:
                if player.get_current_total() == max_total and not player.is_bust():
                    player.receive_reward(1)
                elif not player.is_bust():
                    player.receive_reward(-1)

            self.game_over = True
