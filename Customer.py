import random


class Customer:
    def __init__(self, money):
        self.money = money

    # A drink costs 20$ and the tip is randomly determined between 0$ to 20$.
    #  They buy only if they have more than 60$ cash
    def TryToBuyDrink(self):
        if self.money>60:
            self.money = self.money - 20
            return 20
        else:
            return 0

    def GiveTip(self):
        tip = random.randint(0,20)
        self.money = self.money - tip
        return tip

    def CashMoney(self, gains):
        if gains:
            print("Customer: I won {}".format(gains))
        self.money += gains

    def __str__(self):
        # For printing the customer with str() or print
        return self.__class__.__name__

    def __repr__(self):
        # For printing the customer inside a list
        return self.__class__.__name__


class RegularCustomer(Customer):
    # They always place the minimum table bet. They never bet more but never less,
    # They enter the evening with a random amount between 100$ to 300$
    def __init__(self):
        money = random.randint(100, 300)
        super(self.__class__, self).__init__(money)

    def Bet(self, minimum_bet):
        if self.money > minimum_bet:
            bet = minimum_bet
        else:
            bet = self.money

        self.money = self.money - bet
        return bet


class OneTimeCustomer(Customer):
    def __init__(self):
        money = random.randint(200, 300)
        super(self.__class__, self).__init__(money)

    #They usually bet between 0 to one-third of their money at that time
    def Bet(self):
        bet = random.randint(0, round(1/3*self.money))
        self.money = self.money - bet
        return bet


class BachelorCustomer(Customer):
    def __init__(self):
        money = random.randint(200, 500)
        super(self.__class__, self).__init__(money)

    def Bet(self):
        bet = random.randint(0, self.money)
        self.money = self.money - bet
        return bet

    def GetFreeMoney(self, amount):
        print("Bachelor: I got offer {} !".format(amount))
        self.money = self.money + amount
