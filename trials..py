import Roulette
import random

# This is used to fixe the pseudo random generator so we can test the output
random.seed(3456)

amounts = [10, 85, 120, 65, 150, 122]
bets = [10, 24, 36, 0, 11, 24]

table1 = Roulette.Roulette(100)

print(table1.SimulateGame(bets, amounts))
print(table1.SimulateGame(bets, amounts))