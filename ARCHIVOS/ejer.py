import json

with open ('ARCHIVOS/employees.json','r',encoding='utf-8') as empl:
    data=json.load(empl)
    

sal=[]
for i in data:
    sal.append(int(i['SALARY']))
    
print(sal)

def media (lista): 
    suma = 0
    for i in lista:
        suma = suma + i
        m= suma / len(lista)
    return  m

med=media(sal)

print(f'el promedio salarial es : {med}')

emple=[]

for i in data:
    if i['DEPARTMENT_ID']=='50':
        emple.append(i)

for i in emple:
    print(i['FIRST_NAME'],i['LAST_NAME'])
    

new_empl={
        "EMPLOYEE_ID": input("ingrese el ID del empleado :"),
        "FIRST_NAME": input( "ingrese el primer nombre del empleado :"),
        "LAST_NAME": input( "ingrese el primer apellido del empleado :"),
        "EMAIL": input("ingrese el EMAIL del empleado :"),
        "PHONE_NUMBER": input("ingrese el numero del empleado :"),
        "HIRE_DATE": input("ingrese fecha de contratacion del empleado en año/mes/dia :"),
        "JOB_ID": input("ingrese el ID del trabajo :"),
        "SALARY": input("ingrese el salario del empleado :"),
        "COMMISSION_PCT": input("ingrese comision PCT del empleado :"),
        "MANAGER_ID": input("ingrese el ID del manager del empleado :"),
        "DEPARTMENT_ID": input("ingrese el ID del departamento del empleado :")
    }

data.append(new_empl)



with open ('ARCHIVOS/employees.json','w',encoding='utf-8') as empl:
    data=json.dump(data,empl)
    


