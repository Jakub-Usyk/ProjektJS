from tkinter import *
from tkinter import ttk
from Parkomat import *

def changeDate():
    dateWindow = Tk()
    dateWindow.geometry("120x180")
    dateWindow.resizable(0, 0)
    dateWindowFrame = ttk.Frame(dateWindow)
    dateWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(dateWindowFrame, width=20, text="Wprowadź nową datę \n          DD/MM/YY").grid(column=0, row=0, ipady=10)
    newDate = Entry(dateWindowFrame, width=10)
    newDate.grid(column=0, row=1, ipady=0)
    ttk.Label(dateWindowFrame, width=20).grid(column=0, row=2)  # przerwa
    ttk.Button(dateWindowFrame, width=10, text="Wprowadź", command=lambda: parkomat.changeDate(newDate.get())).grid(column=0, row=3, ipady=5)
    ttk.Button(dateWindowFrame, width=10, text="Zatwierdź", command=lambda:
    currentDate.config(text=parkomat.today.strftime("%D"))).grid(column=0, row=4, ipady=5)

def changeTime():
    timeWindow = Tk()
    timeWindow.geometry("120x180")
    timeWindow.resizable(0, 0)
    timeWindowFrame = ttk.Frame(timeWindow)
    timeWindowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Label(timeWindowFrame, width=20, text="Wprowadź nowy czas \n             HH:MM").grid(column=0, row=0, ipady=10)
    newTime = Entry(timeWindowFrame, width=10)
    newTime.grid(column=0, row=1, ipady=0)
    ttk.Label(timeWindowFrame, width=20).grid(column=0, row=2)  # przerwa
    ttk.Button(timeWindowFrame, width=10, text="Wprowadź", command=lambda: parkomat.changeTime(newTime.get())).grid(column=0, row=3, ipady=5)
    ttk.Button(timeWindowFrame, width=10, text="Zatwierdź", command=lambda:
    currentTime.config(text=parkomat.today.strftime("%H:%M"))).grid(column=0, row=4, ipady=5)

# TWORZENIE TABELI
parkomat = Parkomat("KR12AB3", [0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])

# Tworzenie okna
window = Tk()
window.geometry("780x300")
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
ttk.Button(mainframe, width=20, text=parkomat.plateNum).grid(column=0, row=1, ipady=10)

# Data

    # Aktualna
ttk.Button(mainframe, width=20, text="Aktualna data").grid(column=1, row=0, ipady=0)
currentDate = ttk.Button(mainframe, width=20, text=parkomat.today.strftime("%D"))
currentDate.grid(column=1, row=1, ipady=10)

ttk.Button(mainframe, width=20, text="(Kliknij aby zmienić)", command=lambda: changeDate()).grid(column=1, row=2, ipady=0)

    # Wyjazdu
ttk.Button(mainframe, width=20, text="Data wyjazdu").grid(column=4, row=0, ipady=0)
departureDate = ttk.Button(mainframe, width=20, text=parkomat.departure.strftime("%D"))
departureDate.grid(column=4, row=1, ipady=10)

# Godzina

    #Aktualna
ttk.Button(mainframe, width=20, text="Aktualna godzina").grid(column=2, row=0, ipady=0)
currentTime = ttk.Button(mainframe, width=20, text=parkomat.today.strftime("%H:%M"))
currentTime.grid(column=2, row=1, ipady=10)
ttk.Button(mainframe, width=20, text="(Kliknij aby zmienić)", command=lambda: changeTime()).grid(column=2, row=2, ipady=0)

    # Wyjazdu
ttk.Button(mainframe, width=20, text="Godzina wyjazdu").grid(column=5, row=0, ipady=0)
departureTime = ttk.Button(mainframe, width=20, text=parkomat.departure.strftime("%H:%M"))
departureTime.grid(column=5, row=1, ipady=10)

# Dodanie przycisków do wrzucania monet
ttk.Label(mainframe, width=20).grid(column=0, row=6, ipady=10)  # przerwa
for i, value in enumerate([0.01, 0.02, 0.05, 0.10, 0.20, 0.5, 1, 2, 5, 10, 20, 50]):
    if value <= 5:
        ttk.Button(mainframe, width=20, text="Wrzuć %0.2f zł" % (value), command=lambda value=value:
        parkomat.addCoin(Moneta(value, "PLN"))).grid(column=i % 6, row=7 + i // 6)
    else:
        ttk.Button(mainframe, width=20, text="Wrzuć %0.2f zł" % (value), command=lambda value=value:
        parkomat.addBill(Banknot(value, "PLN"))).grid(column=i % 6, row=7 + i // 6)

# tutaj kod testowy \/  \/  \/  \/



# tutaj kod testowy /\  /\  /\  /\

# Zapętlenie okna
window.mainloop()


