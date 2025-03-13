import data
import random

def pais(lista):
    for dic in lista:
        paises=['UK','USA','Australia','Canada']
        dic['country']=random.choice(paises)
    return lista


def nombre(lista):
    for dic in data.personas:
        for k in  dic.keys():
            nom=(dic["name"])
        lista.append(nom)
    return lista

#nombres=[]
#print(nombre(nombres))
def us(lista):
    usa=set()
    for dic in data.personas:
        for k in dic.keys():
            if dic["country"]=="USA":
                coun=dic["name"]
                usa.add(coun)
    return usa

def u(lista):
    uk=set()
    for dic in data.personas:
        if dic["country"]=="UK":
            coun=dic["name"]
            uk.add(coun)
    return uk

def australia(lista):
    aus=set()
    for dic in data.personas:
        if dic["country"]=="Australia":
            coun=dic["name"]
        aus.add(coun)
    return aus

def canada(lista):
    cana=set()
    for dic in data.personas:
        for k in dic.keys():
            if dic["country"]=="Canada":
                coun=dic["name"]
                cana.add(coun)
    return usa



pai=pais(data.personas)
usa=us(pai)
uk=u(pai)
aus=australia(pai)
can=canada(pai)

#print(usa)
print(pai)
#print(uk)
print(aus)
#print(can)