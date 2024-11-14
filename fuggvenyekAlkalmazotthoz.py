def fizSum(lista):
    osszFiz:int=0
    for i in range (0, len(lista), 1):
        osszFiz+=(lista[i].fizetes)
    return osszFiz

def legidosebbDolg(lista):
    maxEletkor:int=0
    kor:int=lista[0].kor
    for i in range(0, len(lista), 1):
        if(kor>maxEletkor):
            maxEletkor=kor
        kor=lista[i].kor
    return maxEletkor

def beosztottDb(lista):
    db:int=0
    for i in range (0, len(lista), 1):
        if (lista[i].pozicio=="beosztott"):
            db+=1
    return db

def kinekMinFizetes(lista):
    minFiz_index:int=(0)
    kinek:str=""
    for i in range (0, len(lista), 1):
        if (lista[minFiz_index].fizetes>lista[i].fizetes):
            minFiz_index=i

    return minFiz_index
