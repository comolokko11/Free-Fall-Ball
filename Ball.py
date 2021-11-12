from DrawingPanel import *
import math

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

print(t1, "&", t2)

#from DrawingPanel import *
#import time
#panel=DrawingPanel(300,300,"light blue")
#for i in range (0,8):
#    panel.clear()
#    panel.fill_oval(10, 10+i*30, 20, 20,"red")
#    panel.sleep(880)
#for j in range (0,8):
#    panel.clear()
#    panel.fill_oval(200, 50+j*24, 20, 20,"blue")
#    panel.sleep(868)