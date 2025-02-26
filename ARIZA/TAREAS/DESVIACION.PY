
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

li=[1,2,3,4,5,6,7,8,9,10] 
print(li)

print(desviacion(li))