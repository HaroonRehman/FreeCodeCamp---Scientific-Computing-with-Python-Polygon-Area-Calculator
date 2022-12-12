import Rectangle

class Square(Rectangle.Rectangle):

    def __init__(self,s):
        super().__init__(s,s)
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self,s):
        self.width = s
        self.height = s









