class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.current_money = 0
        self.money_receive = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.current_money}")

    def process_coin(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_receive += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_receive

    def transaction(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coin()
        change = round((self.money_receive - cost), 2)
        if self.money_receive > cost:
            self.current_money += cost
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.money_receive = 0
            return True
        elif self.money_receive == cost:
            self.current_money += cost
            self.money_receive = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.\n\n")
            self.money_receive = 0
            return False
