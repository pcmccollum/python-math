def setup():
    size(600,600)
    
def draw():
    translate(width/2, height/2)
    polygon(15,200) #3 sides, vertices 100 units from the center

def polygon(sides, sz):
    ''' draws a polygon given the number
    of sides and length from the center'''
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(sz*cos(i * step),
               sz*sin(i * step))
    endShape()
