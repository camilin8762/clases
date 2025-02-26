

def mediana(lista):
    if len(lista)%2 == 0:
        lista.sort()
        m = (lista[len(lista)//2-1] + lista[len(lista)//2])/2
    else:
        lista.sort()
        m = lista[len(lista)//2]
    return m

li=[1,2,3,4,5,6,7,8,9,10] 
print(li)
print(mediana(li))
        