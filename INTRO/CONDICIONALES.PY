
num_1=int(input("ingrese un numero: "))
num_2=int(input("ingrese un numero: "))

if num_1==num_2:
    print("los numeros son iguales: ")
elif num_1<num_2:
    print("los numeros van en orden ascendete: ")
elif num_1>num_2:
    print("los numeros van en orden descendente: ") 
else:
    print('Error: invalid ❌❌❌')



est=input("ingrese su estrato: ")

match est:
    case 1:
        print('estrato 1')
    case 2:
        print('estrato 2')
    case 3:
        print('estrato 3')
    case 4:
        print('estrato 4')
    case 5:
        print('estrato 5')
    case 6:
        print('estrato 6')    