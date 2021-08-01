class Banker :

    def __init__(self):
        self.balance=0
        self.shelved=0

    def bank(self):
        amount=self.shelved
        self.balance+=self.shelved
        self.shelved=0
        return amount

    def shelf(self,amount1):
        self.shelved+=amount1

    def clear_shelf(self):
        self.shelved=0