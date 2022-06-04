#!/usr/bin/python3
'# class Rectangle that inherits from Base'


from models.base import Base
'# import class base'


class Rectangle(Base):
    '# class rectangle'

    def __init__(self, width, height, x=0, y=0, id=None):
        '# class constructor'

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)
        '# call the super class'

    '# validation method width'
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    '# validation method height'
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    '# validation method x'
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    '# validation method y'
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    '# public method area'
    def area(self):
        return self.__width * self.__height

    '# public method that prints in stdout #'
    def display(self):
        for line in range(self.__y):
            print()
        for line1 in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for char in range(self.__width):
                print('#', end="")
            print()

    '# overriding the str method'
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    '# print in stdout the rectangle isinstance with #'
    def update(self, *args, **kwargs):
        flag = 0
        for i in args:
            if flag == 0:
                self.id = i
            if flag == 1:
                self.__width = i
            if flag == 2:
                self.__height = i
            if flag == 3:
                self.__x = i
            if flag == 4:
                self.__y == i
            flag += 1
        if len(args) < 1:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
    '# assign an argument to each attribute'
    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}
