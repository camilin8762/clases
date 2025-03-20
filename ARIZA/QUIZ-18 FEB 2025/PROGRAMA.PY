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
def mediana(lista):
    if len(lista)%2 == 0:
        lista.sort()
        m = (lista[len(lista)//2-1] + lista[len(lista)//2])/2
    else:
        lista.sort()
        m = lista[len(lista)//2]
    return m
def mayor(lista):
    if len(lista) == 0:
        print('error')
    else:
        mayor = lista[0]
        for i in range(1,len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
def menor(lista):
    if len(lista) == 0:
        return None
    else:
        men = lista[0]
        for i in range(1,len(lista)):
            if lista[i] <  men:
                men = lista[i]
        return men
def varianza(lista):
    suma = 0
    for i in lista:
        suma = suma + (i - media(lista))**2
        v=suma / len(lista)
    return v
def desviacion(lista):
    des= (varianza(lista) / len(lista)) ** (1/2)
    return des


li = []
can=random.randint(5,20)
li=llenarli(li,can)
print(li)
print(mayor(li))
print(menor(li))
print(media(li))
print(mediana(li))
print(varianza(li))
print(desviacion(li))
print