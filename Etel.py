"""1.lépés: osztály létrehozása"""
class Etel:
    def __init__(self, nev:str="",ar:int=1000):
        """Konstruktor feladata,hogy létrehozza a konkrét példányt a konkrét adatokkal a tervrajzból
        +beállítsa az adattagokat - objektum
        tulajdonságok értékei"""
        self.nev=nev 
        self.ar=ar
        self.allapot="folyamatban"
    
    def keszul(self):
        self.allapot="kész"