def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    # set background white
    background(0)
    translate(20,20)
    for x in range(30):
        for y in range(30):
            d = dist(30*x, 30*y, mouseX, mouseY) 
            fill(0.5*d, 255, 255)
            ellipse(30*x, 30*y, 25, 25)
            
