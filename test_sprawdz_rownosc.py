import unittest
from sprawdzRownosc import sprawdz_rownosc #unit test, w tym skrypcie testujemy ta i tylko ta funkcje

a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")


class TestSprawdz_czy_na_stanie(unittest.TestCase):
    
    def test_czy_na_stanie_int(self):
        self.assertEqual(True,sprawdz_rownosc(a,b,c))

if __name__ == '__main__':
    unittest.main()
