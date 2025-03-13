import random
def llenarli(li):
    can=random.randint(5,20)
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

def par(lista):
    tam=len(lista)
    
    if tam%2 != 0:
        m=media(lista)
        lista.append(int(m))
        tam=len(lista)
        print(lista)
    r1=lista[:int(tam/2)]
    r2=lista[int(tam/2):]
    
    return r1 , r2
li=[]
li=llenarli(li)
print(li)

print(par(li))

def prodlista(lista):
    r1=par(lista)
    
    suma=0
    for i in r1:
        suma +=i
        pro=suma/len(r1)
        
    
    return pro 

print(prodlista(li))