import random

class GamePlay:

    # initialize essential elements of a gameplay: players, deck, card points, etc
    def __init__(self, deckContent, initialNumberOfCard, winningPoints):

        self.finish = False
        self.playerCards = []
        self.dealerCards = []
        self.playerCardPoints = 0
        self.dealerCardPoints = 0
        self.playerCardUsableAce = 0;
        self.dealerFirstCardPoint = 0;

        # describe what cards are contained in the deck
        self.deckContent = deckContent[:]

        # randomly shuffle the deck
        self.ShuffleDeck()

        # player draw #initialNumberOfCard cards
        for i in range (initialNumberOfCard):
            self.playerCards.append(self.DrawACard())

        # dealer draw #initialNumberOfCard cards
        for i in range (initialNumberOfCard):
            self.dealerCards.append(self.DrawACard())
            if (i == 0):
                self.dealerFirstCardPoint = self.CalculateDealerFirstCardPoint (self.dealerCards)

        # calculate total points from the card
        self.playerCardPoints, self.playerCardUsableAce = self.CalculateCardPoints (self.playerCards, winningPoints)
        self.dealerCardPoints, dummy = self.CalculateCardPoints (self.dealerCards, winningPoints)

    # Randomize the order of the cards in the deck
    def ShuffleDeck (self):
        random.shuffle(self.deckContent)

    # draw the toppest card (index 0), remove the drawn card from the deck
    def DrawACard (self):
        return self.deckContent.pop(0)

    # given dealer first card point
    def CalculateDealerFirstCardPoint(self, cards):
        # if  card is '2' to '10'
        if cards[0].isdigit():
            return int(cards[0])
        # if card is 'A'
        elif cards[0] == 'A':
            return 1
        # if card is J, Q or K
        else:
            return 10

    # given the player cards, calculate the total points
    def CalculateCardPoints(self, cards, winningPoints):
        points = 0
        aceQuantity = 0
        usableAce = 0
        for card in cards:
            # if  card is '2' to '10'
            if card.isdigit():
                points += int(card)
            # if card is 'A', assume first an ace worth 11 points, reduce it to 1 point if the total points > winningPoints
            elif card == 'A':
                points += 11
                aceQuantity += 1
            # if card is J, Q or K
            else:
                points += 10
        # adjust the total points if has aces and points > winningPoints
        while aceQuantity > 0 and points > winningPoints:
            aceQuantity -= 1
            points -= 10

        # check if there is usable ace
        if (aceQuantity > 0):
            usableAce = 1

        return points, usableAce

    # game proceed by the player's action
    def GameProceed (self, gameplay, action, winningPoints, dealerCriticalPointsToStick):

        reward = None
        playerCardPoints = gameplay.playerCardPoints
        dealerCardPoints = gameplay.dealerCardPoints
        playerCardUsableAce = gameplay.playerCardUsableAce

        # if player chooses to hit
        if (action == 0):
            gameplay.playerCards.append(gameplay.DrawACard())
            playerCardPoints, playerCardUsableAce = gameplay.CalculateCardPoints(gameplay.playerCards, winningPoints)

            if (playerCardPoints) > winningPoints:
                reward = -1
        # if player chooses to stick, then dealer's turn to draw card
        else:
            # dealer only sticks hen his points >= dealerCriticalPointsToStick
            while dealerCardPoints < dealerCriticalPointsToStick:
                gameplay.dealerCards.append(gameplay.DrawACard())
                dealerCardPoints, dummy = gameplay.CalculateCardPoints(gameplay.dealerCards, winningPoints)

            # when both player and dealer choose to stick, determine which one is winner
            if dealerCardPoints > winningPoints:
                reward = 1
            else:
                if playerCardPoints <= winningPoints:
                    if playerCardPoints < dealerCardPoints:
                        reward = -1
                    elif playerCardPoints == dealerCardPoints:
                        reward = 0
                    elif playerCardPoints > dealerCardPoints:
                        reward = 1

        return playerCardPoints, dealerCardPoints, playerCardUsableAce, reward