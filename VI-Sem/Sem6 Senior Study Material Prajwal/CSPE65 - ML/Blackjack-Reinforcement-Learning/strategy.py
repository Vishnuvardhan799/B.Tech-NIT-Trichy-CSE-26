import random

class Strategy:

    def RandomAction(self):
        if random.random() <= 0.5:
            return 0
        else:
            return 1

    def EpsilonGreedyPolicyFromQTableDict(self, epsilon, QTableDict, playerCardPoints, dealerCardPoints, playerCardUsableAce):
        # P = epsilon: exploration
        if random.random() < epsilon:
            return self.RandomAction()
        # P = 1-epsilon: exploitation
        else:
            return self.BestActionPolicyFromQTableDict(QTableDict, playerCardPoints, dealerCardPoints, playerCardUsableAce)

    def BestActionPolicyFromQTableDict(self, QTableDict, playerCardPoints, dealerCardPoints, playerCardUsableAce):
        # Q function for state (playerCardPoints, dealerCardPoints, hit)
        hitValue = QTableDict[(playerCardPoints, dealerCardPoints, playerCardUsableAce, 0)]
        # Q function for state (playerCardPoints, dealerCardPoints, stick)
        stickValue = QTableDict[(playerCardPoints, dealerCardPoints, playerCardUsableAce, 1)]

        if hitValue > stickValue:
            return 0
        elif stickValue > hitValue:
            return 1
        else:
            return self.RandomAction()

    def UpdateQTableDict(self, reward, occurredStateActions, QTableDict, stateCount, stateActionCount, method, gamma = 0.8):
        # update over all keys
        for i in range(len(occurredStateActions)):
            state = occurredStateActions[i][:-1]
            stateAction = occurredStateActions[i]
            # update counts
            stateCount[state] += 1
            stateActionCount[stateAction] += 1

            # set the learning rate
            alpha = 1.0 / stateActionCount[stateAction]

            # update value function
            # for Q-learning or Sarsa
            if (method == "Q-Learning" or method == "Sarsa"):
                previousQ = QTableDict[stateAction]
                # calculate the best Q value for (next state, best action)
                if i < len(occurredStateActions) - 1:
                    # for Q-learning
                    if (method == "Q-Learning"):
                        nextStateHitAction = occurredStateActions[i + 1][:-1] + (0,)
                        nextStateStickAction = occurredStateActions[i + 1][:-1] + (1,)
                        maxvalue = max(QTableDict[nextStateHitAction], QTableDict[nextStateStickAction])
                        bestNextQ = gamma * maxvalue
                    # for Sarsa
                    else:
                        nextStateAction = occurredStateActions[i + 1]
                        bestNextQ = gamma * QTableDict[nextStateAction]
                else:
                    bestNextQ = 0

                # update the Q table dict
                QTableDict[occurredStateActions[i]] = (1 - alpha) * previousQ + alpha * (reward + bestNextQ)

            # for Temporal Difference
            else:
                QTableDict[occurredStateActions[i]] += alpha * (reward - QTableDict[occurredStateActions[i]])