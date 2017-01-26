import random
from CasinoGame import CasinoGame


class Roulette(CasinoGame):

    def __init__(self):
        super(self.__class__, self).__init__("R", (0, 36))

    def SpinTheWheel(self, bets):
        return super(self.__class__, self).Start(bets)
