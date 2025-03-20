li=[]

for i in range(11):
    li.append(i*10)

print(li)

def llenarli(li,can):
    for i in range(can):
        num=(int(input('ingrese numero')))
        li.append(num)
    return li

vec=[]
vec=llenarli(vec,5)
print('-'*35)
print(vec)

