class Shape:
    def __init__(self,name):
        self.name=name

    def draw(self):
        print(f"drawing a generic shape: {self.name}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius=radius
    def draw(self):
        print(f"drawing a Circle: {self.name} with radius {self.radius}")

class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width=width
        self.height=height

    def draw(self):
        print(f"drawing Rectangle: {self.name} with area {self.width * self.height}") 

class Triangle(Shape):
    def __init__(self,length,height):
        super().__init__("Triangle")
        self.length=length
        self.height=height

    def draw(self):
        print(f"drawing Triangle: {self.name} with area {0.5 * self.length * self.height}") 


def main():
    s1=Circle(5)
    s2=Rectangle(4,6)
    s3=Triangle(4,8)
    s1.draw()
    s2.draw()
    s3.draw()
    print("New update here!")
main()