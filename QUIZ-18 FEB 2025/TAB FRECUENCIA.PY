import random

def llenarli(lista):
    can=random.randint(5,20)
    for i in range(can):
        num=random.randint(1,10)
        lista.append(num)
    lista.sort()
    return lista
li=[]
li=llenarli(li)
print(li)

def frecabso(lista):
    
    fre=[]
    for i in lista:
        con=0
        for x in lista:
            if x == i:
                con += 1
        fre.append(con)
        fret=[]
        for z in range(len(fre)):
            if fre[z]==fre[z-1] and fre[z] not in fret or fre[z-1]!=fre[z] :
                fret.append(fre[z])
    return fret

print(frecabso(li))

def fre_relativa(lista):
    fre=frecabso(lista)
    fr=[]
    for i in fre:
         