import json
import csv

with open('ARCHIVOS/employees.json','r',encoding='utf-8') as empl:
    data=json.load(empl)
    
headers=data[0].keys()

with open('ARCHIVOS/empleados.csv','w') as micsv:
    
    escrito= csv.DictWriter(micsv,headers)
    escrito.writeheader()
    escrito.writerows(data)