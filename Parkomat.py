from datetime import datetime
from PrzechowywaczZlotych import *
from Exceptions import *


class Parkomat(PrzechowywaczZlotych):
    _validPlateNums = [chr(i) for i in range(ord('0'), ord('Z') + 1) if i < ord('9') + 1 or i > ord('A') - 1]

    def __init__(self, plateNum, values):
        super().__init__(values)
        self.today = datetime.now()
        self.departure = datetime.now()
        self._parkTime = 0
        for c in plateNum:
            if c not in self._validPlateNums:
                raise badPlateNum(c)
        else:
            self.plateNum = plateNum

    def addCoin(self, coin):
        if isinstance(coin, Moneta):
            if self.howManyCoins(coin) < 5:
                self._money.append(coin)
            else:
                print("Parkomat przepełniony, proszę o wrzucenie innego nominału")
        else:
            raise notACoin(coin)

    def changeDate(self, newDate):
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

    def changeTime(self, newTime):
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