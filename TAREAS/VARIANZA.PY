
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


li=[1,2,3,4,5,6,7,8,9,10] 
print(li)
print(varianza(li))