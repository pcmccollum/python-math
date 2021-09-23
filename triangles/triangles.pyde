def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
    
t = 0

def draw():
    background(255) #white
    global t
    translate(width/2, height/2)
    for i in range(90):
        # space the triangles evenly
        # around the circle
        rotate(radians(360/90))
        pushMatrix() # save this orientation
        # go to circumference of circle
        translate(200,0)
        # spin each triangle
        rotate(radians(t+2*i*360/90))
        #draw the triangle
        tri(100, i)
        # return to saved orientation
        popMatrix()
    t += 0.5

def tri(length, strokeColor):
    '''Draws an equilateral triangle around center of triangle'''
    noFill() # make the triangle transparent
    stroke(strokeColor, 0, 0)
    triangle(0,-length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
