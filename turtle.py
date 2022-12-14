import turtle as trt
import random as rnd

num_side = int(input("Enter Your Shape's Sides Number: "))
color = input("Enter Your Desired Color: ")

trt.colormode(255)
trt.title("Shapes")
trt.speed(8)
trt.color("yellow")
trt.shape("circle")
trt.shapesize(0.001,0.001,0.001)
trt.pensize(10)
trt.pencolor(color)
trt.fillcolor(color)

trt.begin_fill()
for i in range(num_side):
    trt.bgcolor(rnd.randint(0 , 255) , rnd.randint(0 , 255) , rnd.randint(0 , 255))
    trt.forward(100)
    trt.left(360/num_side)
trt.end_fill()

trt.mainloop()

