from turtle import *
import timeit
from math import floor
import random

wn = Screen()     # Creates a playground for turtles
wn.setworldcoordinates(-100,-100,100,100)
wn.delay(1)
t = Turtle()
turs = [(t, 0, 25)]
for i in range(10):
    t = t.clone()
    turs.append((t, 0, random.randrange(1,360)))
                
for t in turs:
    t[0].speed(t[1])
    t[0].shape("circle")
    t[0].color("red")
    t[0].up()
    t[0].setposition(random.randint(-99,100),random.randint(-99,100))
    t[0].left(t[2])
    t[0].shapesize(1, 1, 1)
    
start = timeit.default_timer()

while True: # this "for" loop will repeat these functions 500 times
    for myt in turs:
        t = myt[0]
        a = t.heading()
        if t.position()[0] > 100 : #right    
            if a > 180:#down
                t.setheading(a - (90-360+a)*2)
            elif a < 180 : #up
                t.setheading(a + 180-2*a)
            print(t.position(), t.heading())
        elif t.position()[1] > 100: #top
            t.setheading(360-a)
            t.setposition(t.position()[0],99.9)
            print(t.position(), 2 * myt[2], t.heading())
        elif t.position()[0] < -100: #left
            if a > 180:#down
                t.setheading(a - (90-360+a)*2)
            elif a < 180 : #up
                t.setheading(a + 180-2*a)
            print(t.position(), 180-2 * myt[2], t.heading())
        elif t.position()[1] < -100: #bottom
            t.setheading(360-a)
            print(t.position(), 2 * myt[2], t.heading())
        t.forward(1)

wn.mainloop()  