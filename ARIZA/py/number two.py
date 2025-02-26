def sum_opuesto():     
    c=0
    num=1
    sum=0
    while num!=0:   
        num=int(input("introduzca el numero Numero: "))
        sum=sum+num
        c=c+1
        
    return sum,c-1
print(f'la suma de los numero y la cantidad es{sum_opuesto()}')


def promedio():
    c=0
    num=1
    sum=0
    while num!=0:   
        num=int(input("introduzca el numero Numero: "))
        sum=sum+num
        c=c+1
    pro=sum/(c-1)
    return pro

print(f'El promedio de los numeros ingresados es{promedio()}')