import random


def llenarli(lista,can):
    for i in range(can):
        num=random.randint(1,10)
        li.append(num)
    return li
def ordenar_ascen(lista):
    inter=True
    
    while inter:
        inter=False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]: 
                inter=True
                lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista

def ordenar_descen(lista):
    inter=True
    
    while inter:
        inter=False
        for i in range(len(lista)-1):
            if lista[i]<lista[i+1]: 
                inter=True
                lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista


li=[]
can=random.randint(10,20)
li=llenarli(li,can)
print(li)
ordenar_ascen(li)
print(li)
ordenar_descen(li)
print(li)
def moda(li):
    fer=[]
    for i in li:
        con=0
        for x in li:
            if x == i:
                con+=1
        fer.append(con)
            
    max_fer=max(fer)
    
    mod=[]
    for z in range( len(li) ):
        if fer[z]==max_fer and li [z] not in mod:
            mod.append(li[z])
    return mod


print(moda(li))



