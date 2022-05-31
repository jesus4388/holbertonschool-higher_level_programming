#!/usr/bin/python3
'# a class MyInt that inherits from int'


class MyInt(int):
    '# a class MyInt that inherits from int'

    def __init__(self, number):
        self.number = number

        def __eq__(self, other):
            return False
        def __ne__(self, other):
            return True
