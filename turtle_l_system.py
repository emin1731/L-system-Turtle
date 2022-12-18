import numpy as np
import turtle 

 
# Screen Settings  *************************************
width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
# ******************************************************






class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom      # initiator
        self.state = axiom      # string with a set of commands for the fractal (in the beginning it is the initiator)
        self.width = width      # width of line
        self.t = t              # the turtle itself
        self.t.pensize(self.width)
        self.length = length    # length of one linear segment of a curve
        self.angle = angle      # fixed angle of rotation
        self.rules = {}         # a dictionary for storing the rules for generating curves
    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()
    def draw_turtle(self, start_pos, start_angle):
        # ***************
        turtle.tracer(1, 0)     
        self.t.up()             
        self.t.setpos(start_pos)    
        self.t.seth(start_angle)    
        self.t.down()              
        # ***************
        turtle_stack = []
 
        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == "[":
                turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))
            elif move == "]":
                xcor, ycor, head, w = turtle_stack.pop()
                self.set_turtle((xcor, ycor, head))
                self.width = w
                self.t.pensize(self.width)
 
        turtle.done()
    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value
    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())
            self.state = self.state.upper()
    



# System Params  ***************************************************
t = turtle.Turtle()
t.ht()
t.speed(1)
pen_width = 2       # толщина линии рисования (в пикселах)
f_len = 5          # длина одного сегмента прямой (в пикселах)
angle = 25          # фиксированный угол поворота (в градусах)
axiom = "F"   # аксиома
# ******************************************************************





# harter-heighway dragon curve******************************************

angle = 90 
axiom = "FX"
 
l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
l_sys.add_rules(("FX", "FX+FY+"), ("FY", "-FX-FY"))
l_sys.generate_path(10)
l_sys.draw_turtle( (0, 0), 0)




# hilbert curve*******************************************************

# angle = 90     
# axiom = "X"
 
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("X", "-YF+XFX+FY-"), ("Y", "+XF-YFY-FX+"))
# l_sys.generate_path(5)
# l_sys.draw_turtle( (0, 0), 0)




# tree *******************************************************
# angle = 25
# axiom = "F"
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F[+F]F[-F]F"))
# l_sys.generate_path(4)
# l_sys.draw_turtle( (0, -400), 90)