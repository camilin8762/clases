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


def desviacion(lista):
    
    suma = 0
    for i in lista:
        suma += (i - media(lista)) ** 2
    des= (suma / len(lista)) ** (1/2)
    return des

li=[] 
can=random.randint(5,20)
li=llenarli(li,can)
print(li)

print(desviacion(li))