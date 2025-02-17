def sumDivisores(num):
    sum=0
    for i in range(1,num):        
        if num%i==0:
            sum+=i
    return sum



def primos(num):
    if sumDivisores(num)==1:
        return print("es primo")
    else: 
        return print("no es primo")

num=int(input("ingrese el numero: "))
primos(num)