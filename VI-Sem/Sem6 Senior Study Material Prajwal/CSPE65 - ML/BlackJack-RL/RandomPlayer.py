from numpy import random
from Player import Player, HIT, STICK


class RandomPlayer(Player):
    def __init__(self, description="Random"):
        Player.__init__(self)
        self.description = description
        self.last_reward = 0

    def choose_action(self, state):
        if state is None:
            raise StandardError("No game associated to player")

        return random.random_integers(HIT, STICK)

    def receive_reward(self, reward):
        self.last_reward = reward
        # if reward == -1:
        #     print "Randomly lost"
        # if reward == 1:
        #     print "Randomly won"

    def run_episodes(self, n):
        return
