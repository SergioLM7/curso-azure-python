class Square:
    def __init__(self, w, h):
        self.__height = h;
        self.__width = w;
    
    def set_side(self, new_side):
        self.__height = new_side;
        self.__width = new_side;
    
    def isSquare(self):
        if self.__height == self.__width:
            return True;
        else:
            return False;

    @property
    def height(self):
        return self.__height;

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value;
        else:
            raise Exception("Value needs to be 0 or larger");



try:
    square = Square(3,3);
    #square.height = 34;
    print(square.isSquare());
    print(square.height);
except Exception as err:
    print(err)
