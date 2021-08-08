# set the range of x-values
xmin = -10
xmax = 10

# set the range of y-values
ymin = -10
ymax = 10

# calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl
    background(255) # white
    translate(width/2, height/2)
    grid(xscl, yscl)
    
def grid(xscl, yscl):

    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    #for i in range(xmin, xmax+1):
    #    line(i*xscl, ymin*yscl, i*xscl, ymax*yscl) # draw horizontal line starting from (-10,-10) to (-10,10) -- x changes, y is maintained
    #    line(xmin*xscl, i*yscl, xmax*xscl, i*yscl) # draw vertical line starting from (-10,-10) to (10, -10) -- y changes, x is maintained
    for i in range(xmin, xmax+1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) # black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
