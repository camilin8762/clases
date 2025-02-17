def sum_num():     
    c=0
    num=1
    sum=0
    while num!=0:
        if num<0:
            break 
        else:
            num=int(input("introduzca el numero Numero: "))
            if num<0:
                break
            else:
                sum=sum+num
                c=c+1
    return sum
    
print(f'la suma de los numeros es: {sum_num()}')