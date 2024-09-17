import pygame   
pygame.init()

screen = pygame.display.set_mode((500,500))


class Rectangle():
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.surface = screen

    def drawRect(self):
        self.rect_draw = pygame.draw.rect(self.surface, self.color, self.position)

class Circle():
    def __init__(self, color, position, radius):
        self.color = color
        self.position = position
        self.radius = radius
        self.surface = screen

    def drawCircle(self):
        self.circle_draw = pygame.draw.circle(self.surface, self.color, self.position, self.radius)

blueRect = Rectangle("red", (50, 100, 50, 150))
blueRect.drawRect()


yellowCircle = Circle("yellow", (75, 75), 20)
yellowCircle.drawCircle()

blackRect = Rectangle("black", (70, 70, 10, 30))
blackRect.drawRect()

while True:
    pygame.display.update()