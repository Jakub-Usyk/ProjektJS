from tkinter import *
from tkinter import ttk
from Parkomat import *


def updateDepartureTime():
    '''Funkcja wylicza oraz aktualizuje date oraz godzine wyjazdu'''

    parkomat.calcDepartureDate()

    departureDate.config(
        text=parkomat.departure.strftime("%D") + "\n (" + parkomat.weekDays[parkomat.departure.strftime("%w")] + ")")
    departureTime.config(text=parkomat.departure.strftime("%H:%M"))


def updateDate(win):
    """Funkcja aktualizuje wyswietlana date"""
    currentDate.config(
        text=parkomat.today.strftime("%D") + "\n(" + parkomat.weekDays[parkomat.today.strftime("%w")] + ")")
    departureDate.config(
        text=parkomat.departure.strftime("%D") + "\n (" + parkomat.weekDays[parkomat.departure.strftime("%w")] + ")")
    departureTime.config(text=parkomat.departure.strftime("%H:%M"))
    win.destroy()


def updateTime(win):
    """Funkcja aktualizuje wyswietlany czas"""
    currentTime.config(text=parkomat.today.strftime("%H:%M"))
    departureDate.config(
        text=parkomat.departure.strftime("%D") + "\n (" + parkomat.weekDays[parkomat.departure.strftime("%w")] + ")")
    departureTime.config(text=parkomat.departure.strftime("%H:%M"))
    win.destroy()


def updateCoinAmount(win):
    """Funkcja aktualizuje wyswietlana ilosc wrzucanych monet"""
    coinAmount.config(text=parkomat.coinAmount)
    win.destroy()


def updatePlateNum(win):
    """Funkcja aktualizuje wyswietlany nr. rejestracyjny pojazdu"""
    plateNum.config(text=parkomat.plateNum)
    win.destroy()


def closeMainWindow():
    """Funkcja zamyka glowne okno, przy czym konczy prace programu"""
    mainframe.quit()


def confirm(p):
    """Funkcja wyswietlajaca potwierdzenie, podaje nr. rejestracyjny pojazdu,
    date i godzine zakupu, oraz date i godzine odjazu, funkcja rzuca wyjatki noCoinsAdded oraz blankPlateNum,
    odpowiednio jesli nie zostaly wrzucone zadne monety lub nie zostal dodany numer rejestracyjny"""

    if p.valCalc() == 0:
        raise noCoinsAdded()

    if p.plateNum == "(Brak)":
        raise blankPlateNum()

    confirmWindow = Tk()
    confirmWindow.geometry("484x226")
    confirmWindow.resizable(0, 0)
    confirmWindowFrame = ttk.Frame(confirmWindow)
    confirmWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(confirmWindowFrame, width=20).grid(column=0, row=0)  # przerwa
    ttk.Label(confirmWindowFrame, width=20, text="     POTWIERDZENIE", font="0", foreground="green").grid(column=1,
                                                                                                          row=0,
                                                                                                          ipady=10)
    ttk.Button(confirmWindowFrame, width=20, text="Nr. rejestracyjny").grid(column=0, row=2, ipady=0)
    ttk.Button(confirmWindowFrame, width=20, text=p.plateNum).grid(column=0, row=3, ipady=10)
    ttk.Button(confirmWindowFrame, width=20, text="Data zakupu").grid(column=1, row=2, ipady=0)
    ttk.Button(confirmWindowFrame, width=20, text=p.today.strftime("%D")).grid(column=1, row=3, ipady=10)
    ttk.Button(confirmWindowFrame, width=20, text="Czas zakupu").grid(column=2, row=2, ipady=0)
    ttk.Button(confirmWindowFrame, width=20, text=p.today.strftime("%H:%M")).grid(column=2, row=3, ipady=10)
    ttk.Label(confirmWindowFrame, width=20).grid(column=0, row=4, ipady=10)  # przerwa
    ttk.Button(confirmWindowFrame, width=20, text="Data wyjazdu").grid(column=0, row=5, ipady=0)
    ttk.Button(confirmWindowFrame, width=20, text=p.departure.strftime("%D")).grid(column=0, row=6, ipady=10)
    ttk.Button(confirmWindowFrame, width=20, text="Czas wyjazdu").grid(column=1, row=5, ipady=0)
    ttk.Button(confirmWindowFrame, width=20, text=p.departure.strftime("%H:%M")).grid(column=1, row=6, ipady=10)
    ttk.Button(confirmWindowFrame, width=20, text="ZAKOŃCZ", command=lambda: closeMainWindow()).grid(column=2, row=6,
                                                                                                     ipady=10)


