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

    @property
    def width(self):
        '# validation method width'
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        '# validation method height'
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        '# validation method x'
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        '# validation method y'
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        '# public method area'
        return self.__width * self.__height

    def display(self):
        '# public method that prints in stdout #'
        for line in range(self.__y):
            print()
        for line1 in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for char in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        '# overriding the str method'
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '# print in stdout the rectangle isinstance with #'
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
                self.__y = i
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

    def to_dictionary(self):
        '# assign an argument to each attribute'
        return f"'x': {self.__x} 'y': {self.__y} 'id': {self.id}\
 'height': {self.__height}, 'width': {self.__width}"
