# determinar las cifras de un numero 

print('\n ++++++++++++ vamos a determinar cifras +++++++++++')

num=int(input('por favor ingrese el numero'))

# determinar las cifras

if num>=0 and num<=9:
    print(f'\n el {num} tiene una cifra ')
elif num>=10 and num<=99:
    print(f'\n el {num} tiene dos cifras ')
elif num>=100 and num<=999:
    print(f'\n el {num} tiene tres cifras ')
elif num>=1000 and num<=9999:
    print(f'\n el {num} tiene cuatro cifras ')
elif num>=10000:
    print(f'\n el {num} excede el limite' )
