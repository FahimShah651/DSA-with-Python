import math

class Circle:
    def __init__(self, radius=1):
      self.radius = radius
    def getPerimeter(self):
      return 2*self.radius*math.pi
    def getArea(self):
      return self.radius*self.radius*math.pi
    def setRadius(self, radius):
      self.radius = radius


c = Circle(3)
print("The value of radius is", c.radius)
print("perimeter of the circle is " ,{c.getPerimeter()})
