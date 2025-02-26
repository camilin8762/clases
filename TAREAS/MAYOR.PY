


def mayor(lista):
    if len(lista) == 0:
        print('error')
    else:
        mayor = lista[0]
        for i in range(1,len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
    
li=[1,2,3,4,5,6,7,8,9,10]  
print(li)
print(mayor(li)) 