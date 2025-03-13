from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i
print(data)
try:
    bf = open('TAREAS/file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))