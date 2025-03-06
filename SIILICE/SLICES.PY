import random
def llenarli(li):
    can=random.randint(5,20)
    for i in range(can):
        num=random.randint(1,100)
        li.append(num)
    return li
li=[]
li=llenarli(li)
print(li)
def rebanada(li,i,x):
    if i>len(li) or x<len(li)*-1:
        return 'fuera de rango'
    else:
        return li[i:x]
    

i=int(input('ingrese el primer valor de la rebanada'))
x=int(input('ingrese el primer valor de la rebanada'))

reb=rebanada(li,i,x)

print(reb)