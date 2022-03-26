class Summa:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self._sovellus.plus(self._syote())


class Erotus:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self._sovellus.miinus(self._syote())

class Nollaus:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self._sovellus.nollaa(self._syote())

class Kumoa:
    def __init__(self,sovellus,syote):
        self._sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self._sovellus.kumoa(self._syote())