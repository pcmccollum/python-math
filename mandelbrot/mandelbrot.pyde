#range of x-values
xmin = -200
xmax = 20

#range of y-values
ymin = -20
ymax = 200

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    #colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    
def draw():
    #origin in center:
    translate(width/2,height/2)
    #go over all x's and y's on the grid
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl),
                 (ymin + y * yscl) ]
            #put it into the mandelbrot function
            col = mandelbrot(z,100)
            #if madelbrot returns 0
            if col == 100:
                fill(0) #make the rectangle black
            else:
                fill(3*col,255,255) #make the rectangle white
            #draw a tiny rectangle
            rect(x*xscl,y*yscl,1,1)

def mandelbrot(z,num):
    '''runs the process num time and returns the diverge count'''
    count = 0
    #define z1 as z
    z1 = z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z1) > 2.0:
            #return the step it divered on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    #if z hasn't diverged by the end
    return num

def cAdd(a, b):
    '''adds two complex numbers'''
    return [a[0]+b[0], a[1]+b[1]]

def cMult(u, v):
    '''multiplies two complex numbers'''
    return [u[0]*v[0] - u[1]*v[1], u[1]*v[0] + u[0]*v[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
