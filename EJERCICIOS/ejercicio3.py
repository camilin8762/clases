# entregar notas

n=int(input('ingrese la nota del estudiante'))

if n>=1 and n<=2:
    print('reprobado')
else:
    if n>=3 and n<=4:
        print('suficiente')
    else:
        if n>=5 and n<=6:
            print('aprobado')
        else: 
            if n>=7 and n<=8:
                print('bien')
            else:
                if n>=9 and n<=10:
                    print('muy bien')
                else:
                    print('error')