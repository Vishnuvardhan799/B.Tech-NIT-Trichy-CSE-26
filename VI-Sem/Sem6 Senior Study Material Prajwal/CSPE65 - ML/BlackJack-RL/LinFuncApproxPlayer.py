import numpy as np
from numpy import random
from BlackJack import BlackJack
from Player import Player, HIT, STICK
from copy import deepcopy

N_FEATURES = 4*6*2*2
N_DETAILED_FEATURES = 52*52*2*2


class LinFuncApproxPlayer(Player):
    def __init__(self, lmbda=0.5, use_detailed_features=False):
        Player.__init__(self)
        self.W = np.zeros([N_DETAILED_FEATURES, ]) if use_detailed_features else np.zeros([N_FEATURES, ])
        self.epsilon = 0.05
        self.lmbda = lmbda
        self.gamma = 0.7
        self.last_reward = 0
        self.use_detailed_features = use_detailed_features

    @staticmethod
    def generate_features(game_state, current_total, number_of_aces_used, action):
        features = np.zeros([4, 6, 2, 2])

        dealers_first_card = game_state[0]
        number_of_aces_used = min(number_of_aces_used, 1)

        if dealers_first_card <= 10 and current_total <= 18:
            features[(dealers_first_card - 1) / 3][(current_total - 1) / 3][number_of_aces_used][action] = 1

        if dealers_first_card <= 11 and current_total <= 18:
            features[(dealers_first_card - 2) / 3][(current_total - 1) / 3][number_of_aces_used][action] = 1

        if dealers_first_card <= 10 and current_total <= 21:
            features[(dealers_first_card - 1) / 3][(current_total - 4) / 3][number_of_aces_used][action] = 1

        if dealers_first_card <= 11 and current_total <= 21:
            features[(dealers_first_card - 2) / 3][(current_total - 4) / 3][number_of_aces_used][action] = 1

        return features.reshape((N_FEATURES, ))

    @staticmethod
    def generate_detailed_features(game_state, current_cards, number_of_aces_used, action):
        features = np.zeros([52, 52, 2, 2])

        dealers_first_card = game_state[0][0]
        dealers_first_card_value = dealers_first_card.get_suit_value() * 4 + dealers_first_card.get_number()
        number_of_aces_used = min(number_of_aces_used, 1)

        for card in current_cards:
            card_value = card.get_suit_value() * 13 + card.get_number() - 1
            features[dealers_first_card_value][card_value][number_of_aces_used][action] = 1

        return features.reshape((N_DETAILED_FEATURES,))

    def get_q_value(self, state, action):
        if self.use_detailed_features:
            return np.dot(self.generate_detailed_features(state, self.current_cards, self.number_of_aces_used, action), self.W)
        else:
            return np.dot(self.generate_features(state, self.current_total, self.number_of_aces_used, action), self.W)

    def choose_action(self, state):
        if state is None:
            raise StandardError("No game associated to player")

        random_action = random.randint(0, 2)

        action_choice = random.choice(['RAND', 'GREEDY'], p=[self.epsilon, 1 - self.epsilon])

        if action_choice == 'RAND':
            return random_action

        if self.get_q_value(state, HIT) == self.get_q_value(state, STICK):
            return random_action

        if self.get_q_value(state, HIT) == self.get_q_value(state, STICK):
            return HIT
        else:
            return STICK

    def receive_reward(self, reward):
        self.last_reward = reward

    def run_episode(self):
        game = BlackJack([self])
        self.current_total = 0
        self.number_of_aces_used = 0
        action = self.choose_action(game.get_current_state(self.use_detailed_features))
        old_state = deepcopy(game.get_current_state(self.use_detailed_features))
        eligibility_trace = np.zeros([N_DETAILED_FEATURES, ]) if self.use_detailed_features else np.zeros([N_FEATURES, ])
        reward = 0
        alpha = 0.01

        while not game.game_over:
            old_total = self.current_total
            old_cards = self.current_cards
            old_n_aces = self.number_of_aces_used
            old_q = self.get_q_value(old_state, action)

            game.step([action])
            reward = self.last_reward
            new_action = self.choose_action(old_state)

            new_q = self.get_q_value(game.get_current_state(self.use_detailed_features), new_action) if not game.game_over else 0
            delta = reward + self.gamma * new_q - old_q
            if self.use_detailed_features:
                eligibility_trace = self.gamma * self.lmbda * eligibility_trace + self.generate_detailed_features(old_state, old_cards, old_n_aces, action)
            else:
                eligibility_trace = self.gamma * self.lmbda * eligibility_trace + self.generate_features(old_state, old_total, old_n_aces, action)
            self.W = self.W + alpha * delta * eligibility_trace

            old_state = deepcopy(game.get_current_state(self.use_detailed_features))
            action = new_action
        return reward

    def run_episodes(self, n):
        for k in range(1, n+1):
            self.run_episode()
