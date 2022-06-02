#!/usr/bin/python3
'# returns a list of lists of integers\
        representing the Pascal’s triangle'


def pascal_triangle(n):
    '# function triangle'

    if n <= 0:
        return []
    else:
        lists = []
        for i in range(n):
            row = [1]
            if i > 0:
                for x in range(i):
                    row.append(sum(lists[-1][x:x+2]))
            lists.append(row)
        return lists
