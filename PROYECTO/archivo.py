import csv
def cantidad_colombianos():
    with open('PROYECTO/personas.csv',"r",encoding=('utf-8')) as archivo:
            con=0
            paises=[]
            lector = csv.reader(archivo)
            x=(list(lector))
            del x[0]
            dicion={}
            for persona in x:
                paises.append(persona[0])
                
            for pa in paises:
                if pa in dicion:
                    dicion[pa] += 1
                else:
                    dicion[pa] = 1
                    
            for i in dicion:
                print(f'en {i} : hay {dicion[i]} colombianos')
            

cantidad_colombianos()

def ciudad_colombianos():
    with open('PROYECTO/personas.csv',"r",encoding=('utf-8')) as archivo:
            con=0
            ciudad=[]
            lector = csv.reader(archivo)
            x=(list(lector))
            del x[0]
            dicion={}
            for persona in x:
                ciudad.append(persona[2])
                
            for k in ciudad:
                if k in dicion:
                    dicion[k] += 1
                else:
                    dicion[k] = 1
                    
            for i in dicion:
                print(f'en {i} : hay {dicion[i]} colombianos')

#ciudad_colombianos()               
        
def max_min_colombianos():
    with open('PROYECTO/personas.csv',"r",encoding=('utf-8')) as archivo:
            con=0
            paises=[]
            lector = csv.reader(archivo)
            x=(list(lector))
            del x[0]
            dicion={}
            for persona in x:
                paises.append(persona[0])
                
            for pa in paises:
                if pa in dicion:
                    dicion[pa] += 1
                else:
                    dicion[pa] = 1 
            cant=[]
            for i in dicion:
                num=dicion[i]
                cant.append(num)
                
            max_col=max(cant)
            min_col=min(cant)
            
            valor_buscado_max = max_col
            clav_1 = None
            for clave, valor in dicion.items():
                if valor == valor_buscado_max:
                    clav_1 = clave
                    
            valor_buscado_min = min_col
            clav_2 = None
            for clave, valor in dicion.items():
                if valor == valor_buscado_min:
                    clav_2 = clave
            print(f'el pais con mas colombianos es {clav_1} con {valor_buscado_max}')
            print(f'el pais con menos colombianos es {clav_2} con {valor_buscado_min}')
                    
max_min_colombianos()
print('-'*50)

def estado_civil():
    with open("PROYECTO/personas.csv", "r", encoding="utf-8") as datos:
        data = csv.reader(datos)
    
        datos = list(data)
        datos.pop(0)
        ape = []

    for i in datos:
        ape.append(i[9])  

    con_est = {}

    for i in ape:
        if i in con_est:
            con_est[i] += 1
        else:
            con_est[i] = 1

    print("Personas Por Estado Civil:")
    for edad in sorted(con_est.keys()):
        print(f"Estado Cvil {edad}: {con_est[edad]} personas")

estado_civil()
print('-'*50)

def emigrantes():
    with open("PROYECTO/personas.csv", "r", encoding="utf-8") as datos:
        data = csv.reader(datos)
    
        datos = list(data)
        datos.pop(0)
        ape = []

    for i in datos:
        ape.append(i[5])  

    con_eda = {}

    for i in ape:
        if i in con_eda:
            con_eda[i] += 1
        else:
            con_eda[i] = 1

    print("Personas Por Edad:")
    for edad in sorted(con_eda.keys()):
        print(f"Edad {edad}: {con_eda[edad]} personas")

emigrantes()
print('-'*50)

def Profeciones():
    with open("PROYECTO/personas.csv", "r", encoding="utf-8") as datos:
        data = csv.reader(datos) 
        datos = list(data)
        datos.pop(0) 
        con_pais = {}

        for i in datos:
            pais = i[0]    
            profesion = i[7]  

            if pais not in con_pais:
                con_pais[pais] = {}
            if profesion not in con_pais[pais]:
                con_pais[pais][profesion] = 1
            else:
                con_pais[pais][profesion] += 1

    for pais in sorted(con_pais.keys()):
        print(f"\nPaís: {pais}")
        print("Profesiones:")
        for profesion, cantidad in sorted(con_pais[pais].items()):
            print(f" profecion : {profesion}: {cantidad} personas")

Profeciones()