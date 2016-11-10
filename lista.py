#-*-coding:utf-8-*-

import random

"""
class Lista(object):
    # Lista para definir memoria en uso y memoria disponible
    def __init__(self):
        # Inicializa la lista
        self.lista = []

    def

"""
# lista = [[position, status, size]]   >>>>> H stands for hollow(free memory)
lista = [[0, "H", 255]]

diez_procesos = [[random.randint(0,511), "Proceso %d" %(x), random.randint(1,20),] for x in range(10)]

#for x in range(20):
#    print random.randint(0,10)

for proc in range(10):
    print proc
    proc_address = random.randint(0,255)
    proc_size = random.randint(1,20)
    for element in lista:
        if element[0] == "H":
            pass
            if element[0] <= proc_address <= element[0]+element[2]:
                element2 = [proc_address, str(proc), proc_size]
        else:
            pass

        if element[0] < proc_address:
            if elemento[0] + elemento[2] < proc_address:
                pass


print diez_procesos
