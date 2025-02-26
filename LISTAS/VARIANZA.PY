import random
def llenarli(li,can):
    for i in range(can):
        num=random.randint(1,100)
        li.append(num)
    return li

def media (lista): 
    suma = 0
    for i in lista:
        suma = suma + i
        m= suma / len(lista)
    return  m

def varianza(lista):
    suma = 0
    for i in lista:
        suma = suma + (i - media(lista))**2
        v=suma / len(lista)
    return v




li = []
can=random.randint(5,20)
li=llenarli(li,can)
print(li)
print(varianza(li))