#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):


    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
