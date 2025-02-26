import random
def llenarli(li,can):
    for i in range(can):
        num=random.randint(1,100)
        li.append(num)
    return li


def mayor(lista):
    if len(lista) == 0:
        print('error')
    else:
        mayor = lista[0]
        for i in range(1,len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
    
li=[] 
can=random.randint(5,20)
li=llenarli(li,can)
print(li)
print(mayor(li)) 