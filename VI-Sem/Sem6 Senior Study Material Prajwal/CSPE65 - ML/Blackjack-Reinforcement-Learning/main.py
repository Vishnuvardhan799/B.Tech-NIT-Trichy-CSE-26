import bottraining as bt

# these are game variables, can skew them if you wish to
defaultDeckContent = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', \
                      '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', \
                      '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', \
                      '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

arbitraryDeckContent = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                        'A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', \
                      '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', \
                      '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', \
                      '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

initialNumberOfCard = 2
winningPoints = 21
dealerCriticalPointsToStick = 17;

# train agents using three different methods, (1) Q-learning (2) Sarsa (3) Temporal Difference, return Q table
QTableDictForQL = bt.TrainAndTestGameBot(10000000, 100000, "Q-Learning", defaultDeckContent, initialNumberOfCard, winningPoints, dealerCriticalPointsToStick)
QTableDictForSS = bt.TrainAndTestGameBot(10000000, 100000, "Sarsa", defaultDeckContent, initialNumberOfCard, winningPoints, dealerCriticalPointsToStick)
QTableDictForMC = bt.TrainAndTestGameBot(10000000, 100000, "Temporal Difference", defaultDeckContent, initialNumberOfCard, winningPoints, dealerCriticalPointsToStick)

# lambda function for determine hit or stick
HitOrStick = lambda hitQ, stickQ: "H" if hitQ >= stickQ else "S"

# report strategy result
for i in range(0, winningPoints*3-19):
    print(" ", end = "")
print("Q-learning", end = "")
print()

print("              player (usable ace)", end = " ")
for i in range(0, winningPoints*3-36):
    print(" ", end="")
print("player (no usable ace)    ")

print("          ", end = "")
for p in range(11, winningPoints+1):
    print(p, end = " ")
print("              ", end="")
for p in range(11, winningPoints+1):
    print(p, end = " ")
print()

for d in range (1,11):
    if (d == 10):
        print("      10   ", end = "")
    elif (d == 3):
        print("    D  3   ", end = "")
    elif (d == 4):
        print("    e  4   ", end = "")
    elif (d == 5):
        print("    a  5   ", end = "")
    elif (d == 6):
        print("    l  6   ", end = "")
    elif (d == 7):
        print("    e  7   ", end = "")
    elif (d == 8):
        print("    r  8   ", end = "")
    else:
        print("      ", d, "  ", end = "")

    for p in range(11, winningPoints+1):
        print(HitOrStick (QTableDictForQL[p,d,1,0], QTableDictForQL[p,d,1,1]), "", end = " ")

    if (d == 10):
        print("         10  ", end = " ")
    elif (d == 3):
        print("      D   3  ", end = " ")
    elif (d == 4):
        print("      e   4  ", end = " ")
    elif (d == 5):
        print("      a   5  ", end = " ")
    elif (d == 6):
        print("      l   6  ", end = " ")
    elif (d == 7):
        print("      e   7  ", end = " ")
    elif (d == 8):
        print("      r   8  ", end = " ")
    else:
        print("         ", d, " ", end = " ")

    for p in range(11, winningPoints+1):
        print(HitOrStick (QTableDictForQL[p,d,0,0], QTableDictForQL[p,d,0,1]), "", end = " ")
    print()
print()

for i in range(0, winningPoints*3-17):
    print(" ", end = "")
print("Sarsa", end = "")
print()

print("              player (usable ace)", end = " ")
for i in range(0, winningPoints*3-36):
    print(" ", end="")
print("player (no usable ace)    ")

print("         ", end = " ")
for p in range(11, winningPoints+1):
    print(p, end = " ")
print("             ", end=" ")
for p in range(11, winningPoints+1):
    print(p, end = " ")
print()

for d in range (1,11):
    if (d == 10):
        print("      10   ", end = "")
    elif (d == 3):
        print("    D  3   ", end = "")
    elif (d == 4):
        print("    e  4   ", end = "")
    elif (d == 5):
        print("    a  5   ", end = "")
    elif (d == 6):
        print("    l  6   ", end = "")
    elif (d == 7):
        print("    e  7   ", end = "")
    elif (d == 8):
        print("    r  8   ", end = "")
    else:
        print("      ", d, "  ", end = "")

    for p in range(11, winningPoints+1):
        print(HitOrStick (QTableDictForSS[p,d,1,0], QTableDictForSS[p,d,1,1]), "", end = " ")

    if (d == 10):
        print("         10  ", end = " ")
    elif (d == 3):
        print("      D   3  ", end = " ")
    elif (d == 4):
        print("      e   4  ", end = " ")
    elif (d == 5):
        print("      a   5  ", end = " ")
    elif (d == 6):
        print("      l   6  ", end = " ")
    elif (d == 7):
        print("      e   7  ", end = " ")
    elif (d == 8):
        print("      r   8  ", end = " ")
    else:
        print("         ", d, " ", end = " ")

    for p in range(11, winningPoints+1):
        print(HitOrStick (QTableDictForSS[p,d,0,0], QTableDictForSS[p,d,0,1]), "", end = " ")

    print()
print()

for i in range(0, winningPoints*3-23):
    print(" ", end = "")
print("Temporal Difference", end = "")
print()

print("              player (usable ace)", end = " ")
for i in range(0, winningPoints*3-36):
    print(" ", end="")
print("player (no usable ace)    ")

print("         ", end = " ")
for p in range(11, winningPoints+1):
    print(p, end = " ")
print("             ", end=" ")
for p in range(11, winningPoints+1):
    print(p, end = " ")
print()

for d in range (1,11):
    if (d == 10):
        print("      10   ", end = "")
    elif (d == 3):
        print("    D  3   ", end = "")
    elif (d == 4):
        print("    e  4   ", end = "")
    elif (d == 5):
        print("    a  5   ", end = "")
    elif (d == 6):
        print("    l  6   ", end = "")
    elif (d == 7):
        print("    e  7   ", end = "")
    elif (d == 8):
        print("    r  8   ", end = "")
    else:
        print("      ", d, "  ", end = "")

    for p in range(11, winningPoints+1):
        print(HitOrStick (QTableDictForMC[p,d,1,0], QTableDictForMC[p,d,1,1]), "", end = " ")

    if (d == 10):
        print("         10  ", end = " ")
    elif (d == 3):
        print("      D   3  ", end = " ")
    elif (d == 4):
        print("      e   4  ", end = " ")
    elif (d == 5):
        print("      a   5  ", end = " ")
    elif (d == 6):
        print("      l   6  ", end = " ")
    elif (d == 7):
        print("      e   7  ", end = " ")
    elif (d == 8):
        print("      r   8  ", end = " ")
    else:
        print("         ", d, " ", end = " ")

    for p in range(11, winningPoints+1):
        print(HitOrStick (QTableDictForMC[p,d,0,0], QTableDictForMC[p,d,0,1]), "", end = " ")

    print()

