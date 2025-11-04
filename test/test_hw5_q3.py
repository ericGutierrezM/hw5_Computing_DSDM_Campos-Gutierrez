from hw5 import Triangle, Rectangle, Circle
import math

def test_triangle():
    t = Triangle(5, 5, 5, 5.5)
    assert t.compute_perimeter() == 15
    assert t.compute_surface() == 13.75

def test_rectangle():
    r = Rectangle(10, 5)
    assert r.compute_perimeter() == 30
    assert r.compute_surface() == 50

def test_circle():
    c = Circle(3)
    assert c.compute_perimeter() == 2 * math.pi * 3
    assert c.compute_surface() == math.pi * 3 ** 2