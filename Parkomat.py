from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import ttk

from decimal import *


class Moneta:
    _validVal = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    _validCur = ["PLN", "EUR", "GP"]

    def __init__(self, value, currency):
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
        return self._currency

    def getValue(self):
        return self._value


class Banknot(Moneta):
    _validVal = [10, 20, 50]

    def __init__(self, value, currency):
        super().__init__(value, currency)


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
            print("Przesłany obiekt nie jest monetą")

    def addBill(self, bill):
        if isinstance(bill, Banknot):
            if bill.getCurrency() == self._currency and bill.getValue() in self._validValues:
                self._money.append(bill)
            else:
                print("Nieznany banknot")
        else:
            print("Przesłany obiekt nie jest banknotem")

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


class badPlateNum(Exception):
    def __init__(self, val):
        self._val = val
    def __str__(self):
        return repr(self._val)

class Parkomat(PrzechowywaczZlotych):
    _validPlateNums = [chr(i) for i in range(ord('0'), ord('Z') + 1) if i < ord('9') + 1 or i > ord('A') - 1]

    def __init__(self, plateNum, values):
        super().__init__(values)
        self.today = datetime.now()
        self._parkTime = 0
        for c in plateNum:
            if c not in self._validPlateNums:
                raise badPlateNum(c)
        else:
            self.plateNum = plateNum

    def addCoin(self, coin):
        if isinstance(coin, Moneta):
            if parkomat.howManyCoins(coin) < 200:
                self._money.append(coin)
            else:
                print("Parkomat przepełniony, proszę o wrzucenie innego nominału")
        else:
            print("Przesłany obiekt nie jest monetą")

    def addDay(self):
        self.today = (self.today + timedelta(days=1))
        print(self.today)

    def subDay(self):
        self.today = (self.today - timedelta(days=1))
        print(self.today)

    def add5Mins(self):
        self.today = (self.today + timedelta(minutes=5))
        print(self.today)

    def sub5Mins(self):
        self.today = (self.today - timedelta(minutes=5))
        print(self.today)


# tutaj kod testowy \/  \/  \/  \/

#tab = [chr(i) for i in range(ord('0'), ord('Z') + 1) if i < ord('9') + 1 or i > ord('A') - 1]
#print(tab)

# tutaj kod testowy /\  /\  /\  /\
# TWORZENIE TABELI
parkomat = Parkomat("KR12AB3", [0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])

# Tworzenie okna
window = Tk()
window.geometry("780x780")
window.resizable(0, 0)
window.title("Parkomat")

# Tworzenie siatki na przyciski
mainframe = ttk.Frame(window)

# Umieszczenie siatki w oknie
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Numer rejestracyjny
ttk.Button(mainframe, width=20, text="Nr. rejestracyjny").grid(column=0, row=0, ipady=0)
ttk.Button(mainframe, width=20, text=parkomat.plateNum).grid(column=0, row=1, ipady=10)
ttk.Label(mainframe, width=20).grid(column=1, row=4)  # przerwa

# Data
ttk.Button(mainframe, width=20, text="Data").grid(column=2, row=0, ipady=0)
ttk.Button(mainframe, width=20, text=parkomat.today.strftime("%D")).grid(column=2, row=1, ipady=10)
ttk.Button(mainframe, width=20, text="Dodaj dzień", command=lambda: parkomat.addDay()).grid(column=2, row=2, ipady=0)
ttk.Button(mainframe, width=20, text="Odejmij dzień", command=lambda: parkomat.subDay()).grid(column=2, row=3, ipady=0)

# ttk.Label(mainframe, width=20, text="xxx").grid(column=1, row=1, ipady=10)
# ttk.Label(mainframe, width=20, text="xxx").grid(column=1, row=1, ipady=10)

# Godzina
ttk.Button(mainframe, width=20, text="Godzina").grid(column=3, row=0, ipady=0)
ttk.Button(mainframe, width=20, text=parkomat.today.strftime("%H:%M")).grid(column=3, row=1, ipady=10)
ttk.Button(mainframe, width=20, text="Dodaj 5 minut", command=lambda: parkomat.add5Mins()).grid(column=3, row=2,
                                                                                                ipady=0)
ttk.Button(mainframe, width=20, text="Odejmij 5 minut", command=lambda: parkomat.sub5Mins()).grid(column=3, row=3,
                                                                                                  ipady=0)

# Dodanie przycisków do wrzucania monet
ttk.Label(mainframe, width=20).grid(column=0, row=4, ipady=10)  # przerwa
for i, value in enumerate([0.01, 0.02, 0.05, 0.10, 0.20, 0.5, 1, 2, 5, 10, 20, 50]):
    if value <= 5:
        ttk.Button(mainframe, width=20, text="Wrzuć %0.2f zł" % (value), command=lambda value=value:
        parkomat.addCoin(Moneta(value, "PLN"))).grid(column=i % 6, row=6 + i // 6)
    else:
        ttk.Button(mainframe, width=20, text="Wrzuć %0.2f zł" % (value), command=lambda value=value:
        parkomat.addBill(Banknot(value, "PLN"))).grid(column=i % 6, row=6 + i // 6)

# Dodanie przycisku sprawdzenia wartości zawartości
window.mainloop()