def changeDate():
    """Funkcja zmienia aktualna date"""
    dateWindow = Tk()
    dateWindow.geometry("120x180")
    dateWindow.resizable(0, 0)
    dateWindowFrame = ttk.Frame(dateWindow)
    dateWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(dateWindowFrame, width=20, text="Wprowadź nową datę \n          DD/MM/YY").grid(column=0, row=0, ipady=10)
    newDate = Entry(dateWindowFrame, width=10)
    newDate.grid(column=0, row=1, ipady=0)
    ttk.Label(dateWindowFrame, width=20).grid(column=0, row=2)  # przerwa
    ttk.Button(dateWindowFrame, width=10, text="Wprowadź", command=lambda: parkomat.changeDate(newDate.get())).grid(
        column=0, row=3, ipady=5)
    ttk.Button(dateWindowFrame, width=10, text="Zatwierdź", command=lambda: updateDate(dateWindow)).grid(column=0,
                                                                                                         row=4, ipady=5)


def changeTime():
    """Funkcja zmienia aktualny czas"""
    timeWindow = Tk()
    timeWindow.geometry("120x180")
    timeWindow.resizable(0, 0)
    timeWindowFrame = ttk.Frame(timeWindow)
    timeWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(timeWindowFrame, width=20, text="Wprowadź nowy czas \n             HH:MM").grid(column=0, row=0, ipady=10)
    newTime = Entry(timeWindowFrame, width=10)
    newTime.grid(column=0, row=1, ipady=0)
    ttk.Label(timeWindowFrame, width=20).grid(column=0, row=2)  # przerwa
    ttk.Button(timeWindowFrame, width=10, text="Wprowadź", command=lambda: parkomat.changeTime(newTime.get())).grid(
        column=0, row=3, ipady=5)
    ttk.Button(timeWindowFrame, width=10, text="Zatwierdź", command=lambda: updateTime(timeWindow)).grid(column=0,
                                                                                                         row=4, ipady=5)


def changeCoinAmount():
    """Funkcja zmienia ilosc wrzucanych monet"""
    coinWindow = Tk()
    coinWindow.geometry("120x180")
    coinWindow.resizable(0, 0)
    coinWindowFrame = ttk.Frame(coinWindow)
    coinWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(coinWindowFrame, width=20, text="    Wprowadź nową\n       liczbę monet").grid(column=0, row=0, ipady=10)
    newCoinAmount = Entry(coinWindowFrame, width=10)
    newCoinAmount.grid(column=0, row=1, ipady=0)
    ttk.Label(coinWindowFrame, width=20).grid(column=0, row=2)  # przerwa
    ttk.Button(coinWindowFrame, width=10, text="Wprowadź",
               command=lambda: parkomat.changeCoinAmount(newCoinAmount.get())).grid(column=0, row=3, ipady=5)
    ttk.Button(coinWindowFrame, width=10, text="Zatwierdź", command=lambda: updateCoinAmount(coinWindow)).grid(column=0,
                                                                                                               row=4,
                                                                                                               ipady=5)


def changePlateNum():
    """Funkcja zmienia nr. rejestracyjny pojazdu"""
    plateNumWindow = Tk()
    plateNumWindow.geometry("120x180")
    plateNumWindow.resizable(0, 0)
    plateNumWindowFrame = ttk.Frame(plateNumWindow)
    plateNumWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(plateNumWindowFrame, width=20,
              text="    Wprowadź nowy\n  numer rejestracyjny\n         (bez przerw)").grid(column=0, row=0, ipady=10)
    newPlateNum = Entry(plateNumWindowFrame, width=10)
    newPlateNum.grid(column=0, row=1, ipady=0)
    ttk.Label(plateNumWindowFrame, width=20).grid(column=0, row=2)  # przerwa
    ttk.Button(plateNumWindowFrame, width=10, text="Wprowadź",
               command=lambda: parkomat.ChangePlateNum(newPlateNum.get())).grid(column=0, row=3, ipady=5)
    ttk.Button(plateNumWindowFrame, width=10, text="Zatwierdź", command=lambda: updatePlateNum(plateNumWindow)).grid(
        column=0,
        row=4,
        ipady=5)


def addCoin(coin):
    """Funkcja dodaje monete do parkomatu oraz aktualizuje date oraz godzine wyjazdu"""
    parkomat.addCoin(coin)
    updateDepartureTime()


def addBill(Banknot):
    """Funkcja dodaje banknot do parkomatu oraz aktualizuje date oraz godzine wyjazdu"""
    parkomat.addBill(Banknot)
    updateDepartureTime()


