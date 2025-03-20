import csv
def salariomax():
    with open('c:/Users/Aprendiz/Downloads/employees.csv','r',encoding='utf-8') as li:
        lista=csv.reader(li)
        x=(list(lista))
        del x[0]
        sal=[]
        nom=[]
        diccio={}
        for emple in x:
            sal.append(int(emple[7]))
        for emple in x:
            nom.append(emple[2])
        for i in range(len(nom)):
            diccio[nom[i]] = sal[i]
        salmax=max(sal)
        valor_buscado = salmax
        clav = None
        for clave, valor in diccio.items():
            if valor == valor_buscado:
                clav = clave
                
        return clav,valor_buscado

def salariomin():
    with open('c:/Users/Aprendiz/Downloads/employees.csv','r',encoding='utf-8') as li:
        lista=csv.reader(li)
        x=(list(lista))
        del x[0]
        sal=[]
        nom=[]
        diccio={}
        for emple in x:
                sal.append(int(emple[7]))
        for emple in x:
            nom.append(emple[2])
        for i in range(len(nom)):
            diccio[nom[i]] = sal[i]
        salmin=min(sal)
        valor_buscado = salmin
        clav = None
        for clave, valor in diccio.items():
            if valor == valor_buscado:
                clav = clave
        return clav,valor_buscado

mayor=salariomax()
menor=salariomin()

print(mayor)
print(menor)

def ordenar():
    with open ('c:/Users/Aprendiz/Downloads/employees.csv','r',encoding='utf-8') as li:
        lista=csv.reader(li)
        x=list(lista)
        del x[0]
        x.sort()
        for emp in x:
            print(emp)
        
ordenado=ordenar()

