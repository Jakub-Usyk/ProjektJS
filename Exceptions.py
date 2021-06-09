class badPlateNum(Exception):
    """Wyjatek rzucany w przypadku wprowadzenia numeru rejestracyjnego ktorego jeden ze skladnikow nie nalezy do duzych liter lub do cyfr"""

    def __init__(self, val):
        self._val = val

    def __str__(self):
        return repr(self._val)


class notACoin(Exception):
    """Wyjatek rzucany w przypadku proby dodania do automatu obiektu nie bedacego moneta, korzystajac z metody addCoin"""

    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class notABill(Exception):
    """Wyjatek rzucany w przypadku proby dodania do automatu obiektu nie bedacego banknotem, korzystajac z metody addBill"""

    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class wrongDateFormat(Exception):
    """Wyjatek rzucany w przypadku wprowadzenia daty w zlym formacie"""

    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class wrongTimeFormat(Exception):
    """Wyjatek rzucany w przypadku wprowadzenia czasu w zlym formacie"""

    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class wrongCoinAmount(Exception):
    """Wyjatek rzucany w przypadku wprowadzenia liczby wrzucanych moneta na mniejsza niz 0"""

    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class noCoinsAdded(Exception):
    """Wyjatek rzucany w przypadku proby zatwierdzenia gdy nie wrzucono zadnych monet"""
    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class blankPlateNum(Exception):
    """Wyjatek rzucany w przypadku proby zatwierdzenia gdy nie wprowadzono zadnej rejestracji"""
    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)
