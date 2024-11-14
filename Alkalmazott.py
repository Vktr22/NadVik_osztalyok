"""
nev.str
szul_datum:int
fizetes:int
pozicio.str
kor:int
"""
from datetime import datetime
class Alkalmazott:
    def __init__(self, nev:str="",szul_datum:int=2000,fizetes:int=800000, pozicio:str="",kor:int=24):
        self.nev=nev
        self.szul_datum=szul_datum
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.kor=self.korFgv()

    def korFgv(self):
        jelenlegi_ev = datetime.now().year
        self.kor=jelenlegi_ev-self.szul_datum
        return self.kor

    def __str__(self):
        return (f"Név: {self.nev}, "
                f"Születési dátum: {self.szul_datum}, "
                f"Fizetés: {self.fizetes} Ft, "
                f"Pozíció: {self.pozicio}, "
                f"Kor: {self.kor} év")
