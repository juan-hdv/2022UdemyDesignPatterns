"""
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class <code>Shape</code>; a constructor that takes an interface <code>Renderer</code>; 
defined as 
class Renderer(ABC): 
    @property
    def what_to_render_as(self):
        return None

As well as <code>VectorRenderer</code>; and <code>RasterRenderer</code> classes.

Each inheritor of the <code>Shape</code> abstract class should have a constructor that takes a <code>Renderer</code>; 
such that, subsequently, each constructed object's <code>__str__()</code>; 
operates correctly, for example,
<code>str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"</code>
"""
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

from abc import ABC

class Renderer(ABC):
    @property
    def render_as(self):
        pass

class VectorRenderer(Renderer):
    def __init__(self) -> None:
        super().__init__()

    @property
    def render_as(self):
        return "lines"

class RasterRenderer(Renderer):
    def __init__(self) -> None:
        super().__init__()

    @property
    def render_as(self):
        return "pixels"

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class Shape:
    def __init__(self, name: str, renderer:  Renderer):
        self.name = name
        self.renderer = renderer

    def __str__(self) -> str:
        return "Drawing " + self.name + " as " + self.renderer.render_as

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__('Triangle', renderer)

class Square(Shape):
    def __init__(self, renderer):
        super().__init__('Square', renderer)

print (str(Triangle(RasterRenderer())))
print (str(Triangle(VectorRenderer())))
print (str(Square(RasterRenderer())))
print (str(Square(VectorRenderer())))
