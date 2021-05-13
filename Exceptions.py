class badPlateNum(Exception):
    def __init__(self, val):
        self._val = val

    def __str__(self):
        return repr(self._val)


class notACoin(Exception):
    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class notABill(Exception):
    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)


class wrongDateFormat(Exception):
    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)

class wrongTimeFormat(Exception):
    def __init(self, obj):
        self._obj = obj

    def __str__(self):
        return repr(self._obj)