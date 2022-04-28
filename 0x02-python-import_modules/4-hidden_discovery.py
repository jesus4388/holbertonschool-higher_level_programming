#!/usr/bin/python3
import hidde_4
if __name__ == "__main__":
    lis = dir(hidde_4)
    for i in lis:
        if (i[0] != '_' and i[1] != '_'):
            print(f"{i}")
