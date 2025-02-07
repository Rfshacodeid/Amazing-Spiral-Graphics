import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
turtle.colormode(255)

n = 100  
h = 0

def draw_spiral():
    global h
    i = 0
    growing = True
    max_size = 200  
    
    while True:  
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 1 / n
        t.color(int(c[0] * 255), int(c[1] * 255), int(c[2] * 255))
        t.forward(i * 2)
        t.right(91)
        t.forward(i * 2)
        t.right(91)
        
        if growing:
            i += 1  
            if i >= max_size:
                growing = False  
        else:
            i -= 1  
            if i <= 0:
                growing = True  

draw_spiral()

turtle.done()