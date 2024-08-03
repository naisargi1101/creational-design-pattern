'''
Factory Design Pattern: 
    - The factory design pattern is a creational pattern that provides an interface for creating objects 
    in a superclass but allows subclasses to alter the type of objects that will be created. 
    - It promotes loose coupling by eliminating the need to bind application-specific classes into the code.
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

class Shape:
    shapes = {
        'circle': Circle,
        'rectangle': Rectangle,
        'square': Square
    }

    @staticmethod
    def get_shape(shape_type):
        if shape_type in Shape.shapes:
            return Shape.shapes[shape_type]()
        return None

if __name__ == '__main__':
    shape = Shape.get_shape('circle')
    shape.draw()
    shape = Shape.get_shape('rectangle')
    shape.draw()
    shape = Shape.get_shape('square')
    shape.draw()
    shape = Shape.get_shape('triangle')
    print(shape)
