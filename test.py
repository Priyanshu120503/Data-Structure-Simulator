from turtle import Turtle, Screen
import tkinter
import math
import time


def edge_coordinate(c1, c2, r):
    # Assuming c1 is above c2
    # Also assuming the origin is top left of screen and y increases as we go down
    if c1[0] == c2[0]:
        return c2[0], c2[1] - r, c2[0], c1[1] + r
    angle = math.degrees(math.atan((c2[1]-c1[1])/(c1[0]-c2[0])))
    if angle >= 0:
        print('Inside if')
        x1, y1 = c2[0] + r * math.cos(math.radians(angle)), c2[1] - r * math.sin(math.radians(angle))
        x2, y2 = c1[0] - r * math.cos(math.radians(angle)), c1[1] + r * math.sin(math.radians(angle))
    else:
        angle = -angle
        x1, y1 = c2[0] - r * math.cos(math.radians(angle)), c2[1] - r * math.sin(math.radians(angle))
        x2, y2 = c1[0] + r * math.cos(math.radians(angle)), c1[1] + r * math.sin(math.radians(angle))
    return round(x1), round(y1), round(x2), round(y2)


window = tkinter.Tk()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
canvas = tkinter.Canvas(window, width=int(0.6*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#ffee38')
frame = tkinter.Frame(window, width=int(0.4*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#b2e49c')

y_coordinates = [100, 250, 400, 550]
node_diameter = 80

# l = canvas.create_line(240, 140, 190, 290)
c = canvas.create_oval(200, y_coordinates[0], 200 + node_diameter, y_coordinates[0] + node_diameter, fill='white')
d = canvas.create_oval(150, y_coordinates[1], 150 + node_diameter, y_coordinates[1] + node_diameter, fill='white')
e = canvas.create_oval(250, y_coordinates[1], 250 + node_diameter, y_coordinates[1] + node_diameter, fill='white')
f = canvas.create_oval(200, y_coordinates[2], 200 + node_diameter, y_coordinates[2] + node_diameter, fill='white')
x1, y1, x2, y2 = edge_coordinate((240, 140), (190, 290), node_diameter/2)
print(x1, y1, x2, y2)
canvas.create_line(x1, y1, x2, y2)
canvas.create_line(edge_coordinate((240, 140), (290, 290), node_diameter/2))
canvas.create_line(edge_coordinate((240, 140), (240, 440), 40))
print(canvas.coords(d))
canvas.place(x=0, y=0)
frame.place(x=int(0.6*SCREEN_WIDTH), y=0)

window.mainloop()




