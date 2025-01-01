import tkinter as tk
import math

class Canvas():
    def _init_(self, bg, l, w):
        self.bg = bg
        self.length = l
        self.width = w
        self.shapesl = []

    def addit(self, o):
        self.shapesl.append(o)

    def draw(self):
        root = tk.Tk()
        root.title("Shapes on Canvas")

        canvas = tk.Canvas(root, width=self.length, height=self.width, bg=self.bg)
        canvas.pack()

        for shape in self.shapesl:
            shape.draw(canvas)

        root.mainloop()

    def _str_(self):
        out = f'Canvas size is: {self.length} x {self.width}\n'
        out += f'Canvas colour is: {self.bg}\n'
        out += f'SHAPES ON CANVAS:\n'
        out += '--------------------\n'
        for y in range(len(self.shapesl)):
            out += f'{self.shapesl[y]}\n--------\n'
        return out

class Shape(object):
    def _init_(self, nam, ol, bc, p):
        self.name = nam
        self.outline = ol
        self.background = bc
        self.location = p

    def _str_(self):
        return f"Shape name:{self.name}\n{self.outline}\nShape colour:{self.background}\nLocation:{self.location}"

    def draw(self, Canvas):
        pass

class outline():
    def _init_(self, check, thic, col):
        self.check = check
        self.thickness = thic
        self.colour = col

    def _str_(self):
        if self.check:
            return f'Outline present with thickness: {self.thickness} and colour: {self.colour}'
        else:
            return f'Outline not present'

class square(Shape):
    def _init_(self, nam, ol, bc, p, sl):
        super()._init_(nam, ol, bc, p)
        self.length = sl

    def area(self):
        return self.length ** 2

    def _str_(self):
        return f"{super()._str_()}\nArea={self.area()}cm^2\nLength={self.length}cm"

    def draw(self, canvas):
        x, y = self.location.x, self.location.y
        canvas.create_rectangle(x, y, x + self.length, y + self.length, outline=self.outline.colour)

class rectangle(square):
    def _init_(self, nam, ol, bc, p, ln, wd):
        super()._init_(nam, ol, bc, p, ln)
        self.width = wd

    def _str_(self):
        return f"{super()._str_()}\nWidth={self.width}cm"

    def area(self):
        return self.length * self.width

    def draw(self, canvas):
        x, y = self.location.x, self.location.y
        canvas.create_rectangle(x, y, x + self.length, y + self.width, outline=self.outline.colour)

class triangle(Shape):
    def _init_(self, nam, ol, bc, p, p2, p3, ver1, ver2, ver3):
        super()._init_(nam, ol, bc, p)
        self.loc2 = p2
        self.loc3 = p3
        self.vertice1 = ver1
        self.vertice2 = ver2
        self.vertice3 = ver3

    def _str_(self):
        return f"{super()._str_()} vertice1\nLocation:{self.loc2} vertice2\nLocation:{self.loc3} vertice3\nSide1={self.vertice1}cm\nSide2={self.vertice2}cm\nSide3={self.vertice3}cm\nArea={self.area():.4f}cm^3"

    def area(self):
        s = (self.vertice1 + self.vertice2 + self.vertice3) / 2
        a = (s * (s - self.vertice1) * (s - self.vertice2) * (s - self.vertice3))**0.5
        return a

    def draw(self, canvas):
        x1, y1 = self.location.x, self.location.y
        x2, y2 = self.loc2.x, self.loc2.y
        x3, y3 = self.loc3.x, self.loc3.y

        canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline=self.outline.colour)

class Circle(Shape):
    def _init_(self, nam, ol, bc, p, r):
        super()._init_(nam, ol, bc, p)
        self.radius = r

    def area(self):
        return math.pi * (self.radius ** 2)

    def _str_(self):
        return f'{super()._str_()}\nRadius={self.radius}m\nArea={self.area():.4f}m^2'

    def draw(self, canvas):
        x, y = self.location.x, self.location.y
        canvas.create_oval(x, y, x + 2 * self.radius, y + 2 * self.radius, outline=self.outline.colour)

