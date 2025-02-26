def cuadratica ():
    a = int(input('ingrese a'))
    b = int(input('ingrese b'))
    c = int(input('ingrese c'))
    if a == 0 :
        print('indeterminado')
    else:
        xp = int((b**2-(4*(a*c))))
        if xp<0:
            print('indeterminado')
        else:
            xp = int(xp**(1/2))
            xp = int(((b*-1)+xp)/(2*a))
        print(xp)
    if a == 0 :
        print('indeterminado')
    else:
        xn =int( (b**2-(4*(a*c))))
        if xn<0:
            print('indeterminado')
        else:
            xn =int(xn**(1/2))
            xn =int(((b*-1)-xn)/(2*a))
        print(xn)

cuadratica()