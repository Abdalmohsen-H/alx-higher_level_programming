#!/usr/bin/python3
'''
create class square inherits from rectangle
a. Hesham
'''


from models.rectangle import square


class Square(Rectangle):
    '''
    create class square inherits from rectangle
    A. Hesham
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor to intialize objects(instances)
        of suare class
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' repr for str() and print() '''
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    def __repr__(self):
        ''' repr for str() and print() '''
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    @property  # getter
    def size(self):
        ''' public attribute size getter - A. hesham'''
        return self.width

    @size.setter
    def size(self, value):
        ''' public attribute size setter - A. hesham'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' update attibutes using args or kwargs'''
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for idx in range(len(args)):
                setattr(self, attrs[idx], args[idx])
        elif kwargs:
            # print(f"kwargs : {kwargs}")
            for ky, val in kwargs.items():
                setattr(self, ky, val)
