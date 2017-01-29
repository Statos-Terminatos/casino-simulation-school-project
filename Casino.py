import random

from Roulette import Roulette
from Craps import Craps
from Employee import Croupier, Barman
from Customer import OneTimeCustomer, BachelorCustomer, RegularCustomer


class Casino:
    def __init__(self, roulette_tables,
                 craps_tables, barmen_number, wage, casino_cash,
                 customers_number, percent_regular_customers,
                 percent_bachelor_customers, free_budget):

        self.roulette_tables = roulette_tables
        self.craps_tables = craps_tables
        self.barmen_number = barmen_number
        self.wage = wage
        self.casino_cash = casino_cash
        self.customers_number = customers_number
        self.percent_regular_customers = percent_regular_customers
        self.percent_bachelor_customers = percent_bachelor_customers
        self.free_budget = free_budget
        self.OpenCasino()

    def OpenCasino(self):

        self.croupiers = []
        self.tables = []
        self.barmen = []
        self.drinks = []
        self.bachelros = []
        # Create all the roulette tables with their croupier

        for _ in range(self.roulette_tables):
            croupier = Croupier(self.wage, 0.005)
            self.croupiers.append(croupier)
            self.tables.append(Roulette(croupier))

        # Create Craps tables
        for _ in range(self.craps_tables):
            croupier = Croupier(self.wage, 0.005)
            self.croupiers.append(croupier)
            self.tables.append(Craps(0.9, croupier))

        for _ in range(self.barmen_number):
            self.barmen.append(Barman(self.wage))

    def DistributeCustomers(self):
        # Values will be overwritten by the pulled customers

        customers = self.customers
        tables = self.tables

        distribution = []
        for _ in range(len(self.tables)):
            distribution.append([])

        random.shuffle(tables)
        for i, _ in enumerate(customers):
            random.shuffle(customers)
            random_place = random.randint(0, len(tables) - 1)
            distribution[random_place].append(customers.pop())

        return distribution

    def WelcomeCustomers(self):
        # Calculate customers
        self.customers = []
        regular_customers = round(self.customers_number * self.percent_regular_customers)
        bachelor_customers = round(self.customers_number * self.percent_bachelor_customers)
        one_time_customers = self.customers_number - regular_customers - bachelor_customers

        print("the customers numbers are {} R, {} B, {} OT".format(
            regular_customers, bachelor_customers, one_time_customers))

        for _ in range(regular_customers):
            rc = RegularCustomer()
            self.customers.append(rc)

        for _ in range(bachelor_customers):
            bc = BachelorCustomer()
            self.customers.append(bc)

        for _ in range(one_time_customers):
            otc = OneTimeCustomer()
            self.customers.append(otc)

    def PlayOneRound(self):
        results = []
        for table_index, customers in enumerate(self.dist):
            game = self.tables[table_index]
            betted_amounts = []
            # gather bets from customers
            for customer in customers:
                if str(customer) == "RegularCustomer":
                    bet = customer.Bet(game.minimum_bet)
                else:
                    bet = customer.Bet()

                betted_amounts.append(bet)

            print("betted_amounts", betted_amounts)
            print("customers:", customers)
            # Play the game
            result_game = game.SimulateGame(betted_amounts)
            # Give the won money to the customers
            for result_customer, customer in zip(result_game[1], customers):
                customer.CashMoney(result_customer)
            # Pay the croupier
            game.croupier.GatherProfit(result_game[0])
            results.append(result_game)
            print(result_game)
            print("--------------------")
        return results

    def GetDrinks(self, number=1):
        for _ in range(number):
            # allCustomers = [inner for outer in x for inner in outer]
            # random.sample(a, 2)
            for table_index, customers in enumerate(self.dist):
                for customer in customers:
                    price = customer.TryToBuyDrink()
                    if price:
                        # Random barman
                        barmen_number_to_tip = random.randint(0, len(self.barmen) - 1)
                        self.barmen[barmen_number_to_tip].GatherTip(customer.GiveTip())
                        self.drinks.append(price)

    def SetUp(self):
        # Reset all the tables and customers
        self.OpenCasino()
        # Compute the customers
        self.WelcomeCustomers()
        # Distribute them
        self.dist = self.DistributeCustomers()

    def SimulateEvening(self):
        self.SetUp()

        # Give money to bachelros once
        for table_index, customers in enumerate(self.dist):
            for customer in customers:
                if str(customer) == "BachelorCustomer":
                    customer.GetFreeMoney(self.free_budget)
                    self.bachelros.append(self.free_budget)

        # 3 rounds
        results = []
        for _ in range(3):
            self.GetDrinks()
            results += self.PlayOneRound()

        # Calculate cash flow
        croupiers_salary = []
        for table_index, customers in enumerate(self.dist):
            croupiers_salary.append(self.tables[table_index].croupier.GetWage())

        casino_money = sum([result[0] for result in results])
        payed_money = sum([sum(result[1]) for result in results])

        casino_gains = casino_money - payed_money

        drinks_profit = sum(self.drinks)
        wages = sum(croupiers_salary) + sum([b.GetWage() for b in self.barmen])
        offred_money = sum(self.bachelros)

        balance = casino_gains + drinks_profit - (wages + offred_money)
        print("Casino balance: ", balance)
        self.casino_cash += balance

        barmen_salery = [b.GetWage() + sum(b.tips) for b in self.barmen]
        return barmen_salery, croupiers_salary