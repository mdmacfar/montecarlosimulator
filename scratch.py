from mcs_pkg.montecarlo import Die, Game, Analyzer

# Setup: A fair coin (with faces H and T) and one unfair coin, 
# in which one of the faces has a weight of 5 and the others 1.
fair_coin = Die(['H', 'T'])
unfair_coin = Die(['H', 'T'])
unfair_coin.change_weight('H', 5)

# Here's a game of 1000 flips with all fair coins.
fairgame = Game([fair_coin, fair_coin])
fairgame.play(1000)
fairgame_analyzer = Analyzer(fairgame)
fairgame_jackpot = fairgame_analyzer.count_jackpots()
fairgame_flips = fairgame.results.shape[0]
fairgame_jackpot
fairgame_flips
fairgame_freq = fairgame_jackpot / fairgame_flips
print(fairgame_freq)
