# BlackJack RL

This is a BlackJack engine that I made while watching the David Silver lectures on Reinforcement Learning

### Reinforcement Learning algorithms implemented:

* Monte Carlo Learning: wins 46.6% of the games on average
* TD Lambda: wins 46.7% of the games on average
* Linear Function Approximator with 96 features: wins 43.8% of the games on average
* Linear Function Approximator with 10816 features: wins 45.8% of the games on average
* Neural Network Approximator with Theano and Tensorflow: wins 34.9% of the games on average

First three were trained by running 50000 episodes, and last two were trained on only 2000 (more were not run because it'd take too long on my Mac)
Each was evaluated by training and testing ten times from start to get a better average value of win percentages (see main.py) (again, more were not run because it'd take too long on my Mac)
Despite limited resources, the algorithms did manage to improve the player. Compared to these, a Random AI wins 33.5% of the games on average. In fact, simply training on just a 100 episodes can get better than random performance consistently
The lower-than-50% percentages (which means they will all lose money in a casino) can be attributed to the stochastic nature of the game, and the fact that it was designed to make the dealer win more often on average (house always wins).


### Classes:

#### Deck

Deck class with 52 card objects, each with a different number and suit. New cards are drawn without replacement

#### BlackJack

A game of BlackJack that can be played by up to four players plus a dealer.
Has the ability to take one step at a time taking in all player actions. Player actions can be HIT or STICK.
At any point, if a player goes bust, they get a negative reward and the game goes on.
If all players stick, the dealer goes until it either sticks or goes bust. Either way, the highest total wins
If all players go bust, the game ends and all players get a negative reward.

#### Player

A base class for a player. Has methods for adding new card to player and returning current total. Handles the ace being used as 1 or 11 depending on current total

##### HumanPLayer

A human player that chooses actions based on user input. In case you ever feel like playing against an AI player

##### RandomPLayer

A control player to test against. This randomly takes the action to hit or stick. The goal is to consistently do better than this player

##### Monte Carlo Player

First Reinforcement Learning player. Uses Monte Carlo algorithm to estimate Q values

##### TD Learning Player

Uses TD Lambda algorithm with eligibility traces to estimate Q values. This is currently the best performing algorithm

##### LinearFunctionApproximator

Uses a linear function approximator for Q values instead of a table to store them. Currently uses 96 features and a learning rate of 0.01
Two different kinds of features are available. One is card totals (dealer's total, player total, number of aces used). 
The other is more detailed and has all actual cards (dealer's first card, all of the player's cards). The idea was maybe it'll learn probabilities and a basic card counting. But I image I'd have to run it for millions of episodes to see that.

##### NeuralNetworkApproximator

Uses a neural network function approximator for Q values. Uses two kinds of networks, one using Theano and other using TensorFlow. Theano is significantly slower.
It also uses experience replay to avoid divergence in the network
A little disappointing since even Tensorflow takes way, way more time to train for 10,000 episodes, and running for only 2000 episodes, as I did above, does not yield any good results.
Hopefully, at some point, I can train all the algorithms for a million episodes on a rented GPU, but not today.

### Future:

* Hopefully, at some point, I can train all the algorithms for a million episodes on a rented GPU, but not today.
* I also haven't really tuned any hyperparameters and chosen valued that seemed reasonable
* These are the basic algorithms. There are some better algorithms out there, like TRPO and PPO that I haven't tried yet
* The players were trained using Player-vs-Dealer games only. But the game allows multiple players to compete against each other. I'd like to see how the players play when trained to play against other players as well.