import numpy as np
from numpy import random
from BlackJack import BlackJack
from Player import Player, HIT, STICK
from copy import deepcopy
from QNetwork_Theano import Network
from QNetwork_Tensorflow import Network as Network2

BATCH_SIZE = 5
N_EPOCHS = 5
N_FEATURES = 4*6*2*2
N_BETTER_FEATURES = 52*52*2*2


class NeuralNetFuncApproxPlayer(Player):
    def __init__(self, lmbda=0.5):
        Player.__init__(self)
        self.network = Network2([N_FEATURES, 200, 20, 1])
        self.epsilon = 0.05
        self.lmbda = lmbda
        self.gamma = 0.7
        self.last_reward = 0
        self.batch = [[], []]

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
            card_value = card.get_suit_value() * 4 + card.get_number()
            features[dealers_first_card_value][card_value][number_of_aces_used][action] = 1

        return features.reshape((N_BETTER_FEATURES,))

    def choose_action(self, state):
        if state is None:
            raise StandardError("No game associated to player")

        random_action = random.randint(0, 2)

        action_choice = random.choice(['RAND', 'GREEDY'], p=[self.epsilon, 1 - self.epsilon])

        if action_choice == 'RAND':
            return random_action

        hit_features = self.generate_features(state, self.current_total, self.number_of_aces_used, HIT)
        hit_q_value = self.network.get_q_value(hit_features)
        stick_features = self.generate_features(state, self.current_total, self.number_of_aces_used, STICK)
        stick_q_value = self.network.get_q_value(stick_features)

        if hit_q_value == stick_q_value:
            return random_action

        if hit_q_value > stick_q_value:
            return HIT
        else:
            return STICK

    def receive_reward(self, reward):
        self.last_reward = reward

    def run_episode(self):
        game = BlackJack([self])
        self.current_total = 0
        self.number_of_aces_used = 0
        action = self.choose_action(game.get_detailed_state())
        old_state = deepcopy(game.get_detailed_state())
        reward = 0

        while not game.game_over:
            old_total = self.current_total
            old_n_aces = self.number_of_aces_used

            game.step([action])
            reward = self.last_reward
            new_total = self.current_total
            new_n_aces = self.number_of_aces_used

            if game.game_over:
                target_q = 0
            else:
                target_q = max(self.network.get_q_value(self.generate_features(game.get_detailed_state(), new_total, new_n_aces, HIT)),
                               self.network.get_q_value(self.generate_features(game.get_detailed_state(), new_total, new_n_aces, STICK)))
            target = reward + self.gamma * target_q

            if len(self.batch[0]) < BATCH_SIZE:
                self.batch[0].append(self.generate_features(old_state, old_total, old_n_aces, action))
                self.batch[1].append(target)
            else:
                self.network.gradient_descent(self.batch, N_EPOCHS)
                self.batch = [[], []]

            old_state = deepcopy(game.get_detailed_state())
            action = self.choose_action(old_state)
        return reward

    def run_episodes(self, n, print_stuff=False):
        for k in range(1, n+1):
            if print_stuff:
                if k % 100 == 0:
                    print('Episode', k)
            self.run_episode()

