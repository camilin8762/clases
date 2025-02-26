
import random
def llenarli(li,can):
    for i in range(can):
        num=random.randint(1,100)
        li.append(num)
    return li
def menor(lista):
    if len(lista) == 0:
        return None
    else:
        men = lista[0]
        for i in range(1,len(lista)):
            if lista[i] <  men:
                men = lista[i]
        return men
    
li=[]
can=random.randint(5,20)
li=llenarli(li,can)
print(li)
print(menor(li))