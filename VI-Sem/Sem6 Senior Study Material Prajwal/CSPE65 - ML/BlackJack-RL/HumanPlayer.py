from Player import Player, HIT, STICK


class HumanPlayer(Player):
    def __init__(self, description="Human"):
        Player.__init__(self)
        self.description = description

    def choose_action(self, state):
        if state is None:
            raise StandardError("No game associated to player")

        print("\nCurrent State:")
        print("Your Total:", self.get_current_total())
        print("Number of Aces Used as 11:", self.number_of_aces_used)
        print("Dealer's first card:", state[0])
        print("Other players' totals:", state[1:])

        user_input = input('Please enter a valid move (0 for HIT, 1 for STICK) ')
        while user_input != HIT and user_input != STICK:
            user_input = input('Please enter a valid move (0 for HIT, 1 for STICK)! ')

        return user_input

    def receive_reward(self, reward):
        if reward == -1:
            print("\nYou lost")
        if reward == 1:
            print("\nYou won!")
