from datetime import datetime

class Szoba:
    def __init__(self, szoba_szam, ar):
        self.szoba_szam = szoba_szam
        self.ar = ar

class EgyszemelyesSzoba(Szoba):
    def __init__(self, szoba_szam, ar, leiras):
        super().__init__(szoba_szam, ar)
        self.leiras = leiras

class KetszemelyesSzoba(Szoba):
    def __init__(self, szoba_szam, ar, agy_tipus):
        super().__init__(szoba_szam, ar)
        self.agy_tipus = agy_tipus

class HotelSzoba:
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = []

    def szoba_foglalas(self, datum):
        print("Elérhető szobák a megadott dátumra:")
        elerheto_szobak = []
        for szoba in self.szobak:
            foglalt = False
            for foglalas in self.foglalasok:
                if foglalas['szoba_szam'] == szoba.szoba_szam and foglalas['datum'] == datum:
                    foglalt = True
                    break
            if not foglalt:
                elerheto_szobak.append(szoba)
                agyak_szama = "Egyágyas" if isinstance(szoba, EgyszemelyesSzoba) else "Kétágyas"
                print(f"  - Szoba száma: {szoba.szoba_szam}, Ár: {szoba.ar}€, {agyak_szama}")

        if not elerheto_szobak:
            print("Nincs elérhető szoba a megadott dátumra.")
            return None

        valasztott_szoba_szam = input("Kérjük, válasszon egy szobát a fenti listából: ")
        for szoba in elerheto_szobak:
            if szoba.szoba_szam == valasztott_szoba_szam:
                self.foglalasok.append({'szoba_szam': szoba.szoba_szam, 'datum': datum})
                return szoba.ar
        return "Nem létezik ilyen szoba."

    def foglalas_megszuntetes(self, szoba_szam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szoba_szam'] == szoba_szam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                return "A foglalást sikeresen töröltük."
        return "A foglalás nem található."

    def foglalasok_listazasa(self):
        return self.foglalasok

def main():
    szallas = HotelSzoba("GDE Hotel", [])
    adatok_betoltese(szallas)

    while True:
        print("Üdvözöljük a", szallas.nev, "szállodában")
        print("1. Szoba foglalása")
        print("2. Foglalás megszüntetése")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válasszon egy lehetőséget: ")

        if valasztas == '1':
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                datetime.strptime(datum, "%Y-%m-%d")
                ar = szallas.szoba_foglalas(datum)
                if ar:
                    print(f"Köszönjük a foglalást! A szoba ára: {ar}€")
            except ValueError:
                print("Érvénytelen dátum formátum.")

        elif valasztas == '2':
            szoba_szam = input("Adja meg a szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            print(szallas.foglalas_megszuntetes(szoba_szam, datum))

        elif valasztas == '3':
            print("Foglalások listája:")
            for foglalas in szallas.foglalasok_listazasa():
                print("Szoba:", foglalas['szoba_szam'], "- Dátum:", foglalas['datum'])

        elif valasztas == '4':
            print("Programból való kilépés.")
            break

        else:
            print("Érvénytelen választás. Kérem, válasszon egy érvényes lehetőséget.")

def adatok_betoltese(szallas):
    szoba1 = EgyszemelyesSzoba("101", 100, "Egyágyas")
    szoba2 = KetszemelyesSzoba("201", 150, "Kétágyas")
    szoba3 = EgyszemelyesSzoba("301", 120, "Egyágyas")
    szallas.szobak.extend([szoba1, szoba2, szoba3])
    szallas.foglalasok.extend([
        {'szoba_szam': szoba1.szoba_szam, 'datum': '2024-05-15'},
        {'szoba_szam': szoba2.szoba_szam, 'datum': '2024-05-17'},
        {'szoba_szam': szoba3.szoba_szam, 'datum': '2024-05-19'},
        {'szoba_szam': szoba1.szoba_szam, 'datum': '2024-05-20'},
        {'szoba_szam': szoba2.szoba_szam, 'datum': '2024-05-22'}
    ])


main()
