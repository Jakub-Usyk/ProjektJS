from datetime import datetime, timedelta
from PrzechowywaczZlotych import *
from Exceptions import *


class Parkomat(PrzechowywaczZlotych):
    """Najwazniejsza klasa w projekcie. Dziedziczy po klasie PrzechowywaczZlotych oraz tworzy obiekt parkomatu"""

    _validPlateNums = [chr(i) for i in range(ord('0'), ord('Z') + 1) if i < ord('9') + 1 or i > ord('A') - 1]

    def __init__(self, values):
        """Konstruktor klasy, wywoluje konstruktor klasy nadrzednej z podanym argumentem values,
        oraz ustawia odpowiednie poczatkowe wartosci dla ilosc wrzucanych monet,
        czasu parkowania, aktualnej daty i godziny, daty i godziny wyjazdu,
        oraz tworzy slownik przypisujacy liczby od 0 do 6 do odpowiednich dni tygodnia"""
        super().__init__(values)
        self.coinAmount = 1
        self._parkTime = 0
        self.today = datetime.today()
        self.weekDays = {"1": "Poniedzialek", "2": "Wtorek", "3": "Sroda", "4": "Czwartek", "5": "Piatek", "6": "Sobota", "0": "Niedziela"}
        self.plateNum = plateNum = "(Brak)"
        if self.today.hour >= 20 or self.today.hour <= 8:
            self.departure = datetime(self.today.year, self.today.month, self.today.day, 8)
        else:
            self.departure = datetime.today()

        if self.today.strftime("%w") == "0":
            self.departure += timedelta(days=1)
        elif self.today.strftime("%w") == "6":
            self.departure += timedelta(days=2)

        self.departureDelta = self.departure

    def ChangePlateNum(self, plateNum):
        """Metoda sprawdza czy podany numer jest prawidlowy. Jesli tak, ustawia podany numer rejestracyjny,
        w przeciwnym wypadku rzuca wyjatek badPlateNum"""
        for c in plateNum:
            if c not in self._validPlateNums:
                raise badPlateNum(c)
        else:
            self.plateNum = plateNum

    def addCoin(self, coin):
        """Metoda dodaje do parkomatu podana monete jesli jest ona moneta,
         oraz jesli limit monet danej wartosci nie zostal przekroczony. W przeciwnym wypadku odpowiednio
         rzuca wyjatek notACoin, lub wyswietla informacje o przepelnieniu parkomatu"""
        if isinstance(coin, Moneta):
            for i in range(self.coinAmount):
                if self.howManyCoins(coin) < 200:
                    print("wrzucam", coin.getValue())
                    self._money.append(coin)
                else:
                    print("Parkomat przepełniony, proszę o wrzucenie innego nominału")
        else:
            raise notACoin(coin)


    def changeDate(self, newDate):
        """Metoda sprawdza czy podana nowa data jest w odpowiednim formacie. Jesli tak,
        aktualizuje date wjazdu, oraz w odpowiedni sposob date wyjazdu,
        w przeciwnym wypadku rzuca wyjatek wrongDateFormat. Metoda rowniez po zmianie daty ustawia liste monet
        parkomatu na pusta"""
        for el in newDate:
            if not el.isnumeric() and el != "/":
                raise wrongDateFormat()
        dateList = newDate.split(sep="/")
        newDay = int(dateList[0])
        newMonth = int(dateList[1])
        newYear = int(dateList[2])
        if newDay < 1 or newDay > 31:
            raise wrongDateFormat(newDay)
        if newMonth < 1 or newMonth > 12:
            raise wrongDateFormat(newMonth)
        if newYear < 1 or newYear > 99:
            raise wrongDateFormat(newYear)
        oldHour = self.today.hour
        oldMinute = self.today.minute
        self.today = datetime(newYear, newMonth, newDay, oldHour, oldMinute)

        if self.today.hour >= 20 or self.today.hour <= 8:
            self.departure = datetime(self.today.year, self.today.month, self.today.day, 8)
        else:
            self.departure = self.today

        if self.today.strftime("%w") == "0":
            self.departure += timedelta(days=1)
        elif self.today.strftime("%w") == "6":
            self.departure += timedelta(days=2)

        self.departureDelta = self.departure
        self._money = []




    def changeTime(self, newTime):
        """Metoda sprawdza czy podana nowa godzina jest w odpowiednim formacie. Jesli tak,
                aktualizuje godzine wjazdu, oraz w odpowiedni sposob godzine wyjazdu,
                w przeciwnym wypadku rzuca wyjatek wrongTimeFormat. Metoda rowniez po zmianie godziny
                ustawia liste monet parkomatu na pusta"""
        for el in newTime:
            if not el.isnumeric() and el != ":":
                raise wrongTimeFormat()
        dateList = newTime.split(sep=":")
        newHour = int(dateList[0])
        newMinute = int(dateList[1])
        if newHour < 0 or newHour > 23:
            raise wrongTimeFormat(newHour)
        if newMinute < 0 or newMinute > 59:
            raise wrongTimeFormat(newMinute)
        oldYear = self.today.year
        oldMonth = self.today.month
        oldDay = self.today.day
        self.today = datetime(oldYear, oldMonth, oldDay, newHour, newMinute)

        if self.today.hour >= 20 or self.today.hour <= 8:
            self.departure = datetime(self.today.year, self.today.month, self.today.day, 8)
        else:
            self.departure = self.today

        if self.today.strftime("%w") == "0":
            self.departure += timedelta(days=1)
        elif self.today.strftime("%w") == "6":
            self.departure += timedelta(days=2)

        self.departureDelta = self.departure
        self._money = []


    def changeCoinAmount(self, param):
        """Metoda ustawia liczbe wrzucanych monet na podana przez argument param,
         jesli podany argument jest wiekszy od 0. W przeciwnym wypadku metoda rzuca wyjatek wrongCoinAmount"""
        param = int(param)
        if param > 0:
            self.coinAmount = param
        else:
            raise wrongCoinAmount(param)

    def calcDepartureDate(self):
        """Metoda wylicza z monet parkomatu w odpowiedni sposob date oraz godzine wyjazdu z parkingu,
         po czym aktualizuje wyswietlana date oraz godzine wyjazdu"""
        value = float(self.valCalc())
        if value < 2:
            self._parkTime = value * 0.5
        elif value < 6:
            self._parkTime = 2 * 0.5 + (value - 2) * 0.25
        else:
            self._parkTime = 2 * 0.5 + 4 * 0.25 + (value - 6) * 0.20



        if (self.departureDelta + timedelta(hours=self._parkTime)).hour >= 20 or (self.departureDelta + timedelta(hours=self._parkTime)).hour < 8:
            self.departureDelta += timedelta(hours=12)
            self.departure = self.departureDelta + timedelta(hours=self._parkTime)
        else:
            self.departure = self.departureDelta + timedelta(hours=self._parkTime)

        if self.departure.strftime("%w") == "0" or self.departure.strftime("%w") == "6":
            self.departureDelta += timedelta(days=2)
            self.departure = self.departureDelta + timedelta(hours=self._parkTime)