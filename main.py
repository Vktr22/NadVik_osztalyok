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

"""2. lépés létrehozzuk a konkrét példányít a tervrajz alapján"""
etel1=Etel("Húsleves",1234)
etel2=Etel("Krumplis",2345)
etel3=Etel("Rántott hús",2145)
etel4=Etel("Palacsinta",1450)
etel_lista=[] #berakjuk listába
etel_lista.append(etel1)
etel_lista.append(etel2)
etel_lista.append(etel3)
etel_lista.append(etel4)


print("Szia én vagyok a " + etel1.nev + " Az állapotom " + etel1.allapot ) #folyamatban kiir

etel1.keszul()
print("Szia én vagyok a " + etel1.nev + " Az állapotom " + etel1.allapot ) #megváltozik készre az állapot
print("Szia én vagyok a " + etel2.nev + " Az állapotom " + etel2.allapot ) 


