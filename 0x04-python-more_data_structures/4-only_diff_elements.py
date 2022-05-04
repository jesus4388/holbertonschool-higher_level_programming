#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    delete = []
    for i in set_1:
        new.append(i)
    for j in set_2:
        if j not in new:
            new.append(j)
        else:
            delete.append(j)
    for i in new:
        for j in delete:
            if i == j:
                new.remove(i)
    return new
