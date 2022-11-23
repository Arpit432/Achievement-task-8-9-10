
print("Enter the length and width, to calculate perimeter and area od rectangle")

l=(int(input("Enter the length of the rectangle: ")))
w=(int(input("Enter the width of the rectangle: ")))

class Rectangle():
    def __init__(self, l, w):
        self.l = length
        self.w  = width

    def rectangle_area(self):
        return self.l*self.w
        
    def rectangle_perimeter(self):
        return 2*self.l*self.w

Rectangle = Rectangle(l, w)
print("The area of Rectangle is : ", Rectangle.rectangle_area(),"cm^2.")
print("The Perimeter of Rectangle is : ", Rectangle.rectangle_perimeter(),"cm.")