# TWORZENIE INTERFEJSU:  -----------------------------------------------------------------------------------------------

# Tworzenie obiektu klasy Parkomat
parkomat = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])

# Tworzenie okna
window = Tk()
window.geometry("780x447")
window.resizable(0, 0)
window.title("Parkomat")

# Tworzenie siatki na przyciski
mainframe = ttk.Frame(window)

# Umieszczenie siatki w oknie
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Numer rejestracyjny
ttk.Button(mainframe, width=20, text="Nr. rejestracyjny").grid(column=0, row=0, ipady=0)
plateNum = ttk.Button(mainframe, width=20, text=parkomat.plateNum)
plateNum.grid(column=0, row=1, ipady=17)
ttk.Button(mainframe, width=20, text="(Kliknij aby zmienić)", command=lambda: changePlateNum()).grid(column=0, row=2,
                                                                                                     ipady=0)
ttk.Label(mainframe, width=20).grid(column=1, row=4)  # przerwa

# DATA: ----------------------------------------------------------------------------------------------------------------

# Aktualna
ttk.Button(mainframe, width=20, text="Aktualna data").grid(column=1, row=0, ipady=0)
currentDate = ttk.Button(mainframe, width=20, text=parkomat.today.strftime("%D") + "\n(" + parkomat.weekDays[
    parkomat.today.strftime("%w")] + ")")
currentDate.grid(column=1, row=1, ipady=10)
ttk.Button(mainframe, width=20, text="(Kliknij aby zmienić)", command=lambda: changeDate()).grid(column=1, row=2,
                                                                                                 ipady=0)

# Wyjazdu
ttk.Button(mainframe, width=20, text="Data wyjazdu").grid(column=4, row=0, ipady=0)
departureDate = ttk.Button(mainframe, width=20, text=parkomat.departure.strftime("%D") + "\n (" + parkomat.weekDays[
    parkomat.departure.strftime("%w")] + ")")
departureDate.grid(column=4, row=1, ipady=10)

# GODZINA: -------------------------------------------------------------------------------------------------------------

# Aktualna
ttk.Button(mainframe, width=20, text="Aktualna godzina").grid(column=2, row=0, ipady=0)
currentTime = ttk.Button(mainframe, width=20, text=parkomat.today.strftime("%H:%M"))
currentTime.grid(column=2, row=1, ipady=17)
ttk.Button(mainframe, width=20, text="(Kliknij aby zmienić)", command=lambda: changeTime()).grid(column=2, row=2,
                                                                                                 ipady=0)

# Wyjazdu
ttk.Button(mainframe, width=20, text="Godzina wyjazdu").grid(column=5, row=0, ipady=0)
departureTime = ttk.Button(mainframe, width=20, text=parkomat.departure.strftime("%H:%M"))
departureTime.grid(column=5, row=1, ipady=17)

# Dodanie przycisków do wrzucania monet --------------------------------------------------------------------------------
ttk.Label(mainframe, width=20).grid(column=0, row=3, ipady=10)  # przerwa
ttk.Label(mainframe, width=20).grid(column=0, row=4, ipady=10)  # przerwa
ttk.Button(mainframe, width=20, text="Wrzucane monety").grid(column=0, row=5, ipady=0)
coinAmount = ttk.Button(mainframe, width=20, text=parkomat.coinAmount)
coinAmount.grid(column=0, row=6, ipady=15)
ttk.Button(mainframe, width=20, text="(Kliknij aby zmienić)", command=lambda: changeCoinAmount()).grid(column=0, row=7,
                                                                                                       ipady=0)

for i, value in enumerate([0.01, 0.02, 0.05, 0.10, 0.20, 0.5, 1, 2, 5, 10, 20, 50]):
    if value <= 5:
        ttk.Button(mainframe, width=20, text="Wrzuć %0.2f zł" % (value), command=lambda value=value:
        addCoin(Moneta(value, "PLN"))).grid(column=i % 6, row=8 + i // 6)
    else:
        ttk.Button(mainframe, width=20, text="Wrzuć %0.2f zł" % (value), command=lambda value=value:
        addBill(Banknot(value, "PLN"))).grid(column=i % 6, row=8 + i // 6)

# Dodanie przycisku do zatwierdzenia -----------------------------------------------------------------------------------
ttk.Label(mainframe, width=20).grid(column=0, row=10, ipady=10)  # przerwa
ttk.Label(mainframe, width=20).grid(column=0, row=11, ipady=10)  # przerwa
ttk.Button(mainframe, width=20, text="Zatwierdź", command=lambda: confirm(parkomat)).grid(column=5, row=11, ipady=20)

# Zapętlenie okna
window.mainloop()