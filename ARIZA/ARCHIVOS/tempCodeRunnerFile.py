def ordenar():
    with open ('c:/Users/Aprendiz/Downloads/employees.csv','r',encoding='utf-8') as li:
        lista=csv.reader(li)
        
        x=list(lista)
        
        del x[0]
        
        print(x)
        
ordenar()