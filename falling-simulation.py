from DrawingPanel import *
import math
import time

A= 5
v1 = 25
h1 = 600
v2 = 15
h2 = 500

def time(a,b,c):
    delta=math.sqrt(b**2-(4*a*c))
    t=(-b+delta)/(2*a)
    
    #return t if (t>0) else None
    if t>0: return t
    
t1 = time(A,v1,-h1)
t2 = time(A,v2,-h2)

#print(t1, "&", t2)

p = DrawingPanel(600, 600, "gray")

for i in range (0, int(t1)):
    p.clear()
    p.fill_oval(100, 10+i*60, 20, 20, "yellow")
    p.sleep(t1*100)
    
for j in range (0, int(t2)):
    p.clear()
    p.fill_oval(400, 110+j*48, 20, 20,"purple")
    p.sleep(t2*100)