import unittest
import sys
sys.path.append("..")
import kunportu.datumbazo as datumbazo

class TestStringMethods(unittest.TestCase):

    def test_enpaki_nekonata_kategorio(self):
        self.assertFalse(datumbazo.enpaki("volapukajx", grupo=1, grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Hanabi", ecoj={}))

    def test_enpaki_konata_ludo(self):
        cxu_enpakita = datumbazo.enpaki("ludo", grupo=1, grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Hanabi", ecoj={})
        self.assertTrue(cxu_enpakita)

    def test_enpaki_nekonata_ludo(self):
        cxu_enpakita = datumbazo.enpaki(
            "ludo", grupo=1, grupnomo="Testo", chat_id=1, uzanto_id=1, kunportajxo_nomo="Volapukludo", ecoj={}
        )
        self.assertFalse(cxu_enpakita)

if __name__ == '__main__':
    unittest.main()
