from Moneta import *

class Banknot(Moneta):
    _validVal = [10, 20, 50]

    def __init__(self, value, currency):
        super().__init__(value, currency)
