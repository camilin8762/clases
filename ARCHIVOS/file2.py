def nombres():
    with open('ARCHIVOS/data.txt','rt',encoding='utf-8') as dic:
        con=0
        tam=dic.readlines()
        while con<len(tam):
            lista=tam[con].split(',')
            print (lista[0])
            con+=1

