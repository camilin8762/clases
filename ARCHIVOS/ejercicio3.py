import csv
import json

with open('c:/Users/Aprendiz/Downloads/customers.csv','r',newline='',encoding='utf-8')as micsv:
    readers=csv.DictReader(micsv)
    datacsv=[i for i in readers]
print(datacsv)

with open('ARCHIVOS/clientes.json','w',encoding='utf-8') as mijson:
    json.dump(datacsv,mijson,indent=4)