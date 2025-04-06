import numpy as np
from numpy import random
from BlackJack import BlackJack
from Player import Player, HIT, STICK
from copy import deepcopy


class MonteCarloPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.Q = np.random.randn(11, 21, 2, 2)
        self.N = np.zeros([11, 21, 2, 2])
        self.epsilon = 1.
        self.last_reward = 0

    def choose_action(self, state):
        if state is None:
            raise StandardError("No game associated to player")

        dealers_first_card = state[0]
        random_action = random.randint(0, 2)

        action_choice = random.choice(['RAND', 'GREEDY'], p=[self.epsilon, 1 - self.epsilon])

        if action_choice == 'RAND':
            return random_action

        if self.Q[dealers_first_card - 1][self.current_total - 1][min(self.number_of_aces_used, 1)][HIT] == \
                self.Q[dealers_first_card - 1][self.current_total - 1][min(self.number_of_aces_used, 1)][STICK]:
            return random_action

        if self.Q[dealers_first_card - 1][self.current_total - 1][min(self.number_of_aces_used, 1)][HIT] > \
                self.Q[dealers_first_card - 1][self.current_total - 1][min(self.number_of_aces_used, 1)][STICK]:
            return HIT
        else:
            return STICK

    def receive_reward(self, reward):
        self.last_reward = reward

    def run_episode(self):
        game = BlackJack([self])
        self.current_total = 0
        self.number_of_aces_used = 0
        action = self.choose_action(game.get_current_state())
        old_state = deepcopy(game.get_current_state())
        old_total = deepcopy(self.current_total)
        old_n_aces = deepcopy(self.number_of_aces_used)
        reward = 0
        new_q = deepcopy(self.Q)
        while not game.game_over:
            game.step([action])
            reward = self.last_reward

            dealers_first_card = old_state[0]

            self.N[dealers_first_card - 1][old_total - 1][min(old_n_aces, 1)][action] += 1
            alpha = 1. / self.N[dealers_first_card - 1][old_total - 1][min(old_n_aces, 1)][action]
            new_q[dealers_first_card - 1][old_total - 1][min(old_n_aces, 1)][action] += \
                alpha * (reward - self.Q[dealers_first_card - 1][old_total - 1][min(old_n_aces, 1)][action])

            self.epsilon = 100. / (100 + self.N[dealers_first_card - 1][old_total - 1][min(old_n_aces, 1)][action])
            action = self.choose_action(game.get_current_state()) if not game.game_over else 0
            old_state = deepcopy(game.get_current_state())
            old_total = deepcopy(self.current_total)
            old_n_aces = deepcopy(self.number_of_aces_used)

        self.Q = deepcopy(new_q)
        return reward

    def run_episodes(self, n):
        for k in range(1, n+1):
            self.run_episode()

        return self.Q, self.N
