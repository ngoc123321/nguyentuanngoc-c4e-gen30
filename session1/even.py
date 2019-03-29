from turtle import *
speed(0.03)
shape('turtle')
def diamond (n, side_length):
    for i in range(n):
        left(360/n)
        for j in range(n):
                forward(side_length)
                left(360/n)
diamond(40,15)
    
    
mainloop()