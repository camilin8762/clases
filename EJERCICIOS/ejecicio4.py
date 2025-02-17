def divisores(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
            

num=int(input("Ingrese un número: "))

divisores(num)