#!/usr/bin/python3
'''
create class rectangle inherits from base
a. Hesham
'''


from models.base import Base


class Rectangle(Base):
    ''' create class rectangle inherits from base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor to intialize objects(instances)'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property  # getter
    def width(self):
        ''' private attribute width getter - A. hesham'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' private attribute width setter - A. hesham'''
        if not isinstance(value, int):  # 1st way to check - must use "not"
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property  # getter
    def height(self):
        ''' private attribute height getter - A. hesham'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' private attribute height setter - A. hesham'''
        if type(value) is not (int):  # 2nd way to check
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property  # getter
    def x(self):
        ''' private attribute x getter - A. hesham'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' private attribute x setter - A. hesham'''
        if type(value) not in (int,):  # 3rd don't forget ','
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property  # getter
    def y(self):
        ''' private attribute y  getter - A. hesham'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' private attribute y setter - A. hesham'''
        if type(value) is not (int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        ''' return area of the rectangle'''
        return (self.__width * self.__height)

    def display(self):
        ''' displays the rectangle (draw it) '''
        if self.__width == 0 or self.__height == 0:
            print("", end="")
        else:
            for ydist in range(self.__y):
                print()
            for Vunit in range(self.__height):
                for xdist in range(self.__x):
                    print(" ", end="")
                for Hunit in range(self.__width):
                    print("#", end="")
                if Vunit < self.__height - 1:
                    print("\n", end="")
        print("\n", end="")

    def __str__(self):
        ''' __str of a class '''
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def __repr__(self):
        ''' _repr__ of a class '''
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        ''' update attibutes using args '''
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for idx in range(len(args)):
                setattr(self, attrs[idx], args[idx])
        elif kwargs:
            # print(f"kwargs : {kwargs}")
            for ky, val in kwargs.items():
                setattr(self, ky, val)

    def to_dictionary(self):
        ''' desc : returns dict representation of rect class '''
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }
