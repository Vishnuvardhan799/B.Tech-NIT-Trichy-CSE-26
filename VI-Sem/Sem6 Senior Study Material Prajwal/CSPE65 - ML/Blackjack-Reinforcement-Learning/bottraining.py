from gameplay import GamePlay
from strategy import Strategy
from collections import defaultdict
import sys

def TrainAndTestGameBot (trainingIteration, testingIteration, method, deckContent, initialNumberOfCard, \
                         winningPoints, dealerCriticalPointsToStick):

    #check input parameter robustness
    if (initialNumberOfCard * 10 > winningPoints):
        print("initial card points can exceed the winning points, not allowed")
        sys.exit();

    if (initialNumberOfCard < 1):
        print("initial number of card shall be equal ot greater than one")
        sys.exit();

    if (dealerCriticalPointsToStick > winningPoints):
        print("dealer will hit until bust")
        sys.exit()

    # when player combats with dealer after the training phase,
    # this list stores the result [#win, #draw, #lose]
    testResult = [0, 0, 0];

    # dictionary: key = playerCardPoints, dealerFirstCardPoint, usableAce (no usable=0, has usable=1), action (hit=0, stick=1), value = Q function
    # this dict is the Q-table, stores rthe Q value for all combinations of states and actions
    QTableDict = defaultdict(float)
    # dictionary: key = (playerCardPoints, dealerFirstCardPoint, usableAce (no usable=0, has usable=1)), value = number of occurrence throughout the iterations
    # this dict is used to determine epsilon (epsilon-greedy policy)
    stateCount = defaultdict(int)
    # dictionary: key = (playerCardPoints, dealerFirstCardPoint, usableAce (no usable=0, has usable=1), action (hit=0, stick=1), value = number of occurrence throughout the iterations
    # this dict is used to determine alpha (learning rate)
    stateActionCount = defaultdict(int)

    strategy = Strategy()

    for i in range(trainingIteration + testingIteration):

        # hit = 0, stick = 1
        action = None

        # if player wins dealer, reward = 1
        # if player draws dealer, reward = 0
        # if player loses dealer, reward = -1
        # used to update the Q function
        reward = None

        # start a game
        gameplay = GamePlay(deckContent, initialNumberOfCard, winningPoints)

        # a list stores the occurred key = playerCardPoints, dealerCardPoints, action (hit=0, stick=1)
        occurredStateActions = []

        # start the game until it is finished
        while not gameplay.finish:

            # find an action defined by the policy map
            if action != 1:
                # in training phase, use epsilon greedy policy
                if (i < trainingIteration):
                    epsilon = 100 / float(100 + stateCount[(gameplay.playerCardPoints, gameplay.dealerFirstCardPoint, gameplay.playerCardUsableAce)])
                    action = strategy.EpsilonGreedyPolicyFromQTableDict(epsilon, QTableDict, gameplay.playerCardPoints, gameplay.dealerFirstCardPoint, gameplay.playerCardUsableAce)
                # in testing phase, use greedy policy
                else:
                    action = strategy.BestActionPolicyFromQTableDict(QTableDict, gameplay.playerCardPoints, gameplay.dealerFirstCardPoint, gameplay.playerCardUsableAce)

            # if (playerCardPoints, dealerFirstCardPoint, action) is the newly occurred key
            # store this key for an update of Q-table in the end of this gameplay
            if (gameplay.playerCardPoints, gameplay.dealerFirstCardPoint, gameplay.playerCardUsableAce, action) not in occurredStateActions and gameplay.playerCardPoints <= winningPoints:
                occurredStateActions.append((gameplay.playerCardPoints, gameplay.dealerFirstCardPoint, gameplay.playerCardUsableAce, action))

            # game proceed by the player's action
            # playerCardPoints, dealerCardPoints and reward will be updated
            [gameplay.playerCardPoints, gameplay.dealerCardPoints, gameplay.playerCardUsableAce, reward] = gameplay.GameProceed(gameplay, action, winningPoints, dealerCriticalPointsToStick)

            # game is finished if reward is out
            if (reward is not None):
                gameplay.finish = True

        # in training phase, use epsilon greedy policy, update the Q table dict
        if (i < trainingIteration):
            strategy.UpdateQTableDict(reward, occurredStateActions, QTableDict, stateCount, stateActionCount, method)
        # in testing phase, update the test result list
        else:
            if (reward == 1):
                testResult [0] += 1
            elif (reward == -1):
                testResult [2] += 1
            else:
                testResult [1] += 1

    print("After train for ", trainingIteration, " iterations using", method)
    print("Our game bot fights against the dealer for ", testingIteration, " rounds")
    print("Win: ", (float)(testResult [0])/testingIteration*100.0, "%")
    print("Draw: ", (float)(testResult [1])/testingIteration*100.0, "%")
    print("Lose: ", (float)(testResult [2])/testingIteration*100.0, "%")
    print()

    return QTableDict