class Person:
    def __init__(self, money, risk, taxrate):
        self.money = money
        self.risk = risk
        self.taxrate = taxrate
        self.numberofShares = 0
        self.moneytable = []

    def buy(self, number, price):
        if self.money < number * price:
            number = int(self.money / price)
        self.money -= number * price
        self.numberofShares += number

    def sell(self, number, price):
        if(self.numberofShares == 0): return
        if  self.numberofShares > number:
            number = int(self.numberofShares / price)
        self.money += number * price * self.taxrate
        self.numberofShares -= number


    def shouldbuy(self, MACD, price):
        numbers = int(abs(MACD * self.risk))
        if MACD < -0.1:
            self.buy(numbers, price)
        elif MACD > 0.1:
            self.sell(numbers, price)
        self.moneytable.append(self.money)
        return

