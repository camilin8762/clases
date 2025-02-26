# SOLICITAR NUMEROS
def series():
    num_1=int(input('ingrese un numero'))
    num_2=int(input('ingrese un numero')) 
    if num_1<num_2:
        while  num_1<num_2:
            print(num_1)
            num_1+=1
        print(num_2)
    else:
        while  num_1>num_2:
            print(num_1)
            num_1-=1
        print(num_2)
    return num_1, num_2
series()
