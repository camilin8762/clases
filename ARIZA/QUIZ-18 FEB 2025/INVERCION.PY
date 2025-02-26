def invercion():
    d=int(input('ingrese la cantidad de dinero que desea invertir'))
    i=int(input('igrese el porcentaje de la invercion'))
    a=int(input('igrase la cantidad de años que desea invertir'))
    c=0
    g=d*(i/100)
    gn=d+g
    ga_=0
    while c<a:
        ga_=ga_+gn
        g=ga_*(i/100)
        gn=ga_+g
        c+=1
    print(f'el total de su inversion seria{ga_}')
    return ga_
invercion()
