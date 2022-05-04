#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    suma = 0
    for i in my_list:
        if i not in new:
            new.append(i)
    for j in new:
        suma = suma + j
    return(suma)
