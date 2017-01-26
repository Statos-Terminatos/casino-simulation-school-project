import Craps
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

labels, values = zip(*Counter(Craps.Craps.Dices(1000)).items())
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width +0.5, labels)
plt.show()


import Roulette2
import random

# This is used to fixe the pseudo random generator so we can test the output


amounts = [10, 85, 120, 65, 150, 122]

table1 = Roulette2.Roulette()

print(table1.SimulateGame(amounts))

