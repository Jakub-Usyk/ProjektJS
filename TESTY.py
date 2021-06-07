from datetime import timedelta
from tkinter import ttk

from Moneta import Moneta
from Parkomat import Parkomat



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
    #ttk.Button(confirmWindowFrame, width=20, text="ZAKOŃCZ", command=lambda: closeMainWindow()).grid(column=2, row=6,
    #                                                                                                 ipady=10)


#Test nr. 1:

print("\n==============================Test nr. 1:============================== \n")
parkomatTest1 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
try:
    parkomatTest1.changeTime("25:11")
except:
    print("Blad 1")

parkomatTest1.changeTime("12:34")



#Test nr. 2:
print("\n==============================Test nr. 2:============================== \n")
parkomatTest2 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest2.changeTime("08:00")
print("Aktualny czas:", parkomatTest2.today.strftime("%H:%M"))
parkomatTest2.addCoin(Moneta(2, "PLN"))
parkomatTest2.calcDepartureDate()
print("Czas wyjazdu po wrzuceniu 2zl:", parkomatTest2.departure.strftime("%H:%M"))
parkomatTest2.addCoin(Moneta(2, "PLN"))
parkomatTest2.addCoin(Moneta(2, "PLN"))
parkomatTest2.calcDepartureDate()
print("Czas wyjazdu po wrzuceniu 4zl:", parkomatTest2.departure.strftime("%H:%M"))
parkomatTest2.addCoin(Moneta(5, "PLN"))
parkomatTest2.calcDepartureDate()
print("Czas wyjazdu po wrzuceniu 5zl:", parkomatTest2.departure.strftime("%H:%M"))


#Test nr. 3:
print("\n==============================Test nr. 3:============================== \n")
parkomatTest3 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest3.changeTime("08:00")
while parkomatTest3.departure.hour < 19:
    parkomatTest3.addCoin(Moneta(2, "PLN"))
    parkomatTest3.calcDepartureDate()

print("Aktualny czas:", parkomatTest3.departure.strftime("%H:%M"))
parkomatTest3.addCoin(Moneta(5, "PLN"))
parkomatTest3.calcDepartureDate()
print("Czas po wrzuceniu 5zl:", parkomatTest3.departure.strftime("%H:%M"))


#Test nr. 4:
print("\n==============================Test nr. 4:============================== \n")
parkomatTest4 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest4.changeTime("08:00")

while parkomatTest4.departure.hour < 19:
    parkomatTest4.addCoin(Moneta(2, "PLN"))
    parkomatTest4.calcDepartureDate()

while parkomatTest4.departure.strftime("%w") != "5":
    parkomatTest4.departureDelta += timedelta(days=1)
    parkomatTest4.calcDepartureDate()

print("Aktualny dzien", parkomatTest4.departure)
print("Aktualny dzien tygodnia:", parkomatTest4.weekDays[parkomatTest4.departure.strftime("%w")])
print("Aktualna godzina:", parkomatTest4.departure.strftime("%H:%M"))
parkomatTest4.addCoin(Moneta(5, "PLN"))
parkomatTest4.calcDepartureDate()
print("Dzien po dodaniu 5zl", parkomatTest4.departure)
print("Dzien tygodnia po dodaniu 5zl:", parkomatTest4.weekDays[parkomatTest4.departure.strftime("%w")])
print("Godzina po dodaniu 5zl:", parkomatTest4.departure.strftime("%H:%M"))

#Test nr. 5:
print("\n==============================Test nr. 5:============================== \n")
parkomatTest5 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest5.changeTime("08:00")
print("Aktualny czas", parkomatTest5.departure.strftime("%H:%M"))
parkomatTest5.addCoin(Moneta(2, "PLN"))
parkomatTest5.calcDepartureDate()
print("Czas po dodaniu 2zl", parkomatTest5.departure.strftime("%H:%M"))

#Test nr. 6:
print("\n==============================Test nr. 6:============================== \n")
parkomatTest6 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest6.changeTime("08:00")
print("Aktualny czas", parkomatTest6.departure.strftime("%H:%M"))
for i in range(200):
    parkomatTest6.addCoin(Moneta(0.01, "PLN"))
    parkomatTest6.calcDepartureDate()
print("Czas po dodaniu 200 * 0.01gr:", parkomatTest6.departure.strftime("%H:%M"))

#Test nr. 7
print("\n==============================Test nr. 7:============================== \n")
parkomatTest7 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest7.changeTime("08:00")
for i in range(201):
        parkomatTest7.addCoin(Moneta(0.01, "PLN"))
        parkomatTest7.calcDepartureDate()

#Test nr. 8   (funkcja confirm skopiowana z powodu otwierania glownego okna przy imporcie maina)
print("\n==============================Test nr. 8:============================== \n")
parkomatTest8 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest8.addCoin(Moneta(2,"PLN"))
try:
    confirm(parkomatTest8)
except:
    print("Blad 8")

#Test nr. 9   (funkcja confirm skopiowana z powodu otwierania glownego okna przy imporcie maina)
print("\n==============================Test nr. 8:============================== \n")
parkomatTest9 = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
parkomatTest9.ChangePlateNum("AB12345")
try:
    confirm(parkomatTest8)
except:
    print("Blad 9")











