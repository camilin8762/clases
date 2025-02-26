import random
def llenarli(li,can):
    for i in range(can):
        num=random.randint(1,100)
        li.append(num)
    return li
def suma_li (lista): 
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

li=[]
can=random.randint(5,20)
li=llenarli(li,can)
print(li)
print(suma_li(li))

