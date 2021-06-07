from decimal import *
class Moneta:
    """Klasa bedaca odwzorowaniem monety. Posiada liste prawidlowych wartosci oraz walut"""
    _validVal = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    _validCur = ["PLN", "EUR", "GP"]

    def __init__(self, value, currency):
        """Konstruktor klasy, sprawdza czy podana waluta nalezy do listy prawidlowych walut,
        jesli nie, ustawia walute na PLN, oraz sprawdza czy podana wartosc nalezy do listy prawidlowych wartosci,
        jestli nie, przypisuje 0"""
        if currency in self._validCur:
            self._currency = currency
        else:
            print("Nieznana waluta, przypisuje PLN")
            self._currency = "PLN"
        if value in self._validVal:
            self._value = Decimal(str(value))
        else:
            print("Nieznana wartosc, przypisuje 0")
            self._value = Decimal('0')

    def getCurrency(self):
        """Metoda zwraca walute monety"""
        return self._currency

    def getValue(self):
        """Metoda zwraca wartosc monety"""
        return self._value




