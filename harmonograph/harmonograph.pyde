

def setup():
    size(600,600)
    noStroke()
    
def harmonograph(t):
    a1=a2=a3=a4 = 100 #amplitudes
    f1,f2,f3,f4 = 2.01,3,3,2 #frequencies
    p1,p2,p3,p4 = -PI/2,0,-PI/16,0 #phase shifts
    d1,d2,d3,d4 = 0.00085,0.0065,0,0 #decay constants
    x = a1*cos(f1*t + p1)*exp(-d1*t) + a3*cos(f3*t + p3)*exp(-d3*t)
    y = a2*sin(f2*t + p2)*exp(-d2*t) + a4*sin(f4*t + p4)*exp(-d4*t)
    return [x,y]

def draw():
    background(255)
    translate(width/2, height/2)
    t = 0
    points = []
    #save location to points list
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01   
    
    #go through points list and draw lines between them
    for i,p in enumerate(points):
        stroke(255,0,0) #red
        if i < len(points) - 1:
            line(p[0],p[1],points[i+1][0],points[i+1][1])
