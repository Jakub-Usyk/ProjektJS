from Moneta import *

class Banknot(Moneta):
    """Klasa dziedziczaca po klasie Moneta, jedyna jej roznica sa inne przyjmowane wartosci"""
    _validVal = [10, 20, 50]

    def __init__(self, value, currency):
        """Konstruktor klasy Banknot"""
        super().__init__(value, currency)