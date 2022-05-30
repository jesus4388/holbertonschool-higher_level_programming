#!/usr/bin/python3
'# the object is an instance of a class that\
        inherited (directly or indirectly)'


def inherits_from(obj, a_class):
    '# verification'

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
