import axi
import random
A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds
BOUNDS = A4_LAND 

draw = True

"""

Statement:
"Machine Yearning"  is an artwork consisting of five words represented in binary
that depicts a crazy lover's visceral yearning for the beloved.


The binary strings correspond to the following: 

BELOVED 

01100010 01100101 01101100 01101111 01110110 01100101 01100100

UNTIL
01110101 01101110 01110100 01101001 01101100 00100000 

THEN
01010100 01101000 01100101 01101110 00001010

HAUNT
01001000 01100001 01110101 01101110 01110100 00100000

ME
01001101 01100101


zz = zero zero
zo = zero one
oz = one zero
oo = one one
"""



def draw_one(t,x,y):
    t.pu()
    t.goto(x+1.5,y-0.25)
    t.pd()
    t.goto(x+1,y)
    t.goto(x+1,y-2)
    t.pu() 
def draw_zero(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x+1,y)
    t.goto(x+1,y-2)
    t.goto(x,y-2)
    t.goto(x,y)
    t.goto(x+1,y-2)
    t.pu()



def zz(t, x, y):
    for i in range(2):
        draw_zero(t,x-(i*2), y)
def oo(t,x,y):
    for i in range(2):
     draw_one(t,x-(i*2), y)
def zo(t,x,y):
     draw_zero(t, x, y)
     draw_one(t,x-2, y)
def oz(t,x,y):
     draw_one(t, x, y)
     draw_zero(t,x-1, y)




def beloved(t,x,y):
   
    #B
    zo(t,x,y)
    oz(t,x-4,y)
    zz(t,x-8,y)
    oz(t,x-12,y)
    #E
    x = x-18  #the length of one letter is x-18
    zo(t,x,y)
    oz(t,x-4,y)
    zo(t,x-8,y)
    zo(t,x-12,y)
    #L
    x = x-18
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    zz(t,x-12,y)
    #O
    x = x-18
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    zz(t,x-12,y)
    #V

    x = x-18
    zo(t,x,y)
    oo(t,x-4,y)
    zo(t,x-8,y)
    oz(t,x-12,y)
    #E
    x = x-18  
    zo(t,x,y)
    oz(t,x-4,y)
    zo(t,x-8,y)
    zo(t,x-12,y)
    #D 
    x = x-18  
    zo(t,x,y)
    oz(t,x-4,y)
    zo(t,x-8,y)
    zz(t,x-12,y)

def until(t,x,y):
    #U
    zo(t,x,y)
    oz(t,x-4,y)
    zz(t,x-8,y)
    oz(t,x-12,y)

    #N 
    x = x-18
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    oz(t,x-12,y)

    #T 01110100
    x = x-18
    zo(t,x,y)
    oo(t,x-4,y)
    zo(t,x-8,y)
    zz(t,x-12,y)

    #I
    x = x-18
    zo(t,x,y)
    oz(t,x-4,y)
    oz(t,x-8,y)
    zo(t,x-12,y)

    #L 01101100
    x = x-18
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    zz(t,x-12,y)

def then(t,x,y):
    #T
    zo(t,x,y)
    oo(t,x-4,y)
    zo(t,x-8,y)
    zz(t,x-12,y)

    #H 
    x = (x-18)
    zo(t,x,y)
    oz(t,x-4,y)
    oz(t,x-8,y)
    zz(t,x-12,y)
    #E
    x = x-18  
    zo(t,x,y)
    oz(t,x-4,y)
    zo(t,x-8,y)
    zo(t,x-12,y)
    #N
    x = x-18
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    oz(t,x-12,y)

def hauntme(t, x, y):

    #H
    zo(t,x,y)
    oz(t,x-4,y)
    oz(t,x-8,y)
    zz(t,x-12,y)

    x = x-18

    #A 01100001
    zo(t,x,y)
    oz(t,x-4,y)
    zz(t,x-8,y)
    zo(t,x-12,y)

    x = x-18
    #U
    zo(t,x,y)
    oz(t,x-4,y)
    zz(t,x-8,y)
    oz(t,x-12,y)

    x = x-18
    #N
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    oz(t,x-12,y)

    x = x-18  
    #T
    zo(t,x,y)
    oo(t,x-4,y)
    zo(t,x-8,y)
    zz(t,x-12,y)

    x = (x-26) # - 26 because we want to give an additional white space between 'haunt' and 'me'
    #M
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    zo(t,x-12,y)

    x = x-18
    #E
    zo(t,x,y)
    oz(t,x-4,y)
    oo(t,x-8,y)
    zo(t,x-12,y)

    
def lover(t,x,y):
    beloved(t,-(((x-18)*6 )-12),y)
    until(t, -(((x-18)*6 )-12), -5)
    then(t, -(((x-18)*6 )-12), -10) 
    hauntme(t,-(((x-18)*6 )-12), -15)
    #x - 18 = the length of each letter
    # * 6 = we want to x to be on the last letter, the sixth letter
    # - 12 = the x axis of last binary pair of each letter is always x-12

def visceralYearning(t,x,y):

    # This function draws the phrase haunt me in random coordinates between a certain range. This is to give an impression
    # of the chaos inside the crazy, obsessive Lover mind. 
    
    for i in range(10):
        hauntme(t,random.randrange(-50,-1),random.randrange(-50,-20))


def main():
    t = axi.Turtle()
    lover(t,0,0)
    visceralYearning(t,0,0)

    # Scale letter to fit A4-sized paper
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    # Render drawing
    im = drawing.render()
    # Create an image file of the drawing
    im.write_to_png('out.png')
    # Draw with the plotter if relevant
    if draw:
        axi.draw(drawing)

if __name__ == '__main__':
    main()