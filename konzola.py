import re
from poisteny import Poisteny
from evidencia import Evidencia

class Konzola:
    """Trieda zodpovedá za komunikáciu s používateľom."""

    def __init__(self):
        self.evidencia = Evidencia()

    def spusti(self):

        while True:
            self.vypis_menu()
            volba = input("Zvoľte možnosť: ").strip()

            akcie = {
                "1": self.pridaj_poisteneho,
                "2": self.vypis_poistenych,
                "3": self.vyhladaj_poisteneho,
                "4": self.ukoncit_program
            }

            akcia = akcie.get(volba)
            if akcia:
                akcia()
            else:
                print("Neplatná voľba.\n")



    def vypis_menu(self):

        print("=" * 40)
        print("EVIDENCIA POISTENÝCH".center(40))
        print("=" * 40)
        print("1. Pridať poisteného")
        print("2. Zobraziť všetkých poistených")
        print("3. Vyhľadať poisteného")
        print("4. Ukončiť program")

    def nacitaj_text(self, prompt):
        """Načíta textový vstup."""
        while True:
            hodnota = input(f"{prompt}: ").strip()
            if hodnota:
                return hodnota
            print(f"{prompt} nesmie byť prázdne.\n")

    def nacitaj_cislo(self, prompt, minimum=None, maximum=None):
        """Načíta celé číslo v danom rozsahu."""
        while True:
            try:
                cislo = int(input(f"{prompt}: ").strip())
                if (minimum is None or cislo >= minimum) and (maximum is None or cislo <= maximum):
                    return cislo
                print(f"Hodnota musí byť medzi {minimum} a {maximum}.")
            except ValueError:
                print("Zadajte celé číslo.")

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
        meno = self.nacitaj_text("Meno")
        priezvisko = self.nacitaj_text("Priezvisko")
        vek = self.nacitaj_cislo("Vek", 1, 120)
        telefon = self.nacitaj_telefon()

        poisteny = Poisteny(meno, priezvisko, vek, telefon)
        self.evidencia.pridaj_poisteneho(poisteny)
        print("\n Poistený bol pridaný!\n")

    def vypis_poistenych(self):
        """Vypíše všetkých poistených."""
        print("\n--- Zoznam poistených ---")
        print(self.evidencia.vypis_vsetkych(), "\n")

    def vyhladaj_poisteneho(self):
        """Vyhľadá poisteného podľa mena a priezviska."""
        print("\n--- Vyhľadávanie poisteného ---")
        meno = self.nacitaj_text("Meno")
        priezvisko = self.nacitaj_text("Priezvisko")
        print("\n--- Výsledok vyhľadávania ---")
        print(self.evidencia.vyhladaj_poisteneho(meno, priezvisko), "\n")

    def ukoncit_program(self):
        """Ukončí aplikáciu."""
        print("Koniec programu.")
        exit()
