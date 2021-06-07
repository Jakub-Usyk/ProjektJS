from Banknot import *
from Exceptions import *

class PrzechowywaczZlotych:
    """Klasa bedaca odwzorowaniem przechowywacza zlotych. Posiada ona metody pozwalajace na dodawanie
     monet lub banknotow, wyliczenie ile monet danej wartosci znajduje sie w nim,
     oraz na obliczenie wartosci wszystkich posiadanych monet oraz banknotow"""
    def __init__(self, values):
        """Konstruktor klasy, ustawia walute monet oraz banknotow na PLN, liste monet na pusta,
        oraz ustawia prawidlowe wartosci monet na wartosci podane w argumencie"""
        self._currency = "PLN"
        self._money = []
        self._validValues = values

    def addCoin(self, coin):
        """Metoda dodajaca monete podana w argumencie do przechowywacza zlotych. Jesli podany argument
        nie jest obiektem klasy Moneta, rzuca wyjatek notACoin. Jesli podana waluta oraz wartosc nie naleza
        do prawidlowych walut oraz wartosci metoda wyswietla komunikat o nieznanej monecie"""
        if isinstance(coin, Moneta):
            if coin.getCurrency() == self._currency and coin.getValue() in self._validValues:
                self._money.append(coin)
            else:
                print("Nieznana moneta")
        else:
            raise notACoin(coin)

    def addBill(self, bill):
        """Metoda dodajaca banknot podany w argumencie do przechowywacza zlotych. Jesli podany argument
        nie jest obiektem klasy Banknot, rzuca wyjatek notABill. Jesli podana waluta oraz wartosc nie naleza
        do prawidlowych walut oraz wartosci metoda wyswietla komunikat o nieznanym banknocie"""
        if isinstance(bill, Banknot):
            if bill.getCurrency() == self._currency and bill.getValue() in self._validValues:
                self._money.append(bill)
            else:
                print("Nieznany banknot")
        else:
            raise notABill(bill)

    def howManyCoins(self, coin):
        """Metoda wyliczajaca oraz zwracajaca ilosc monet danego typu w przechowywaczu zlotych"""
        counter = 0
        for money in self._money:
            if money.getValue() == coin.getValue():
                counter += 1
        return counter

    def valCalc(self):
        """Metoda wyliczajaca oraz zwracajaca sume pieniedzy w przechowywaczu zlotych"""
        suma = Decimal('0')
        for money in self._money:
            suma += money.getValue()
        return suma