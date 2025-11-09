class Poisteny:
    """Trieda reprezentuje jednu poistenú osobu."""

    def __init__(self, meno, priezvisko, vek, telefon):
        if not meno.strip() or not priezvisko.strip():
            raise ValueError("Meno a priezvisko nesmú byť prázdne.")
        if not (0 < vek <= 120):
            raise ValueError("Vek musí byť v rozsahu 1 až 120.")
        if len(telefon) != 10 or not telefon.isdigit():
            raise ValueError("Telefónne číslo musí mať presne 10 číslic.")

        self.meno = meno.strip().title()
        self.priezvisko = priezvisko.strip().title()
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.vek} {self.telefon}"
