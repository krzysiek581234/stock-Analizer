class Person:
    def __init__(self, money, risk, taxrate):
        self.money = money
        self.risk = risk
        self.taxrate = taxrate
        self.numberofShares = 0

    def buy(self, number, price):
        if self.money < number * price:
            number = int(self.money / price)
        self.money -= number * price
        self.numberofShares += number

    def sell(self, number, price):
        if  self.numberofShares > number:
            number = int(self.numberofShares / price)
        self.money += number * price * self.taxrate
        self.numberofShares -= number

    def shouldbuy(self, MACD, price):
        numbers = int(MACD * self.risk)
        if MACD < 0:
            self.buy(numbers, price)
        else:
            self.sell(numbers, price)

