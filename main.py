from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):  # is-a relationship: subclasses Rectangle

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(
            self.point1.x,
            self.point1.y
        )
        canvas.pendown()

        # relative move
        canvas.forward(
            self.point2.x - self.point1.x
        )
        canvas.left(90)
        canvas.forward(
            self.point2.y - self.point1.y
        )
        canvas.left(90)
        canvas.forward(
            self.point2.x - self.point1.x
        )
        canvas.left(90)
        canvas.forward(
            self.point2.y - self.point1.y
        )


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Create rectangle object
gui_rectangle = GuiRectangle(
    Point(
        randint(0, 100),
        randint(0, 100)
    ),
    Point(
        randint(101, 200),
        randint(101, 200)
    )
)

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      gui_rectangle.point1.x, ",",
      gui_rectangle.point1.y, "and",
      gui_rectangle.point2.x, ",",
      gui_rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(
                float(input("Guess x: ")),
                float(input("Guess y: "))
)
user_area = float(
                input("Guess rectangle area: ")
)

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(gui_rectangle))
print("Your area was off by: ", gui_rectangle.area() - user_area)

canvas = turtle.Turtle()                # initialize turtle
gui_rectangle.draw(canvas=canvas)       # draw rectangle
user_point.draw(canvas)                 # draw point

# turtle.done()
turtle.Screen().exitonclick()           # wait for click
