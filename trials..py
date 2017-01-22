import Roulette
rg = Roulette.Roulette(5)

print(rg.AboveMinimum([1, 20, 6, 3, 2]))
print(rg.SpinTheWheel([1, 2, 24]))

lucky, result_bets = rg.SpinTheWheel([1, 2, 23])
print (lucky, result_bets)
