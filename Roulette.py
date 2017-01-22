import random

# This is used to fixed the random generator so we can test the output 
random.seed(3456)

class Roulette(object):
    # Initialization method
    def __init__(self, minimum_bet):
        self.minimum_bet = minimum_bet

    def AboveMinimum(self, betted_amounts):

        # Result to return
        resultBet = []

        # For each bet, compare with minimum bet
        for betted_amount in betted_amounts:

            if type(betted_amount) not in [int, float]:
                print("Please enter a real bet, in numbers")

            if self.minimum_bet > betted_amount:
                print("Bet is lower than minimum bet")
                resultBet.append(False)
            else:
                print("Bet is allowed")
                resultBet.append(True)

        return resultBet

    def SpinTheWheel(self, bets):
        result_bets = []

        # Check the bets are between 0 and 36
        for bet in bets:
            if bet < 0 or bet > 36:
                print("Please give a bet between 0 and 36")
                return False

        lucky_number = random.randrange(0, 36)
        print("Ball lands on {}".format(lucky_number))

        # Check for winners
        for i, v in enumerate(bets):

            if v == lucky_number:
                result_bets.append(1)
            else:
                result_bets.append(0)

        return lucky_number, result_bets

