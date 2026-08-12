class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self) -> int:
        return self.width*self.height

    def get_perimeter(self) -> int:
        return 2*(self.width+self.height)

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        ret = []
        for i in range(self.height):
            ret.append('*'*self.width)
        return '\n'.join(ret) + '\n'

    def get_amount_inside(self, other_shape: Rectangle) -> int:
        return int(self.get_area() / other_shape.get_area())

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        self.side = side

    def set_width(self,width):
        self.set_side(width)

    def set_height(self,height):
        self.set_side(height)

    def set_side(self,side):
        self.height = side
        self.width = side
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
