from turtle import *
le = left 
ri = right 
forw = forward
speed(2)
pensize(7)
color("white")
bgcolor("black")
screensize(500, 300)

penup()
le(180)
forw(200)
le(180)
pendown()

begin_fill()
for i in range(8):
    forw(100)
    ri(55)
    forw(100)
    le(120)
    
color("#eaeaea")
end_fill()



done()
