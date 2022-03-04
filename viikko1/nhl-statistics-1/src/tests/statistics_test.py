import unittest
from statistics import Statistics

from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class testStatistics(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    

    def test_haku_palauttaa_haetun_pelaajan(self):
        self.assertEqual(self.statistics.search("Kurri").name,"Kurri")


    def test_haettu_pelaaja_ei_listassa(self):
        self.assertAlmostEqual(self.statistics.search("Gamma"), None)
    
    
    def test_tiimin_haku(self):
        team = self.statistics.team("EDM")
        self.assertEqual(self.statistics.team("EDM"), team)


    def test_top_scorers_haku(self):
        top_scorers = self.statistics.top_scorers(2)
        self.assertEqual(self.statistics.top_scorers(2), top_scorers)