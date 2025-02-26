
def media (lista): 
    suma = 0
    for i in lista:
        suma = suma + i
    m= suma / len(lista)
    return  m

li=[1,2,3,4,5,6,7,8,9,10] 
print(li)
print(media(li))