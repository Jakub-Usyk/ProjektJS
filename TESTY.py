import unittest
from datetime import timedelta

from Moneta import Moneta
from Parkomat import Parkomat
from main import confirm

''' UWAGA, po uruchomieniu testow nalezy zamknac wyskakujace okno. Powstaje ono przy uruchomieniu testow 8 oraz 9,
    lecz nie ma wplywu na wynik testow'''

class Tests(unittest.TestCase):
    def test_shouldReturnError_whenWrongTime(self):
        """1. Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie.
        Ustawić godzinę na 12:34."""

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])

        # bledna data
        wrongDateErrorOccured = False
        try:
            parkomatTest.changeTime("25:11")
        except:
            wrongDateErrorOccured = True
        self.assertTrue(wrongDateErrorOccured)

        # prawidlowa data
        rightDateErrorOccured = False
        try:
            parkomatTest.changeTime("12:34")
        except:
            rightDateErrorOccured = True

        # sprawdzam czy wystapil blad
        self.assertFalse(rightDateErrorOccured)

    def test_shouldCalculateDeparture_whenGivenMoney(self):
        """2. Wrzucić 2zl, oczekiwany termin wyjazdu godzinę po aktualnym czasie.
        Dorzuć 4zl, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie.
        Dorzuć 5zł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie.
        Dorzuć kolejne 5zł, oczekiwany termin wyjazdu cztery godziny po aktualnym czasie"""

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # zmieniam aktualna godzine parkomatu
        parkomatTest.changeTime("08:00")

        # po wrzuceniu 2zl
        parkomatTest.addCoin(Moneta(2, "PLN"))
        parkomatTest.calcDepartureDate()
        # sprawdzam czy data czas wyjazdu jest 1 godziny po aktualnym czasie
        self.assertEqual(parkomatTest.departure, parkomatTest.today + timedelta(hours=1))

        # po dorzuceniu 4zl
        parkomatTest.addCoin(Moneta(2, "PLN"))
        parkomatTest.addCoin(Moneta(2, "PLN"))
        parkomatTest.calcDepartureDate()
        # sprawdzam czy data czas wyjazdu jest 2 godziny po aktualnym czasie
        self.assertEqual(parkomatTest.departure, parkomatTest.today + timedelta(hours=2))

        # po dorzuceniu 5zl
        parkomatTest.addCoin(Moneta(5, "PLN"))
        parkomatTest.calcDepartureDate()
        # sprawdzam czy data czas wyjazdu jest 3 godziny po aktualnym czasie
        self.assertEqual(parkomatTest.departure, parkomatTest.today + timedelta(hours=3))

        # po dorzuceniu kolejnych 5zl
        parkomatTest.addCoin(Moneta(5, "PLN"))
        parkomatTest.calcDepartureDate()
        # sprawdzam czy data czas wyjazdu jest 4 godziny po aktualnym czasie
        self.assertEqual(parkomatTest.departure, parkomatTest.today + timedelta(hours=4))

    def test_shouldUpdateDay_whenTimeOutOfRange(self):
        """3. Wrzucić tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny dzień,
        zgodnie z zasadami - wrzucić tyle monet aby termin wyjazdu był po godzinie 19:00,
        dorzucić monetę 5zł, """

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # zmieniam aktualna godzine parkomatu
        parkomatTest.changeTime("08:00")

        # dodaje 2zl dopoki godzina wyjazdu jest mniejsza niz 19
        while parkomatTest.departure.hour < 19:
            parkomatTest.addCoin(Moneta(2, "PLN"))
            parkomatTest.calcDepartureDate()

        # dodaje dodatkowe 5zl
        parkomatTest.addCoin(Moneta(5, "PLN"))
        parkomatTest.calcDepartureDate()

        # sprawdzam czy dzien daty wyjazdu jest zwiekszony o 1
        self.assertEqual(parkomatTest.departure.day, parkomatTest.today.day + 1)

    def test_shouldUpdateWeek_whenDayOutOfRange(self):
        """4. Wrzucić tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny tydzień,
        zgodnie z zasadami - wrzucić tyle monet aby termin wyjazdu był w piątek po godzinie 19:00,
        a potem dorzucić monetę 5zł"""

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # zmieniam aktualna godzine parkomatu
        parkomatTest.changeTime("08:00")

        # dodaje 2zl dopoki godzina wyjazdu jest mniejsza niz 19
        while parkomatTest.departure.hour < 19:
            parkomatTest.addCoin(Moneta(2, "PLN"))
            parkomatTest.calcDepartureDate()

        # dodaje dzien, dopoki dzien tygodnia nie jest piatkiem
        while parkomatTest.departure.strftime("%w") != "5":
            parkomatTest.departureDelta += timedelta(days=1)
            parkomatTest.calcDepartureDate()

        # dodaje dodatkowe 5zl
        parkomatTest.addCoin(Moneta(5, "PLN"))
        parkomatTest.calcDepartureDate()

        # sprawdzam czy czas wyjazdu jest w poniedzialek
        self.assertEqual(parkomatTest.departure.strftime("%w"), "1")

    def test_shouldAddHalfHour_whenAddedValueForHalfHour(self):
        """5. Wrzucić 1zł, oczekiwany termin wyjazdu pół godziny po aktualnym czasie"""

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # zmieniam aktualna godzine parkomatu
        parkomatTest.changeTime("08:00")

        # dodaje 1zl
        parkomatTest.addCoin(Moneta(1, "PLN"))
        parkomatTest.calcDepartureDate()

        # sprawdzam czy czas wyjazdu jest zwiekszony o pol godziny
        self.assertEqual(parkomatTest.departure, parkomatTest.today + timedelta(hours=0.5))

    def test_shouldAddHourToDeparture_whenAddedEquivalentInPennies(self):
        """6. Wrzucić 200 monet 1gr, oczekiwany termin wyjazdu godzinę po aktualnym czasie. """

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # zmieniam aktualna godzine parkomatu
        parkomatTest.changeTime("08:00")

        # dodaje 200 monet 1gr
        for i in range(200):
            parkomatTest.addCoin(Moneta(0.01, "PLN"))
            parkomatTest.calcDepartureDate()

        # sprawdzam czy czas wyjazdu jest zwiekszony o godzine
        self.assertEqual(parkomatTest.departure, parkomatTest.today + timedelta(hours=1))

    def test_shouldReturnError_whenCoinAmountOutOfRange(self):
        """7. Wrzucić 201 monet 1gr, oczekiwana informacja o przepełnieniu parkomatu"""

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # zmieniam aktualna godzine parkomatu
        parkomatTest.changeTime("08:00")

        CoinOutOfRangeMessage = ""
        # dodaje 200 monet 1gr
        for i in range(201):
            CoinOutOfRangeMessage = parkomatTest.addCoin(Moneta(0.01, "PLN"))
            parkomatTest.calcDepartureDate()

        # sprawdzam czy czas wyjazdu jest zwiekszony o godzine
        self.assertEqual(CoinOutOfRangeMessage, "error")

    def test_shouldReturnError_whenConfirmingWithNoCoinsAdded(self):
        """8. Wciśnięcie "Zatwierdź" bez wrzucenia monet -- oczekiwana informacja o błędzie."""

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # ustawiam rejestracje
        parkomatTest.ChangePlateNum("AB12345")

        # czy wystapil blad
        noCoinsAddedError = False
        try:
            confirm(parkomatTest)
        except:
            noCoinsAddedError = True

        # sprawdzam czy wystapil blad
        self.assertTrue(noCoinsAddedError)

    def test_shouldReturnError_whenConfirmingWithNoPlateNumAdded(self):
        """9. Wciśnięcie "Zatwierdź" bez wpisania numeru rejestracyjnego -
        oczekiwana informacja o błędzie. Wciśnięcie "Zatwierdź" po wpisaniu
        niepoprawnego numeru rejestracyjnego — oczekiwana informacja o błędzie. """

        parkomatTest = Parkomat([0.01, 0.02, 0.05, 0.20, 0.5, 1, 2, 5, 10, 20, 50])
        # dodaje 2 zl
        parkomatTest.addCoin(Moneta(2, "PLN"))

        # czy wystapil blad
        noPlateNumAddedError = False
        try:
            confirm(parkomatTest)
        except:
            noPlateNumAddedError = True

        # sprawdzam czy wystapil blad
        self.assertTrue(noPlateNumAddedError)















