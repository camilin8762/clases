def sumDivisores(num):
    sum=0
    for i in range(1,num):        
        if num%i==0:
            sum+=i
    return sum

def Perfect(num):
    if num==sumDivisores(num):
        return print(f'{num} es perfecto')
    else:
        return print(f'{num} no es perfecto')   
    
num=int(input("Ingrese un número: "))

Perfect(num)