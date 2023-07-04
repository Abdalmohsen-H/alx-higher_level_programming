#!/usr/bin/python3
''' this is a module for a class
by A. Hesham
for rectangle task 8
'''


class Rectangle:
    '''This is a Rectangle class '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        ''' intialize instance (object) of class
        Rectangle
        doc description for intialization function
        __width and __hight are private
        '''
        self.__width = 0  # intialize private
        self.__height = 0  # intialize private
        self.width = width  # change value via setter
        self.height = height  # change value via setter
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''width getter
        doc description for function
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height  getter
        doc description for function
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' instance method to
        return are of rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' instance method to return
        perimeter of regtangle (mo7eet)
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ print rectangle using #'s in stdout
        and print empty string
        if width or height is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for Vunit in range(self.__height):
                for Hunit in range(self.__width):
                    print("{}".format(self.print_symbol), end="")
                if Vunit < self.__height - 1:
                    print("\n", end="")
        return ""

    def __repr__(self):
        ''' __repr__ magic method of class rectangle '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        ''' __del__ magic method of class rectangle
        to delete an instance when it called
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' static method to check which
        rect is bigger
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
