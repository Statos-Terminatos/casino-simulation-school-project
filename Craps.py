import random

random.seed(3456)

class Craps(object):
    def __init__(self, minimum_bet):
        self.minimum_bet = minimum_bet

    def AboveMinimum(self, betted_amounts):
        resultBet = []

        for betted_amount in betted_amounts:
            if betted_amount >= self.minimum_bet:
                resultBet.append(1)
            else:
                resultBet.append(0)
        return resultBet

    def Dices(simulation):
        rolls = []
        for num in range(simulation):
            sum_dices = random.randint(1,6) + random.randint(1,6)
            rolls.append(sum_dices)
        return rolls

    def RollTheDices(self, bets):
        result_guess = []
        for bet in bets:
            if bet < 0 or bet > 36:
                raise ValueError("Please give a bet between 0 and 36")

        lucky_number = random.randint(2,12)

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
        can_play =  self.AboveMinimum(betted_amounts)
        lucky_number, result_guess = self.RollTheDices(bets)

        winners = []
        # Zip is used for looping through 2 lists
        for w_l, guess in zip(can_play, result_guess):
            winners.append(w_l * guess)

        cash_players = []
        cash_casino = 0

        for winner, betted_amount in zip(winners, betted_amounts):
            if winner:
                # winners cash money
                cash_players.append(betted_amount)
            else:
                # Casino cash the money lost players betted
                cash_players.append(0)
                cash_casino = cash_casino + betted_amount

        return [cash_casino, cash_players]

print(Craps.Dices(10))
