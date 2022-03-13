from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):

        self._ostokset = []

        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):

        #maarat = reduce(lambda x,y: x + y.lukumaara(), self._ostokset)
        maarat = map(lambda x: x.lukumaara(), self._ostokset)
        return sum(maarat)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinnat = map(lambda x: x.hinta(), self._ostokset)
        return sum(hinnat)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen jos tuotetta ei löydy ostoksista
        if len(list(filter(lambda x: x.tuotteen_nimi() == lisattava.nimi(), self._ostokset))) == 0:
            self._ostokset.append(Ostos(lisattava))
        else:
            #etsi korista ostos-olio jossa tuotteen nimi ja kasvata määrää

            for ostos in self._ostokset:
                if ostos.tuotteen_nimi() == lisattava.nimi():
                   ostos.muuta_lukumaaraa(1)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
