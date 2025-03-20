#!/usr/bin/python3.13
from shapes import *

p = Point()
s = Square()
r = Rectangle(4,4,4)
t = Triangle("*",10)
d = Diamond("!", 5)

t.draw()
r.draw()
p.draw()
s.draw()
d.draw()
