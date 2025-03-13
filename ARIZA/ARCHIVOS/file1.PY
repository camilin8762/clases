def palabra():
    with open ('ARCHIVOS/himno.txt' , 'rt',encoding='utf-8') as him :
            con=0
            pal=input('ingrese la palabra que desea buscar: ')
            no=him.read().lower()
            sep=no.split()
            for j in sep:
                if j == pal:
                    con+=1
            if con>0:
                return f'la palabra si se encuentra y se repite {con} de veces'
            else:
                return 'la palabra no se encuentra'

print(palabra())