#imprirmir la cantidad de numeros es su lado opuesto

def opuesto():
    c=0
    num=1
    while num!=0:   
        num=int(input("introduzca el numero Numero: "))
        print(f'El numero es {num*-1}')
        c=c+1
    return c-1


print(opuesto())

def sum_opuesto():
    c=0
    num=1
    sum=0
    while num!=0:   
        num=int(input("introduzca el numero Numero: "))
        sum=sum+num
        c=c+1
        print(f'la suma es{sum}')
    return c-1

print(f'la cantidad de numeros ingresados es{sum_opuesto()}')
