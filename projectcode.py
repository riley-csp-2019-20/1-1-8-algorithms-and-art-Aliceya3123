#   a115_flower_image.py
import turtle as trtl

flowerbody= trtl.Turtle()
flowerbody.pensize(40)
flowerbody.circle(20)
w = 1
length = 90
circle = 380 / w
flowerbody.pensize(5)
flowerlegs = 0
   
# stem 
flowerbody.color("green")
flowerbody.pensize(10)
flowerbody.goto(0,-150)

flowerbody.shape("circle")
petals=0
while(petals <20):
    flowerbody.penup()
    flowerbody.goto(0,20)
    flowerbody.pendown()
    flowerbody.right(20)
    flowerbody.forward
    flowerbody.pendown
    flowerbody.circle(20)
    flowerbody.pendown



wn = trtl.Screen()
wn.mainloop()




