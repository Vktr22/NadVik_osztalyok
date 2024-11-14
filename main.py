"""
osztalyzatok_lista=[1,4,2,3]
nevek=["Béla","Jenő","Ági","Rozi",3]

nevek és a nevekhez tartozó osztályzatok összetartoznak

etelek=["húsleves","krumplis"]
ar=[1234,3456]

új adatszerkezet

szemely = {név: "Béla", osztályzat:3 }

kaja1 = {nev: "húsleves", ar:1234, elk_ido:2 }
kaja2 = {nev: "krumplis", ar:12345 elk_ido:0.5 }

objektumok - tulajdonságokkal(főnevek) és viselkedéssel(cselekvés) bíró adatszrkezet

készítünk egy sablont ami alapján letudjuk gyártani a konkrét egyedeket(ételeket,emberek).
OSZTÁLY - sablon - osztály - tervrajz
OBJEKTUM - konkrét egyedek - objektumok - konkrét termék


"""

from Etel import Etel
import fuggvenyek

"""2. lépés létrehozzuk a konkrét példányít a tervrajz alapján"""
"""etel1=Etel("Húsleves",1234)
etel2=Etel("Krumplis",2345)
etel3=Etel("Rántott hús",2145)
etel4=Etel("Palacsinta",1450)"""
etel_lista=[] #berakjuk listába
etel_lista.append(Etel("Húsleves",1234))
etel_lista.append(Etel("Krumplis",2345))
etel_lista.append(Etel("Rántott hús",2145))
etel_lista.append(Etel("Palacsinta",1450))


print("Szia én vagyok a " + etel_lista[0].nev + " Az állapotom " + etel_lista[0].allapot ) #folyamatban kiir

"""etel1.keszul()
print("Szia én vagyok a " + etel1.nev + " Az állapotom " + etel1.allapot ) #megváltozik készre az állapot
print("Szia én vagyok a " + etel2.nev + " Az állapotom " + etel2.allapot ) 
"""
"""írj metódust, mely paraméterként megkapja a listát és
kiyrja az ételek neveit és árait látványos formában"""
fuggvenyek.etlap(etel_lista)

"""írj metódust, mely paraméterként megkapja a listát és, megmondja az ételek átlagárát"""
atlagar=fuggvenyek.atlag_ar(etel_lista)
print(f"Az ételek  átlagára: {atlagar:.2f} Ft")

"""írj metódust, mely paraméterként megkapja a listát és, megmondja a legdrágább étel nevét"""
legdragabb_index=fuggvenyek.legdragabb(etel_lista)
#print(f"A legdrágább étel neve és ára {}, {}")

"""hozz létre egy Alkalmazott osztályt, melyben az alábbi adatokat
tudod tárolni egy cég dolgozóiról:
nev.str
szul_datum_fizetes:int
fizeted:int
pozicio.str
kor:int

keszits hozza metodust, ami megmondja az adott ember korát
__str__

Hozz létre legalább 5 embert, tedd bele őket listába
- mennyi az össz fizetés?
- hány éves a legidősebb ember?
- hány ember van 'beosztott' pozícióba?
- kinek a legalacsonyabb a fizetése?

++ az osztálynak legyen egy fizetés emelés metódusa,
amelyik a fizetést megemeli a paraméterében megadott százalék értékkel.
A legkisebb fizetésű ember fizetését emeld meg 20%-al!"""