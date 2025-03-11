def media(a,b):
    sum=a+b
    m=sum/2
    
    return m
print(media(5,8))

def varianzas(c,d):
    v=((c-media(c,d))**2)+((d-media(c,d))**2)
    v=v/2
    
    return v
print(varianzas(5,8))

def desviacion(d,f):
    des=varianzas(d,f)
    des=des**(1/2)
    return des
print(desviacion(5,8))