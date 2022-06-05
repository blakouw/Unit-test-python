import unittest
from sprawdzRownosc import sprawdz_rownosc #unit test, w tym skrypcie testujemy ta i tylko ta funkcje

a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")


class TestSprawdz_rownosc(unittest.TestCase):
    
    def test_Sprawdz_rownosc_int(self):
        self.assertEqual(True,sprawdz_rownosc(a,b,c))

if __name__ == '__main__':
    unittest.main()
