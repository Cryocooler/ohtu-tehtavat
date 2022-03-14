
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava positiivinen kokonaisluku")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kasvatuskoon on oltava positiivinen kokonaisluku")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku : int):
        if luku in self.lukujono:
            return True
        return False

    def lisaa(self, lisattava : int):
        if self.kuuluu(lisattava):
            return False

        self.lukujono[self.alkioiden_lkm] = lisattava
        self.alkioiden_lkm +=1

        if self.alkioiden_lkm - len(self.lukujono) == 0:
            self.lukujono.append([0] * self.kasvatuskoko)

    def poista(self, poistettava : int):

        if self.kuuluu(poistettava):
            self.lukujono.remove(poistettava)
            self.lukujono[self.alkioiden_lkm -1] = 0
            self.alkioiden_lkm -=1

            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]
        return False



    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste.lisaa(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus.poista(b_taulu[i])

        return erotus

    def __str__(self):

        merkkijono = ', '.join(str(alkio) for alkio in self.lukujono[:self.alkioiden_lkm])
        return f'{{{merkkijono}}}'

        # if self.alkioiden_lkm == 0:
        #     return "{}"
        # elif self.alkioiden_lkm == 1:
        #     return "{" + str(self.lukujono[0]) + "}"
        # else:
        #     tuotos = "{"
        #     for i in range(0, self.alkioiden_lkm - 1):
        #         tuotos = tuotos + str(self.lukujono[i])
        #         tuotos = tuotos + ", "
        #     tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
        #     tuotos = tuotos + "}"
        #     return tuotos