class Oval(Circle):
    def _init_(self, nm, bk, outline, point, rd, rd2):
        super()._init_(nm, bk, outline, point, rd)
        self.min_r = rd2

    def area(self):
        return round((self.radius) * (self.min_r) * math.pi, 3)

    def _str_(self):
        return f'{super()._str_()}\nMinor Radius={self.min_r}m'

    def draw(self, canvas):
        x, y = self.location.x, self.location.y
        canvas.create_oval(x, y, x + 2 * self.radius, y + 2 * self.min_r, outline=self.outline.colour)

class points():
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _str_(self):
        return f'{self.x}x , {self.y}y'



# ... (previous code)

# Increase canvas size
canvas = Canvas("white", 800, 600)

# First set of shapes
square_shape1 = square("Square", outline(True, 2, "blue"), "green", points(50, 50), 100)
rectangle_shape1 = rectangle("Rectangle", outline(True, 1, "red"), "yellow", points(200, 50), 120, 80)

# Coordinates for the first triangle
triangle1_shape1 = triangle("Triangle", outline(True, 2, "purple"), "orange", points(50, 200), points(150, 300), points(250, 200), 100, 80, 60)

# Coordinates for the second triangle
triangle2_shape1 = triangle("Triangle", outline(True, 2, "blue"), "yellow", points(250, 300), points(350, 400), points(450, 300), 120, 90, 70)

# Second set of shapes
circle_shape1 = Circle("Circle", outline(True, 1, "black"), "yellow", points(100, 450), 50)
oval_shape1 = Oval("Oval", outline(True, 2, "brown"), "green", points(250, 450), 60, 40)

# Set different colors, outline thickness, and fill colors for the second set of shapes
square_shape1.outline.colour = "purple"
square_shape1.outline.thickness = 3
square_shape1.background = "cyan"

rectangle_shape1.outline.colour = "green"
rectangle_shape1.outline.thickness = 2
rectangle_shape1.background = "lightblue"

triangle1_shape1.outline.colour = "black"
triangle1_shape1.outline.thickness = 2
triangle1_shape1.background = "gray"

triangle2_shape1.outline.colour = "red"
triangle2_shape1.outline.thickness = 1
triangle2_shape1.background = "pink"

circle_shape1.outline.colour = "brown"
circle_shape1.outline.thickness = 2
circle_shape1.background = "orange"

oval_shape1.outline.colour = "blue"
oval_shape1.outline.thickness = 1
oval_shape1.background = "yellow"

# Add shapes to the canvas
canvas.addit(square_shape1)
canvas.addit(rectangle_shape1)
canvas.addit(triangle1_shape1)
canvas.addit(triangle2_shape1)
canvas.addit(circle_shape1)
canvas.addit(oval_shape1)

# Draw the canvas
canvas.draw()






def main():
    canvas1=Canvas('White',9,12)
    s1=square('Square',outline(True,2.3,'green'),'yellow',points(2,3),4)
    # print(s1)
    r1=rectangle('Rectangle',outline(False,0,None),'skyblue',points(8,7),4,6)
    # print(r1)
    t1=triangle('Triangle',outline(True,3.4,'brown'),'golden',points(1.5,4.7),points(4.7,7.8),points(2.8,6.7),4,6,5)
    # print(t1)
    c1=Circle('Circle',outline(False,0,None),'Orange',points(5.8,3.6),7)
    # print(c1)
    o1 = Oval('Oval', outline(True,1.3,'Red'),'Blue', points(4.8,2.3), 2, 6)
    canvas1.addit(s1)
    canvas1.addit(r1)
    canvas1.addit(t1)
    canvas1.addit(c1)
    canvas1.addit(o1)
    print(canvas1)

main()