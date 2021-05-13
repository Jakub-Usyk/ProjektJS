from Banknot import *
from Exceptions import *

class PrzechowywaczZlotych:
    def __init__(self, values):
        self._currency = "PLN"
        self._money = []
        self._validValues = values

    def addCoin(self, coin):
        if isinstance(coin, Moneta):
            if coin.getCurrency() == self._currency and coin.getValue() in self._validValues:
                self._money.append(coin)
            else:
                print("Nieznana moneta")
        else:
            raise notACoin(coin)

    def addBill(self, bill):
        if isinstance(bill, Banknot):
            if bill.getCurrency() == self._currency and bill.getValue() in self._validValues:
                self._money.append(bill)
            else:
                print("Nieznany banknot")
        else:
            raise notABill(bill)

    def howManyCoins(self, coin):
        counter = 0
        for money in self._money:
            if money.getValue() == coin.getValue():
                counter += 1
        return counter

    def valCalc(self):
        suma = Decimal('0')
        for money in self._money:
            suma += money.getValue()
        return suma

