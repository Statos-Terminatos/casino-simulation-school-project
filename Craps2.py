import random
from CasinoGame import CasinoGame


class Craps(CasinoGame):

    def __init__(self):
        super(self.__class__, self).__init__("R", (0, 36))

    def Dices():
        return super(self.__class__, self).GenerateLuckyNumber()

    def RollTheDices(self, bets):
        return super(self.__class__, self).Start(bets)