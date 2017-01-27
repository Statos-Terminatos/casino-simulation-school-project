class Employee(object):
    def __init__(self, name, fixed_wage):
        self.name = name
        self.fixed_wage = fixed_wage

    def GetWage(self):
        return self.variable_wage + self.fixed_wage

    def __str__(self):
        return "My name is {}".format(self.name)


class Croupier(Employee):
    def __init__(self, name, fixed_wage, variable_percentage):
        super(self.__class__, self).__init__(self, name, fixed_wage)
        self.variable_percentage = variable_percentage

    def SetVariableWage(self, gains):
        self.variable_wage = self.variable_percentage * gains

    def GetWage(self):
        return self.fixed_wage + self.variable_wage


class Barman(Employee):
    def SetVariableWage(self, tip):
        self.tips.append(tip)

    def GetWage(self):
        return self.fixed_wage + sum(self.tips)
