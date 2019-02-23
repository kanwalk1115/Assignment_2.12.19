from graphics import *
win = GraphWin('Window 1', 600, 600)

point1 = Point(300,300)

circle = Circle(point1,200)
circle.setOutline('black')
circle.setFill('yellow')
circle.draw(win)

point2 = Point(200,250)

circle2 = Circle(point2, 50)
circle2.setOutline('black')
circle2.setFill('black')
circle2.draw(win)

point3 = Point(400,250)

circle3 = Circle(point3, 50)
circle3.setOutline('black')
circle3.setFill ('black')
circle3.draw(win)

point4 = Point(200,400)
point5 = Point(400,400)

line = Line(point4 ,point5)
line.draw(win)



input("press any key to exit...")
#
