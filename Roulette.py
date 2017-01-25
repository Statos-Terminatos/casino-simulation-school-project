import random


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
                raise TypeError("Please enter a real bet, in numbers")

            if betted_amount >= self.minimum_bet:
                resultBet.append(1)
            else:
                resultBet.append(0)

        return resultBet

    def SpinTheWheel(self, bets):
        print("Spinning the wheel...")
        result_guess = []

        # Check the bets are between 0 and 36
        for bet in bets:
            if bet < 0 or bet > 36:
                raise ValueError("Please give a bet between 0 and 36")

        lucky_number = random.randrange(0, 36)
        print("Ball lands on {}".format(lucky_number))

        # number of winners
        number_correct_bets = 0

        for bet in bets:
            if bet == lucky_number:
                result_guess.append(1)
                number_correct_bets = number_correct_bets + 1
            else:
                result_guess.append(0)

        if number_correct_bets > 0:
            print("There are {} correct bet(s)".format(number_correct_bets))
        else:
            print("No winners this round")
        return lucky_number, result_guess

    def SimulateGame(self, bets, betted_amounts):
        can_play = self.AboveMinimum(betted_amounts)
        lucky_number, result_bets = self.SpinTheWheel(bets)

        winners = []
        # Zip is used for looping through 2 lists
        for w_l, guess in zip(can_play, result_bets):
            winners.append(w_l * guess)

        cash = []
        casino = 0

        for winner, betted_amount in zip(winners, betted_amounts):
            if winner:
                # winners cash money
                cash.append(betted_amount * 30)
            else:
                # Casino cash the money lost players betted
                cash.append(0)
                casino = casino + betted_amount

        return [casino, cash]