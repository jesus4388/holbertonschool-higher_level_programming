#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aux1 = (0, 0)
    aux2 = (0, 0)
    if len(tuple_b) == 0:
       aux1 = 0, 0
    elif len(tuple_b) == 1:
       aux1 = tuple_b[0], 0
    else:
        aux1 = tuple_b[0], tuple_b[1]
    if len(tuple_a) == 0:
        aux2 = tuple_a[1], 0
    elif len(tuple_a) == 1:
        aux2 = tuple_a[0], tuple_a[1]
    else:
        aux2 = tuple_a[0], tuple_a[1]
    return(aux1[0] + aux2[0], aux1[1] + aux2[1])
