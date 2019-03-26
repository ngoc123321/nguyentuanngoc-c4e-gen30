from turtle import *
speed(0.03)
shape('turtle')
def diamond (n, side_length):
    for i in range(6):
        left(60)
        for j in range(n):
                forward(side_length)
                left(360/n)
diamond(30,30)
    
    
mainloop()