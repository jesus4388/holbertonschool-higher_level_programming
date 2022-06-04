#!/usr/bin/python3
'# class Square that inherits from Rectangle'


from models.rectangle import Rectangle
'# import rectangle'


class Square(Rectangle):
    '# class Square'


    def __init__(self, size, x=0, y=0, id=None):
        '# class constructor'

        super().__init__(size, size, x, y, id)
        '# Call the super class'

    '# overloading __str__ method'
    def __str__(self):
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    '# method size'
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    '# public method that assigns attributes'
    def update(self, *args, **kwargs):
        flag = 0
        if len(args) < 1:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        else:
            for i in args:
                if flag == 0:
                    self.id = i
                if flag == 1:
                    self.size = i
                if flag == 2:
                    self.x = i
                if flag == 3:
                    self.y = i
                flag += 1

    '# returns the dictionary representation of a Rectangle'
    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
