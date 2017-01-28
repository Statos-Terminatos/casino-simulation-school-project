import random


class CasinoGame:
    """
    Abstraction class for caisno games
    """

    def __init__(self, guess_range, minimum_bets, callable_generate_random,
                 callable_calculate_prize, croupier):
        self.guess_range = guess_range
        self.minimum_bet = random.choice(minimum_bets)
        # This is a callable function, to generate the lucky number
        self.callable_generate_random = callable_generate_random
        self.calculate_prize = callable_calculate_prize
        self.croupier = croupier

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

        # Check the bets are between self.guess_range
        for bet in bets:
            if bet < self.guess_range[0] or bet > self.guess_range[1]:
                raise ValueError(
                    "Please give a bet between {} and {}".format(*self.guess_range))

        lucky_number = self.callable_generate_random()
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

    def GenerateBets(self, number):
        return [self.callable_generate_random() for x in range(number)]

    def SimulateGame(self, betted_amounts):

        can_play = self.AboveMinimum(betted_amounts)
        bets = self.GenerateBets(len(betted_amounts))
        print("Bets are {}".format(bets))
        print("The minimum amount for this game is {}".format(self.minimum_bet))
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
                cash.append(self.calculate_prize(lucky_number, betted_amount))
            else:
                # Casino cash the money lost players betted
                cash.append(0)
                casino = casino + betted_amount

        # The end of the game, means we pay the croupier here
        return [casino, cash]
