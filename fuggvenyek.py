def etlap(lista):
    """itt írjuk ki az ételek neveit"""
    for i in range (0, len(lista), 1):
        print(f"** {lista[i].nev} {lista[i].ar} Ft **")

def atlag_ar(lista):
    osszeg:int=0
    db:int=0
    for i in range (0, len(lista), 1):
        osszeg+=(lista[i].ar)
        db+=1
    atlag:float = osszeg/db
    return atlag

def legdragabb(etel_lista):
    max_index = 0
    for i in range (0,len(etel_lista),1):
        if (etel_lista[i].ar < etel_lista[max_index].ar):
            max_index+=1
    return max_index
