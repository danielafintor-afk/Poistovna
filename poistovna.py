import re

class Poisteny:
    def __init__(self, meno, priezvisko, vek, telefon):
        if not meno.strip() or not priezvisko.strip():
            raise ValueError("Meno a priezvisko nesmú byť prázdne.")
        self.meno = meno.strip().title()
        self.priezvisko = priezvisko.strip().title()
        self.vek = vek
        self.telefon = telefon  # 10 číslic

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.vek} {self.telefon}"


class Evidencia:
    def __init__(self):
        # Tu sa ukladajú všetci poistení do pamäte
        self.poisteni = []

    def pridaj_poisteneho(self, poisteny):
        self.poisteni.append(poisteny)

    def vypis_vsetkych(self):
        print("\n--- Zoznam poistených ---")
        if len(self.poisteni) == 0:
            print("Zatiaľ nie sú evidovaní žiadni poistení.\n")
        else:
            for p in self.poisteni:
                print(f"{p.meno} {p.priezvisko} {p.vek} {p.telefon}")
            print()  # prázdny riadok pre oddelenie výpisu

    def vyhladaj_poisteneho(self, meno, priezvisko):
        print("\n--- Výsledok vyhľadávania ---")
        najdeni = [
            p for p in self.poisteni
            if p.meno.lower() == meno.lower() and p.priezvisko.lower() == priezvisko.lower()
        ]
        if najdeni:
            for p in najdeni:
                print(f"{p.meno} {p.priezvisko} {p.vek} {p.telefon}")
        else:
            print("Poistený nebol nájdený.")
        print()


class Konzola:
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
                self.evidencia.vypis_vsetkych()
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
        print("\n--- Pridanie poisteného ---")
        meno = input("Meno: ").strip()
        priezvisko = input("Priezvisko: ").strip()
        while True:
            try:
                vek = int(input("Vek: ").strip())
                if vek > 0:
                    break
                else:
                    print("Vek musí byť kladné číslo.")
            except ValueError:
                print("Zadajte celé číslo.")

        telefon = self.nacitaj_telefon()

        poisteny = Poisteny(meno, priezvisko, vek, telefon)
        self.evidencia.pridaj_poisteneho(poisteny)
        print("\n Poistený bol pridaný!\n")

    def vyhladaj_poisteneho(self):
        meno = input("Zadajte meno: ").strip()
        priezvisko = input("Zadajte priezvisko: ").strip()
        self.evidencia.vyhladaj_poisteneho(meno, priezvisko)


if __name__ == "__main__":
    app = Konzola()
    app.spusti()
