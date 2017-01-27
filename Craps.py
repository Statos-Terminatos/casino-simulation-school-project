import random
from CasinoGame import CasinoGame


class Craps(CasinoGame):

    def __init__(self, expected_return, croupier):
        super(self.__class__, self).__init__(
            (2, 12),
            [0, 25, 50],
            lambda: random.randint(1,6) + random.randint(1,6),
            # The prizes for craps are dependent on the number to bet on
            # and the expected return
            lambda x, y: round(y*expected_return*36/(6 - abs(x - 7))),
            croupier
        )

    def Dices(self):
        return self.callable_generate_random()

    def RollTheDices(self, bets):
        return super(self.__class__, self).Start(bets)