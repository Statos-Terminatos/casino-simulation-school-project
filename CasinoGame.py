import random


class CasinoGame(object):
    """
    Abstraction class for caisno games
    """

    def __init__(self, game_type, guess_range):
        self.game_type = game_type
        self.guess_range = guess_range
        self.SetMinimumBet()

    def SetMinimumBet(self):
        if self.game_type == "R":
            minimum_bet = random.choice([50, 100, 200])
        elif self.game_type == "C":
            minimum_bet = random.choice([0, 25, 50])

        self.minimum_bet = minimum_bet

    def AboveMinimum(self, betted_amounts):
        resultBet = []

        for betted_amount in betted_amounts:
            if type(betted_amount) not in [int, float]:
                raise TypeError("Please enter a real bet, in numbers")

            if betted_amount >= self.minimum_bet:
                resultBet.append(1)
            else:
                resultBet.append(0)

        return resultBet

    def Start(self, bets):
        result_guess = []

        # Check the bets are between 0 and 36
        for bet in bets:
            if bet < self.guess_range[0] or bet > self.guess_range[1]:
                raise ValueError("Please give a bet between {} and {}".format(*self.guess_range))

        lucky_number = self.GenerateLuckyNumber()
        print("Lucky number is {}".format(lucky_number))

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

    def GenerateLuckyNumber(self):
        if self.game_type == "R":
            lucky_number = random.randint(0, 36)
        elif self.game_type == "C":
            lucky_number = random.randint(1, 6) + random.randint(1, 6)

        return lucky_number

    def GenerateBets(self, number):
        # This is not optimized, doing the if way more times than
        # we should, may be we can use generators to get around this.
        return [self.GenerateLuckyNumber() for x in range(number)]

    def SimulateGame(self, betted_amounts):
        can_play = self.AboveMinimum(betted_amounts)
        bets = self.GenerateBets(len(betted_amounts))
        print("Bets are {}".format(bets))
        lucky_number, result_bets = self.Start(bets)

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
