import random
def llenarli(li,can):
    for i in range(can):
        num=random.randint(1,100)
        li.append(num)
    return li

def mediana(lista):
    if len(lista)%2 == 0:
        lista.sort()
        m = (lista[len(lista)//2-1] + lista[len(lista)//2])/2
    else:
        lista.sort()
        m = lista[len(lista)//2]
    return m

li = []
can=random.randint(5,20)
li=llenarli(li,can)
print(li)
print(mediana(li))
        