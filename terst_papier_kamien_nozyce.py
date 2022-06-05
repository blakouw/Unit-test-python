import unittest
from papier_kamien_nozyc import papier_kamien_nozyce #unit test, w tym skrypcie testujemy ta i tylko ta funkcje



player1_action=input("Gracz1: wybierz ruch: ")
player2_action=input("Gracz2: wybierz ruch: ")
wygrany='User1'
class TestSprawdz_czy_na_stanie(unittest.TestCase):
    
    def test_czy_na_stanie_int(self):
        self.assertEqual(wygrany,papier_kamien_nozyce(player1_action,player2_action))

if __name__ == '__main__':
    unittest.main()

