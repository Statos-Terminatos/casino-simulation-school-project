class Employee:
    def __init__(self, fixed_wage):
        self.fixed_wage = fixed_wage


class Croupier(Employee):
    def __init__(self, fixed_wage, variable_percentage):
        super(self.__class__, self).__init__(fixed_wage)
        self.variable_percentage = variable_percentage
        self.variable_wage = []

    def GatherProfit(self, gains):
        mymoney = self.variable_percentage * gains
        print("Croupier: I finished a game and I earned {}".format(mymoney))
        self.variable_wage.append(mymoney)
        return mymoney

    def GetWage(self):
        return self.fixed_wage + sum(self.variable_wage)


class Barman(Employee):
    def __init__(self, fixed_wage):
        super(self.__class__, self).__init__(fixed_wage)
        self.tips = []

    def GatherTip(self, tip):
        print("Barmen: You bought a drink, I just got a tip {}".format(tip))
        self.tips.append(tip)

    def GetWage(self):
        # Tips are payed by the customer and not the
        # the casino
        return self.fixed_wage
