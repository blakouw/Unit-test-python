from genericpath import exists
from itertools import count
import unittest
from sprawdz import sprawdz_czy_na_stanie #unit test, w tym skrypcie testujemy ta i tylko ta funkcje
import math

id_artykulu=int(input("Podaj numer identyfikacyjny dla danego typu artykulu: "))

"""
def czy_poprawne_id(id_artykulu):
   digits = int(math.log10(id_artykulu))
    if digits==4:
        return True
    else:
        return False
"""

stan_magazynowy=[4061,3103,9831,4061,4061,3103]

class TestSprawdz_czy_na_stanie(unittest.TestCase):
    
    def test_czy_na_stanie_int(self):
        self.assertEqual(stan_magazynowy.count(id_artykulu),sprawdz_czy_na_stanie(id_artykulu))

if __name__ == '__main__':
    unittest.main()

