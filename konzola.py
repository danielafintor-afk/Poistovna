import re
from poisteny import Poisteny
from evidencia import Evidencia

class Konzola:
    """Trieda zodpovedá za komunikáciu s používateľom."""

    def __init__(self):
        self.evidencia = Evidencia()

    def spusti(self):

        while True:
            print("=" * 40)
            print("EVIDENCIA POISTENÝCH".center(40))
            print("=" * 40)
            print("1. Pridať poisteného")
            print("2. Zobraziť všetkých poistených")
            print("3. Vyhľadať poisteného")
            print("4. Ukončiť program")
            volba = input("Zvoľte možnosť: ").strip()

            if volba == "1":
                self.pridaj_poisteneho()
            elif volba == "2":
                print("\n--- Zoznam poistených ---")
                print(self.evidencia.vypis_vsetkych(), "\n")
            elif volba == "3":
                self.vyhladaj_poisteneho()
            elif volba == "4":
                print("Koniec programu.")
                break
            else:
                print("Neplatná voľba.\n")

    def nacitaj_telefon(self):
        """Overí, že číslo obsahuje presne 10 číslic."""
        while True:
            tel = input("Zadajte telefónne číslo (10 číslic): ").strip()
            cisla = re.sub(r"\D", "", tel)
            if len(cisla) == 10:
                return cisla
            print("Formát čísla je nesprávny – zadajte presne 10 číslic.\n")

    def pridaj_poisteneho(self):
        """Načíta údaje o poistenom a pridá ho do evidencie."""
        print("\n--- Pridanie poisteného ---")
        meno = input("Meno: ").strip()
        priezvisko = input("Priezvisko: ").strip()

        while True:
            try:
                vek = int(input("Vek: ").strip())
                if 0 < vek <= 120:
                    break
                print("Vek musí byť číslo od 1 do 120.")
            except ValueError:
                print("Zadajte celé číslo.")

        telefon = self.nacitaj_telefon()

        poisteny = Poisteny(meno, priezvisko, vek, telefon)
        self.evidencia.pridaj_poisteneho(poisteny)
        print("\n Poistený bol pridaný!\n")

    def vyhladaj_poisteneho(self):
        meno = input("Zadajte meno: ").strip()
        priezvisko = input("Zadajte priezvisko: ").strip()
        print("\n--- Výsledok vyhľadávania ---")
        print(self.evidencia.vyhladaj_poisteneho(meno, priezvisko), "\n")
