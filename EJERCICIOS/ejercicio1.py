# deteerminar igualdad de nuneros

print ('\n+++++++++ determinar igualdad de numeros +++++++++')

#intruducir mumeros

num_1 =int(input('introdusca el primer numero: '))
num_2 =int(input('introdusca el segundo numero: '))
num_3 =int(input('introdusca el tercer numero: '))

#determinar la igualdad

if num_1==num_2 and num_2==num_3 and num_3==num_1:
    print ('\n los tres nunmeros son iguales')
elif num_1==num_2 :
    print ('\n hay dos numeros iguales ')
elif num_2==num_3 :
    print ('\n hay dos numeros iguales ')
elif num_3==num_1:  
    print ('\n hay dos numeros iguales ')
else:
    print ('todos los numeros son distintos')