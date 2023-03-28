class Person:
    def __init__(self, money, risk, taxrate):
        self.money = money
        self.risk = risk
        self.taxrate = taxrate
        self.numberofShares = []

    def buy(self, number, price):
        if self.money > number * price:
            self.money -= number * price
        else:
            number = int(self.money / price)
            self.money -= number * price
