

def menor(lista):
    if len(lista) == 0:
        return None
    else:
        men = lista[0]
        for i in range(1,len(lista)):
            if lista[i] <  men:
                men = lista[i]
        return men
    
li=[1,2,3,4,5,6,7,8,9,10] 
print(li)
print(menor(li))