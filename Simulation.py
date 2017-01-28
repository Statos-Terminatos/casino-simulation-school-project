import random
import sys
import os

import Roulette
import Craps
from Casino import Casino
from Employee import Barman, Croupier
from Customer import OneTimeCustomer, BachelorCustomer, RegularCustomer

from matplotlib import pyplot

# This is used to fixe the pseudo random generator so we can test the output


# res = []
# total1 = 0
# total2 = 0
# for i in range(10000):
#     craps = Craps.Craps(0.9, 1)
#     table = Roulette.Roulette(1)
#     amounts1 = [random.randrange(50, 200) for x in range(10)]
#     amounts2 = [random.randrange(40, 300) for x in range(10)]
#     res1 = craps.SimulateGame(amounts1)
#     res2 = table.SimulateGame(amounts2)
#     print("--------------------------\n")
#     total1 = total1 + sum(res1[1])/sum(amounts1)
#     total2 = total2 + sum(res2[1])/sum(amounts2)
#     print( "total: {}%".format(total1) )
#     print( "total: {}%".format(total2) )
#     print("--------------------------\n")

# print(total1/10000*100)
# print(total2/10000*100)


# Disable print to the stdout
# print will slow the computation
 #f = open(os.devnull, 'w')
#sys.stdout = f

casino = Casino(10, 10, 4, 200, 50000, 100, 0.2, 0.1, 60)

money = []
for _ in range(10):
	casino.SimulateEvening()
	money.append(casino.casino_cash)

print(sum(money))

#f.close()
#sys.stdout = sys.__stdout__

pyplot.bar(range(10), money, 0.01)
pyplot.show()



