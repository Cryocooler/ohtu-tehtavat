import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
#from viikko4.verkkokauppa.src.ostoskori import Ostoskori
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, 'pesto', 2)
            if tuote_id == 3:
                return Tuote(3, 'brooklyn lager', 8)


        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote




    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        #self.viitegeneraattori_mock.uusi.return_value = 42
         # tehdään toteutus saldo-metodille
        # def varasto_saldo(tuote_id):
        #     if tuote_id == 1:
        #         return 10

        # # tehdään toteutus hae_tuote-metodille
        # def varasto_hae_tuote(tuote_id):
        #     if tuote_id == 1:
        #         return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        # self.varasto_mock.saldo.side_effect = varasto_saldo
        # self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    def test_ostokset_ppankin_tilisiirto_oikeilla_argumenteilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", self.kauppa._kaupan_tili,5 )
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteist
    def test_ostokset_useampi_tuote_tilisiirto_kunnossa(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 7)


    def test_ostokset_sama_tuote_tilisiirto_kunnossa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345")
        #print(kauppa.varasto.)

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 10)

    def test_ostokset_tuote_jolla_ei_saldoa_ei_lisata_ostoskoriin_ja_tilisiirron_summaan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka","12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 5)


    def test_aiemmat_ostoskorit_eivat_sisally_uusiin_ostoskoreihin(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("janne","123456")
        self.pankki_mock.tilisiirto.assert_called_with("janne", 42, "123456", self.kauppa._kaupan_tili, 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("janne","123456")
        self.pankki_mock.tilisiirto.assert_called_with("janne", 42, "123456", self.kauppa._kaupan_tili, 2)

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kaksi kertaa
    def test_pyydetaan_uusi_viite_jokaiseen_maksuun(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("janne","123456")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)


        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("janne","123456")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_korista_poistettu_tuote_ei_sisally_tilisiirron_summaan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("jokke","123456")

        self.pankki_mock.tilisiirto.assert_called_with("jokke", 42, "123456", self.kauppa._kaupan_tili, 0)
