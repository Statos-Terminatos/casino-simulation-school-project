import random
from CasinoGame import CasinoGame



class Roulette(CasinoGame):

    def __init__(self, croupier):
        super(self.__class__, self).__init__(
            (0, 36),
            [50, 100, 200],
            lambda: random.randint(0, 36),
            # The prizes for roulette are bets*30
            lambda _,y: y*30,
            croupier
        )

    def SpinTheWheel(self, bets):
        return super(self.__class__, self).Start(bets)
