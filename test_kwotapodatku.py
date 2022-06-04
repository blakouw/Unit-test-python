import unittest
from numpy import double
from kwotapodatku import oblicz_kwote_podatku #unit test, w tym skrypcie testujemy ta i tylko ta funkcje

kwota_brutto=double(input("Wprowadz kwote brutto: "))
stawka_podatku=double(input("Wprowadz stawke podatku: "))

def wartosc_podatkuVAT():
    return kwota_brutto*stawka_podatku#oblicza oczekiwana wartosc podatku

class TestKwotaPodatku(unittest.TestCase):
    
    def test_kwota_int(self):
        print("Kwota Brutto:",kwota_brutto)
        self.assertEqual(oblicz_kwote_podatku(kwota_brutto,stawka_podatku),wartosc_podatkuVAT())



if __name__ == '__main__':
    unittest.main()

