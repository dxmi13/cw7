import random
import string
from typing import Dict, Tuple


def generuj_klucz() -> Dict[str, str]:
    """
    Generuje losowy klucz.

    Zwraca:
        Dict[str, str]: Słownik mapujący każdą literę alfabetu na inną literę.
    """
    litery = list(string.ascii_uppercase)
    random.shuffle(litery)
    return {oryginal: podstawienie for oryginal, podstawienie in zip(string.ascii_uppercase, litery)}


def podstawienie_monoalfabetyczne(tekst: str, klucz: Dict[str, str]) -> str:
    """
    Zastępuje każdą literę w tekście zgodnie z kluczem.

    Argumenty:
        tekst (str): Tekst do zaszyfrowania.
        klucz (Dict[str, str]): Słownik.

    Zwraca:
        str: Zaszyfrowany tekst.
    """
    tekst = tekst.upper().replace(" ", "")
    podstawiony_tekst = ''.join(klucz.get(znak, znak) for znak in tekst)
    return podstawiony_tekst


def transpozycja_kolumnowa(tekst: str, dlugosc_klucza: int) -> str:
    """
    Transponuje tekst, dzieląc go na kolumny o podanej długości i łączy te kolumny.

    Argumenty:
        tekst (str): Tekst do transpozycji.
        dlugosc_klucza (int): Długość kolumny.

    Zwraca:
        str: Transponowany tekst.
    """
    n = len(tekst)
    dlugosc_klucza = min(dlugosc_klucza, n)

    dlugosc_uzupelnienia = (dlugosc_klucza - n % dlugosc_klucza) % dlugosc_klucza
    tekst += 'X' * dlugosc_uzupelnienia

    kolumny = [tekst[i::dlugosc_klucza] for i in range(dlugosc_klucza)]
    transponowany_tekst = ''.join(kolumny)
    return transponowany_tekst


def transpozycja_wierszowa(tekst: str, dlugosc_klucza: int) -> str:
    """
    Transponuje tekst, przestawiając wiersze o podanej długości.

    Argumenty:
        tekst (str): Tekst do transpozycji.
        dlugosc_klucza (int): Długość wiersza.

    Zwraca:
        str: Transponowany tekst.
    """
    n = len(tekst)
    dlugosc_klucza = min(dlugosc_klucza, n)

    wiersze = [tekst[i:i + dlugosc_klucza] for i in range(0, n, dlugosc_klucza)]
    transponowany_tekst = ''.join([''.join(wiersz) for wiersz in zip(*wiersze)])
    return transponowany_tekst


def szyfr(tekst: str) -> Tuple[str, Dict[str, str]]:
    """
    Szyfruje tekst za pomocą podstawienia monoalfabetycznego oraz transpozycji kolumnowej i wierszowej.

    Argumenty:
        tekst (str): Tekst do zaszyfrowania.

    Zwraca:
        Tuple[str, Dict[str, str]]: Zaszyfrowany tekst oraz użyty klucz.
    """

    klucz_podstawieniowy = generuj_klucz()

    podstawiony_tekst = podstawienie_monoalfabetyczne(tekst, klucz_podstawieniowy)

    dlugosc_klucza_kolumn = random.randint(2, 10)
    transponowany_tekst_kolumnowy = transpozycja_kolumnowa(podstawiony_tekst, dlugosc_klucza_kolumn)

    dlugosc_klucza_wierszy = random.randint(2, 10)
    transponowany_tekst_wierszowy = transpozycja_wierszowa(transponowany_tekst_kolumnowy, dlugosc_klucza_wierszy)

    return transponowany_tekst_wierszowy, klucz_podstawieniowy


def zapisz_tekst_do_pliku(tekst: str, nazwa_pliku: str) -> None:
    """
    Zapisuje podany tekst do pliku.

    Argumenty:
        tekst (str): Tekst.
        nazwa_pliku (str): Nazwa pliku, do którego tekst ma zostać zapisany.
    """
    with open(nazwa_pliku, 'w') as plik:
        plik.write(tekst)


tekst = "The Caesar cipher is what’s known as a substitution cipher, because each letter is substituted with another one; other variations on this, then, would substitute letter blocks or whole words. For most of history, cryptography consisted of various substitution ciphers deployed to keep government and military communications secure. Medieval Arab mathematicians pushed the science forward, particularly the art of decryption—once researchers realized that certain letters in a given language are more common than others, it becomes easier to recognize patterns, for instance. But most pre-modern encryption is incredibly simple by modern standards, for the obvious reason that, before the advent of computers, it was difficult to perform mathematical transformations quickly enough to make encryption or decryption worthwhile. In fact, the development of computers and advances in cryptography went hand in hand. Charles Babbage, whose idea for the Difference Engine presaged modern computers, was also interested in cryptography. During World War II, the Germans used the electromechanical Enigma machine to encrypt messages—and, famously, Alan Turing led a team in Britain that developed a similar machine to break the code, in the process laying some of the groundwork for the first modern computers. Cryptography got radically more complex as computers became available, but it remained the province of spies and generals for several more decades."
zaszyfrowany_tekst, klucz = szyfr(tekst)

print("Oryginalny tekst: ", tekst)
print('\n')
print("Zaszyfrowany tekst: ", zaszyfrowany_tekst)
print('\n')
print("Klucz podstawieniowy: ", klucz)

zapisz_tekst_do_pliku(zaszyfrowany_tekst, "zaszyfrowany.txt")
