from tkinter import *
import matplotlib.pyplot as plt

coordinates = []

def draw(event):
    global coordinates
    if(event):
        x1,y1=(event.x),(event.y)
        coordinates.append((x1,y1))
        #print(coordinates)    
        
    if not (event):
        exit()


my_window=Tk()
my_window.title("location")
my_canvas=Canvas(my_window,width=500,height=500,background='white')
my_canvas.grid(row=0,column=0)
my_canvas.bind('<B1-Motion>',draw)
my_window.mainloop()



"""
from tkinter import *
from pynput.mouse import Listener
from pynput import mouse



def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

   
listener = mouse.Listener(on_move=on_move)
listener.start()
    
my_window=Tk()
my_window.title("location")
my_canvas=Canvas(my_window,width=500,height=500,background='white')
my_canvas.grid(row=0,column=0)
my_canvas.bind("motion",on_move)
my_window.mainloop()

listener.stop()  
listener.join()
"""