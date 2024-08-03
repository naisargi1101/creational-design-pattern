'''
Abstract Factory Design Pattern: 
    - The abstract factory design pattern is a creational pattern that provides an interface for creating 
    families of related or dependent objects without specifying their concrete classes. 
    - It allows for the creation of objects that follow a particular theme, ensuring that related products 
    are used together.
'''

class Circle:
    def draw(self):
        print('Circle.draw')

class Rectangle:
    def draw(self):
        print('Rectangle.draw')

class Square:
    def draw(self):
        print('Square.draw')

class ShapeFactory:
    def __init__(self, shape_name) -> None:
        self.shape_type = shape_name
    
    def get_shape(self):
        if self.shape_type == 'circle':
            return Circle()
        elif self.shape_type == 'rectangle':
            return Rectangle()
        elif self.shape_type == 'square':
            return Square()
        return None

if __name__ == '__main__':
    shape = ShapeFactory('circle')
    shape.get_shape().draw()
    shape = ShapeFactory('rectangle')
    shape.get_shape().draw()
    shape = ShapeFactory('square')
    shape.get_shape().draw()
    shape = ShapeFactory('triangle')
    print(shape.get_shape())
