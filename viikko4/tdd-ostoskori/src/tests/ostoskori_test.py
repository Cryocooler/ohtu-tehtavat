import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self._maito = Tuote("Maito", 3)
        self._apa = Tuote("APA", 5)
    #step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    #step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    #step3
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    #step4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self._apa)
        self.kori.lisaa_tuote(self._maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    #step5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self._maito)
        self.kori.lisaa_tuote(self._apa)

        self.assertEqual(self.kori.hinta(), 8)

    #step6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self._maito)
        self.kori.lisaa_tuote(self._maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    #step 7
    def test_kahden_saman_tuotteen_lisayksen_jalkeen_hinta_on_saman_tuotteen_hinta_kertaa_kaksi(self):
        self.kori.lisaa_tuote(self._maito)
        self.kori.lisaa_tuote(self._maito)


        self.assertEqual(self.kori.hinta(), 6)

    #step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        # testaa että metodin palauttaman listan pituus 1

    #step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.

    #step10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self._apa)
        self.kori.lisaa_tuote(self._maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)