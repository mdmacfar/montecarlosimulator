from mcs_pkg import *

# create a sample game with two dice
die1 = Die([1,2,3,4,5,6])
die2 = Die([1,2,3,4,5,6])
game = Game([die1, die2])

# play the game 1000 times
game.play(1000)

# show the jackpot results
an = Analyzer(game)
an_jackpot = an.count_jackpots()
an_flips = game.results.shape[0]
an_jackpot
an_flips
an_freq = an_jackpot / an_flips
print(an_freq)