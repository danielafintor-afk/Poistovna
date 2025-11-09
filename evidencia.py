from poisteny import Poisteny

class Evidencia:
    """Trieda spravuje kolekciu poistených osôb."""

    def __init__(self):
        self.poisteni = []

    def pridaj_poisteneho(self, poisteny: Poisteny):
        self.poisteni.append(poisteny)

    def vypis_vsetkych(self):
        """Vráti zoznam všetkých poistených ako text."""
        if not self.poisteni:
            return "Zatiaľ nie sú evidovaní žiadni poistení."
        return "\n".join(str(p) for p in self.poisteni)

    def vyhladaj_poisteneho(self, meno, priezvisko):
        """Vyhľadá poisteného podľa mena a priezviska."""
        najdeni = [
            p for p in self.poisteni
            if p.meno.lower() == meno.lower() and p.priezvisko.lower() == priezvisko.lower()
        ]
        if not najdeni:
            return "Poistený nebol nájdený."
        return "\n".join(str(p) for p in najdeni)
