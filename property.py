#property is a decorator that allows defining methods in a class that can be accessed like attributes.
class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def width(self):
        return f"{self._width:.1f} cm"
    @property
    def height(self):
        return f"{self._height:.1f} cm"
    @width.setter
    def width(self,new_width):
        if new_width >=0:
            self._width=new_width
        else:
            print("Width cannot be negative.")
    @height.setter
    def height(self,new_height):
        if new_height >=0:
            self._height=new_height
        else:
            print("Height cannot be negative.")
rectangle1=Rectangle(10,5)
rectangle1.width=15
rectangle1.height=7
print(rectangle1.width)
print(rectangle1.height)