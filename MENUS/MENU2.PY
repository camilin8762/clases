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

def suma (lista): 
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

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

def ordenar_ascen(lista):
    inter=True
    
    while inter:
        inter=False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]: 
                inter=True
                lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista

def ordenar_descen(lista):
    inter=True
    
    while inter:
        inter=False
        for i in range(len(lista)-1):
            if lista[i]<lista[i+1]: 
                inter=True
                lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista


print('seleccione una de las siguientes opciones: ')
print(' 1- ver la lista')
print(' 2- suma de toda la lista')
print(' 3- ver promedio de la lista')
print(' 4- ver el valor mayor de la lista')
print(' 5- ver el valor menor de la lista')
print(' 6- ver la lista de manera ascendente')
print(' 7- ver la lista de manera descendente')
print(' 8- ver la madiana de la lista')

sel=int(input('opcion :'))

match sel:
    case 1 :
        li=[]
        can=int(input('ingrse el tamaño de la lista:  '))
        li=llenarli(li,can)
        print('\n',li)
    case 2 :
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print(sum(li))
    case 3  :
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print(media(li))
    case 4:
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print(mayor(li))
    case 5:
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print(menor(li))
    case 6:
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print( ordenar_ascen(li))
    case 7:
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print( ordenar_descen(li))
    case 8 :
        li=[]
        can=int(input('ingrse el tamaño de la lista: '))
        li=llenarli(li,can)
        print(mediana(li))
        
    case _:
        print('opcion invalida' )