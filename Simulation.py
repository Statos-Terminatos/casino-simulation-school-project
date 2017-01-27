import Roulette
import Craps
import random

from Employee import Barman, Croupier
# This is used to fixe the pseudo random generator so we can test the output


res = []
total1 = 0
total2 = 0
for i in range(10000):
    craps = Craps.Craps(0.9, 1)
    table = Roulette.Roulette(1)
    amounts1 = [random.randrange(50, 200) for x in range(10)]
    amounts2 = [random.randrange(40, 300) for x in range(10)]
    res1 = craps.SimulateGame(amounts1)
    res2 = table.SimulateGame(amounts2)
    print("--------------------------\n")
    total1 = total1 + sum(res1[1])/sum(amounts1)
    total2 = total2 + sum(res2[1])/sum(amounts2)
    print( "total: {}%".format(total1) )
    print( "total: {}%".format(total2) )
    print("--------------------------\n")

print(total1/10000*100)
print(total2/10000*100)

#b = Barman("aliya", 300)
#print(b)



