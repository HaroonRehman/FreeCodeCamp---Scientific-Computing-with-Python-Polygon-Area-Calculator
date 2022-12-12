import Rectangle , Square


# Rectangle

rect = Rectangle.Rectangle(10,5)

print(rect.get_area())
rect.sets_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# Square

sq = Square.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

#little tweak rect

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

