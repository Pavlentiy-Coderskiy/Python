from turtle import *
num = int(input("Введите колличество вершие звезды: "))
le = left 
ri = right 
forw = forward
pensize(7)
color("white")
bgcolor("black")
screensize(500, 300)
# n - в if, else конструкции 

class Star_edit:
    
    def star(self, spd, lft, frw, righ, lft2, n, *args):
        speed(spd)                #1
        left(lft)              #60
        begin_fill()

        for i in range(n):
            forw(frw)
            ri(righ)
            forw(frw)
            le(lft2)
        color("#eaeaea")
        end_fill()
        try:
            ri(args[0])
            forw(args[1])
            le(args[2])
            forw(args[3])
            end_fill()
        except:
            return
        return

    def star2(self):
        speed(6)
        penup()
        le(180)
        forw(180)
        ri(180)
        pendown()
        begin_fill()
        for i in range(9):
            forw(100)
            ri(60)
            forw(100)
            le(100)
        color("#eaeaea")
        end_fill()
        return

star_edit = Star_edit()

if num == 4:
    star_edit.star(2, 60, 120, 30, 120, 4), done()  

elif num == 5:
    star_edit.star(2, 20, 100, 30, 102, 5), done()

elif num == 6:
    star_edit.star(3, 20, 100, 40, 100, 6), done()

elif num == 7:
    star_edit.star(4, 20, 100,49, 100, 7, 95, 7, 90, 10), done()

elif num == 8: 
    star_edit.star(5, 0, 100, 55, 100, 8), done()

elif num == 9:
    star_edit.star2(), done()

else:
    print("Такой нет")
    star_edit.star2(), done()
    
 
