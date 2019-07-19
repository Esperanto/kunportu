import unittest
import sys
sys.path.append("..")
import kunportu.datumbazo as datumbazo

class TestStringMethods(unittest.TestCase):

    def test_enpaki_nekonata_kategorio(self):
        self.assertFalse(datumbazo.enpaki("volapukajx", grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Hanabi", ecoj={}))
        datumbazo.session.commit()

    def test_enpaki_konata_ludo(self):
        cxu_enpakita = datumbazo.enpaki("ludo", grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Hanabi", ecoj={})
        self.assertTrue(cxu_enpakita)
        datumbazo.session.commit()

    def test_enpaki_nekonata_ludo(self):
        cxu_enpakita = datumbazo.enpaki(
            "ludo", grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Volapukludo", ecoj={}
        )
        self.assertFalse(cxu_enpakita)
        datumbazo.session.commit()

    def test_elpaki_nur_povas_enpakanto(self):
        antauxe = len(datumbazo.session.query(datumbazo.Kunportajxo).all())
        cxu_enpakita = datumbazo.enpaki("ludo", grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Kuhhandel", ecoj={})
        #ne elpakas kiam ne estas sama homo en sama grupo, kiu enpakis
        self.assertEquals(1, len(datumbazo.session.query(datumbazo.Kunportajxo).all())-antauxe)
        cxu_enpakita = datumbazo.elpaki("ludo", chat_id=2, uzanto_id=1, kunportajxo_nomo="Kuhhandel")
        self.assertEquals(1, len(datumbazo.session.query(datumbazo.Kunportajxo).all())-antauxe)
        cxu_enpakita = datumbazo.elpaki("ludo", chat_id=1, uzanto_id=2, kunportajxo_nomo="Kuhhandel")
        self.assertEquals(1, len(datumbazo.session.query(datumbazo.Kunportajxo).all())-antauxe)
        cxu_enpakita = datumbazo.elpaki("volapukajx", chat_id=1, uzanto_id=1, kunportajxo_nomo="Kuhhandel")
        self.assertEquals(1, len(datumbazo.session.query(datumbazo.Kunportajxo).all())-antauxe)
        cxu_enpakita = datumbazo.elpaki("ludo", chat_id=1, uzanto_id=1, kunportajxo_nomo="l")
        #elpakis kiam samas enpakanto
        cxu_enpakita = datumbazo.elpaki("ludo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Kuhhandel")
        self.assertEquals(0, len(datumbazo.session.query(datumbazo.Kunportajxo).all())-antauxe)

if __name__ == '__main__':
    unittest.main()
